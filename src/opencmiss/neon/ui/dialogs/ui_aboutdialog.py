# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/designer/aboutdialog.ui'
#
# Created: Tue May 17 20:55:29 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(AboutDialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelTitle = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Zekton")
        font.setPointSize(28)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout_2.addWidget(self.labelTitle)
        self.labelDescritpion = QtGui.QLabel(self.frame)
        self.labelDescritpion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDescritpion.setWordWrap(True)
        self.labelDescritpion.setOpenExternalLinks(True)
        self.labelDescritpion.setObjectName("labelDescritpion")
        self.verticalLayout_2.addWidget(self.labelDescritpion)
        self.verticalLayout.addWidget(self.frame)
        self.buttonBox = QtGui.QDialogButtonBox(AboutDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AboutDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), AboutDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), AboutDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QtGui.QApplication.translate("AboutDialog", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTitle.setText(QtGui.QApplication.translate("AboutDialog", "OpenCMISS-Neon", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDescritpion.setText(QtGui.QApplication.translate("AboutDialog", "Visual editing environment for OpenCMISS [http://opencmiss.org].", None, QtGui.QApplication.UnicodeUTF8))

