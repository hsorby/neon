# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res\designer\preferencesdialog.ui'
#
# Created: Mon May  9 12:37:28 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        PreferencesDialog.setObjectName("PreferencesDialog")
        PreferencesDialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(PreferencesDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtGui.QTabWidget(PreferencesDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tabToolbars = QtGui.QWidget()
        self.tabToolbars.setObjectName("tabToolbars")
        self.horizontalLayout = QtGui.QHBoxLayout(self.tabToolbars)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidgetToolbars = QtGui.QListWidget(self.tabToolbars)
        self.listWidgetToolbars.setEditTriggers(QtGui.QAbstractItemView.CurrentChanged)
        self.listWidgetToolbars.setViewMode(QtGui.QListView.ListMode)
        self.listWidgetToolbars.setObjectName("listWidgetToolbars")
        self.horizontalLayout.addWidget(self.listWidgetToolbars)
        self.widgetToolbar = QtGui.QWidget(self.tabToolbars)
        self.widgetToolbar.setObjectName("widgetToolbar")
        self.horizontalLayout.addWidget(self.widgetToolbar)
        self.tabWidget.addTab(self.tabToolbars, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(PreferencesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(PreferencesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), PreferencesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), PreferencesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PreferencesDialog)

    def retranslateUi(self, PreferencesDialog):
        PreferencesDialog.setWindowTitle(QtGui.QApplication.translate("PreferencesDialog", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabToolbars), QtGui.QApplication.translate("PreferencesDialog", "Toolbars", None, QtGui.QApplication.UnicodeUTF8))

