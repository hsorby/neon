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
import json
from PySide import QtCore, QtGui

from opencmiss.neon.core.neonlogger import NeonLogger

from opencmiss.neon.ui.dialogs.ui_preferencesdialog import Ui_PreferencesDialog


class PreferencesDialog(QtGui.QDialog):

    def __init__(self, parent):
        super(PreferencesDialog, self).__init__(parent)

        self._ui = Ui_PreferencesDialog()
        self._ui.setupUi(self)
        self._original_state = {}

    def showEvent(self, event):
        super(PreferencesDialog, self).showEvent(event)
        self._updateUi()

    def accept(self):
        current_state = self._getInterfaceState()
        if current_state != self._original_state:
            self._setState(current_state)

        super(PreferencesDialog, self).accept()

    def _updateUi(self):
        current_state = self._getState()
        self._original_state = current_state.copy()
        if 'toolbars' in current_state:
            self._ui.listWidgetToolbars.clear()
            toolbars_state = current_state['toolbars']
            self._setToolBarInterfaceState(toolbars_state)

    def _getToolBarState(self):
        main_window = self.parent()
        state = []
        state.append((main_window._ui.toolBarFile.objectName(), main_window._ui.toolBarFile.isVisible()))
        state.append((main_window._ui.toolBarEdit.objectName(), main_window._ui.toolBarEdit.isVisible()))
        state.append((main_window._ui.toolBarView.objectName(), main_window._ui.toolBarView.isVisible()))
        state.append((main_window._ui.toolBarDialog.objectName(), main_window._ui.toolBarDialog.isVisible()))
        return state

    def _setToolBarInterfaceState(self, state):
        for toolbar_state in state:
            item = QtGui.QListWidgetItem(getDisplayName(toolbar_state[0]))
            item.setCheckState(QtCore.Qt.Checked if toolbar_state[1] else QtCore.Qt.Unchecked)
            self._ui.listWidgetToolbars.addItem(item)

    def _getToolBarInterfaceState(self):
        state =[]
        for index in range(self._ui.listWidgetToolbars.count()):
            item = self._ui.listWidgetToolbars.item(index)
            state.append((getObjectName(item.text()), item.checkState() == QtCore.Qt.Checked))

        return state

    def _setToolBarState(self, state):
        main_window = self.parent()
        for toolbar_state in state:
            toolbar_name = toolbar_state[0]
            toolbar = getattr(main_window._ui, toolbar_name)
            toolbar.setVisible(toolbar_state[1])

    def _getInterfaceState(self):
        state = {}
        state['toolbars'] = self._getToolBarInterfaceState()
        return state

    def _getState(self):
        state = {}
        state['toolbars'] = self._getToolBarState()
        return state

    def _setState(self, state):
        if 'toolbars' in state:
            self._setToolBarState(state['toolbars'])

    def serialize(self):
        state = self._getState()
        return json.dumps(state)

    def deserialize(self, string):
        try:
            state = json.loads(string)
            self._setState(state)
        except ValueError as e:
            NeonLogger.getLogger().error("Failed to read application preferences.\n" + str(e))


name_map = {}
name_map['toolBarDialog'] = 'Dialog toolbar'
name_map['toolBarView'] = 'View toolbar'
name_map['toolBarEdit'] = 'Edit toolbar'
name_map['toolBarFile'] = 'File toolbar'


def getObjectName(name):

    object_name = "not-found"
    list_of_name = [k for k, v in name_map.items() if v == name]
    if list_of_name:
        object_name = list_of_name[0]

    return object_name


def getDisplayName(name):

    display_name = "not-found"
    if name in name_map:
        display_name = name_map[name]

    return display_name