'''
   Copyright 2015 University of Auckland

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''
import os.path

from PySide import QtCore, QtGui

from opencmiss.neon.ui.ui_mainwindow import Ui_MainWindow
from opencmiss.neon.undoredo.commands import CommandEmpty
from opencmiss.neon.ui.views.defaultview import DefaultView

class MainWindow(QtGui.QMainWindow):
    
    def __init__(self, model):
        super(MainWindow, self).__init__()
        self._model = model
        
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        
        self._location = None # The last location/directory used by the application
        
        self._undoRedoStack = QtGui.QUndoStack(self)
        
        self._readSettings()
        
        self._makeConnections()
        
        # List of possible views
        view_list = [DefaultView()]
        self._setupViews(view_list)

        # Set the undo redo stack state
        self._undoRedoStack.push(CommandEmpty())
        self._undoRedoStack.clear()
        
    def _makeConnections(self):
        self._ui.action_Quit.triggered.connect(self.quitApplication)
        self._ui.action_Open.triggered.connect(self._open)
        
        
        self._undoRedoStack.indexChanged.connect(self._undoRedoStackIndexChanged)
        self._undoRedoStack.canUndoChanged.connect(self._ui.action_Undo.setEnabled)
        self._undoRedoStack.canRedoChanged.connect(self._ui.action_Redo.setEnabled)
        
    def _writeSettings(self):
        settings = QtCore.QSettings()
        settings.beginGroup('MainWindow')
        settings.setValue('size', self.size())
        settings.setValue('pos', self.pos())
        settings.setValue('location', self._location)
        settings.endGroup()
        
    def _readSettings(self):
        settings = QtCore.QSettings()
        settings.beginGroup('MainWindow')
        self.resize(settings.value('size', QtCore.QSize(1200, 900)))
        self.move(settings.value('pos', QtCore.QPoint(100, 150)))
        self._location = settings.value('location', QtCore.QDir.homePath())
        settings.endGroup()
    
    def _setupViews(self, views):
        action_group = QtGui.QActionGroup(self)
        context = self._model.getContext()
        for v in views:
            v.setContext(context)
            self._ui.viewStackedWidget.addWidget(v)
            
            action_view = QtGui.QAction(v.name(), self)
            action_view.setCheckable(True)
            action_view.setChecked(True)
            action_view.setActionGroup(action_group)
            self._ui.menu_View.addAction(action_view)
    
    def _undoRedoStackIndexChanged(self, index):
        self._model.setCurrentUndoRedoIndex(index)
        
    def _open(self):
        filename, _ = QtGui.QFileDialog.getOpenFileName(self, caption='Choose file ...', dir=self._location, filter="Neon Files (*.neon, *.json);;All (*.*)")
        
        if filename:
            self._location = os.path.dirname(filename)
            self._model.load(filename)
    
    def confirmClose(self):
        # Check to see if the Workflow is in a saved state.
        if self._model.isModified():
            ret = QtGui.QMessageBox.warning(self, 'Unsaved Changes', 'You have unsaved changes, would you like to save these changes now?',
                                      QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if ret == QtGui.QMessageBox.Yes:
                self._model.save()

    
    def quitApplication(self):
        self.confirmClose()
        
        self._writeSettings()
        
        QtGui.qApp.quit()
        
        
        