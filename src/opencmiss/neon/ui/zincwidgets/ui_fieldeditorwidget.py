# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fieldeditorwidget.ui'
#
# Created: Fri Apr 15 13:43:43 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FieldEditorWidget(object):
    def setupUi(self, FieldEditorWidget):
        FieldEditorWidget.setObjectName("FieldEditorWidget")
        FieldEditorWidget.setEnabled(True)
        FieldEditorWidget.resize(298, 1030)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FieldEditorWidget.sizePolicy().hasHeightForWidth())
        FieldEditorWidget.setSizePolicy(sizePolicy)
        FieldEditorWidget.setMinimumSize(QtCore.QSize(180, 0))
        self.gridLayout_2 = QtGui.QGridLayout(FieldEditorWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.field_type_label = QtGui.QLabel(FieldEditorWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.field_type_label.sizePolicy().hasHeightForWidth())
        self.field_type_label.setSizePolicy(sizePolicy)
        self.field_type_label.setMinimumSize(QtCore.QSize(100, 27))
        self.field_type_label.setObjectName("field_type_label")
        self.gridLayout_2.addWidget(self.field_type_label, 0, 0, 1, 1)
        self.field_type_chooser = FieldTypeChooserWidget(FieldEditorWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.field_type_chooser.sizePolicy().hasHeightForWidth())
        self.field_type_chooser.setSizePolicy(sizePolicy)
        self.field_type_chooser.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.field_type_chooser.setObjectName("field_type_chooser")
        self.gridLayout_2.addWidget(self.field_type_chooser, 0, 1, 1, 1)
        self.sourcefields_groupbox = QtGui.QGroupBox(FieldEditorWidget)
        self.sourcefields_groupbox.setObjectName("sourcefields_groupbox")
        self.gridLayout_4 = QtGui.QGridLayout(self.sourcefields_groupbox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.number_of_source_fields_label = QtGui.QLabel(self.sourcefields_groupbox)
        self.number_of_source_fields_label.setObjectName("number_of_source_fields_label")
        self.gridLayout_4.addWidget(self.number_of_source_fields_label, 0, 0, 1, 1)
        self.number_of_source_fields_lineedit = QtGui.QLineEdit(self.sourcefields_groupbox)
        self.number_of_source_fields_lineedit.setEnabled(False)
        self.number_of_source_fields_lineedit.setObjectName("number_of_source_fields_lineedit")
        self.gridLayout_4.addWidget(self.number_of_source_fields_lineedit, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.sourcefields_groupbox, 3, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 6, 0, 1, 1)
        self.create_group = QtGui.QGroupBox(FieldEditorWidget)
        self.create_group.setMinimumSize(QtCore.QSize(180, 0))
        self.create_group.setTitle("")
        self.create_group.setObjectName("create_group")
        self.gridLayout_5 = QtGui.QGridLayout(self.create_group)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.create_button = QtGui.QPushButton(self.create_group)
        self.create_button.setObjectName("create_button")
        self.gridLayout_5.addWidget(self.create_button, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.create_group, 5, 0, 1, 1)
        self.coordinate_system_groupbox = QtGui.QGroupBox(FieldEditorWidget)
        self.coordinate_system_groupbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.coordinate_system_groupbox.setFlat(False)
        self.coordinate_system_groupbox.setObjectName("coordinate_system_groupbox")
        self.gridLayout = QtGui.QGridLayout(self.coordinate_system_groupbox)
        self.gridLayout.setObjectName("gridLayout")
        self.coordinate_system_type_label = QtGui.QLabel(self.coordinate_system_groupbox)
        self.coordinate_system_type_label.setObjectName("coordinate_system_type_label")
        self.gridLayout.addWidget(self.coordinate_system_type_label, 0, 0, 1, 1)
        self.coordinate_system_type_chooser = FieldChooserWidget(self.coordinate_system_groupbox)
        self.coordinate_system_type_chooser.setEditable(False)
        self.coordinate_system_type_chooser.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.coordinate_system_type_chooser.setObjectName("coordinate_system_type_chooser")
        self.coordinate_system_type_chooser.addItem("")
        self.coordinate_system_type_chooser.addItem("")
        self.coordinate_system_type_chooser.addItem("")
        self.coordinate_system_type_chooser.addItem("")
        self.coordinate_system_type_chooser.addItem("")
        self.coordinate_system_type_chooser.addItem("")
        self.gridLayout.addWidget(self.coordinate_system_type_chooser, 0, 1, 1, 1)
        self.coordinate_system_focus_label = QtGui.QLabel(self.coordinate_system_groupbox)
        self.coordinate_system_focus_label.setObjectName("coordinate_system_focus_label")
        self.gridLayout.addWidget(self.coordinate_system_focus_label, 1, 0, 1, 1)
        self.coordinate_system_focus_lineedit = QtGui.QLineEdit(self.coordinate_system_groupbox)
        self.coordinate_system_focus_lineedit.setObjectName("coordinate_system_focus_lineedit")
        self.gridLayout.addWidget(self.coordinate_system_focus_lineedit, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.coordinate_system_groupbox, 2, 0, 1, 2)
        self.derived_groupbox = QtGui.QGroupBox(FieldEditorWidget)
        self.derived_groupbox.setObjectName("derived_groupbox")
        self.gridLayout_9 = QtGui.QGridLayout(self.derived_groupbox)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.derived_values_lineedit = QtGui.QLineEdit(self.derived_groupbox)
        self.derived_values_lineedit.setEnabled(False)
        self.derived_values_lineedit.setObjectName("derived_values_lineedit")
        self.gridLayout_9.addWidget(self.derived_values_lineedit, 0, 2, 1, 1)
        self.derived_chooser_1 = QtGui.QComboBox(self.derived_groupbox)
        self.derived_chooser_1.setObjectName("derived_chooser_1")
        self.gridLayout_9.addWidget(self.derived_chooser_1, 1, 2, 1, 1)
        self.derived_values_label = QtGui.QLabel(self.derived_groupbox)
        self.derived_values_label.setObjectName("derived_values_label")
        self.gridLayout_9.addWidget(self.derived_values_label, 0, 0, 1, 1)
        self.derived_combo_label_1 = QtGui.QLabel(self.derived_groupbox)
        self.derived_combo_label_1.setObjectName("derived_combo_label_1")
        self.gridLayout_9.addWidget(self.derived_combo_label_1, 1, 0, 1, 1)
        self.derived_combo_label_2 = QtGui.QLabel(self.derived_groupbox)
        self.derived_combo_label_2.setObjectName("derived_combo_label_2")
        self.gridLayout_9.addWidget(self.derived_combo_label_2, 2, 0, 1, 1)
        self.derived_chooser_2 = QtGui.QComboBox(self.derived_groupbox)
        self.derived_chooser_2.setObjectName("derived_chooser_2")
        self.gridLayout_9.addWidget(self.derived_chooser_2, 2, 2, 1, 1)
        self.gridLayout_2.addWidget(self.derived_groupbox, 4, 0, 1, 2)
        self.general_groupbox = QtGui.QGroupBox(FieldEditorWidget)
        self.general_groupbox.setEnabled(True)
        self.general_groupbox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.general_groupbox.setTitle("")
        self.general_groupbox.setCheckable(False)
        self.general_groupbox.setObjectName("general_groupbox")
        self.gridLayout_3 = QtGui.QGridLayout(self.general_groupbox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.type_coordinate_checkbox = QtGui.QCheckBox(self.general_groupbox)
        self.type_coordinate_checkbox.setObjectName("type_coordinate_checkbox")
        self.gridLayout_3.addWidget(self.type_coordinate_checkbox, 1, 0, 1, 1)
        self.managed_checkbox = QtGui.QCheckBox(self.general_groupbox)
        self.managed_checkbox.setObjectName("managed_checkbox")
        self.gridLayout_3.addWidget(self.managed_checkbox, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.general_groupbox, 1, 0, 1, 2)

        self.retranslateUi(FieldEditorWidget)
        QtCore.QMetaObject.connectSlotsByName(FieldEditorWidget)

    def retranslateUi(self, FieldEditorWidget):
        FieldEditorWidget.setWindowTitle(QtGui.QApplication.translate("FieldEditorWidget", "Field Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.field_type_label.setText(QtGui.QApplication.translate("FieldEditorWidget", "Field type:", None, QtGui.QApplication.UnicodeUTF8))
        self.sourcefields_groupbox.setTitle(QtGui.QApplication.translate("FieldEditorWidget", "Source fields:", None, QtGui.QApplication.UnicodeUTF8))
        self.number_of_source_fields_label.setText(QtGui.QApplication.translate("FieldEditorWidget", "Number of source fields:", None, QtGui.QApplication.UnicodeUTF8))
        self.create_button.setText(QtGui.QApplication.translate("FieldEditorWidget", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.coordinate_system_groupbox.setTitle(QtGui.QApplication.translate("FieldEditorWidget", "Coordinate System:", None, QtGui.QApplication.UnicodeUTF8))
        self.coordinate_system_type_label.setText(QtGui.QApplication.translate("FieldEditorWidget", "Coordinate system type:", None, QtGui.QApplication.UnicodeUTF8))
        self.coordinate_system_type_chooser.setItemText(0, QtGui.QApplication.translate("FieldEditorWidget", "Rectangular Cartesian", None, QtGui.QApplication.UnicodeUTF8))
        self.coordinate_system_type_chooser.setItemText(1, QtGui.QApplication.translate("FieldEditorWidget", "Cylindrial Polar", None, QtGui.QApplication.UnicodeUTF8))
        self.coordinate_system_type_chooser.setItemText(2, QtGui.QApplication.translate("FieldEditorWidget", "Spherical Polar", None, QtGui.QApplication.UnicodeUTF8))
        self.coordinate_system_type_chooser.setItemText(3, QtGui.QApplication.translate("FieldEditorWidget", "Prolate Spheroidal", None, QtGui.QApplication.UnicodeUTF8))
        self.coordinate_system_type_chooser.setItemText(4, QtGui.QApplication.translate("FieldEditorWidget", "Oblate Spheroidal", None, QtGui.QApplication.UnicodeUTF8))
        self.coordinate_system_type_chooser.setItemText(5, QtGui.QApplication.translate("FieldEditorWidget", "Fibre", None, QtGui.QApplication.UnicodeUTF8))
        self.coordinate_system_focus_label.setText(QtGui.QApplication.translate("FieldEditorWidget", "Coordinate system focus:", None, QtGui.QApplication.UnicodeUTF8))
        self.derived_groupbox.setTitle(QtGui.QApplication.translate("FieldEditorWidget", "Derived Parameters:", None, QtGui.QApplication.UnicodeUTF8))
        self.derived_values_label.setText(QtGui.QApplication.translate("FieldEditorWidget", "Constant Values:", None, QtGui.QApplication.UnicodeUTF8))
        self.derived_combo_label_1.setText(QtGui.QApplication.translate("FieldEditorWidget", "Derived combo1", None, QtGui.QApplication.UnicodeUTF8))
        self.derived_combo_label_2.setText(QtGui.QApplication.translate("FieldEditorWidget", "Derived combo2", None, QtGui.QApplication.UnicodeUTF8))
        self.type_coordinate_checkbox.setText(QtGui.QApplication.translate("FieldEditorWidget", "Type Coordinate", None, QtGui.QApplication.UnicodeUTF8))
        self.managed_checkbox.setText(QtGui.QApplication.translate("FieldEditorWidget", "Managed", None, QtGui.QApplication.UnicodeUTF8))

from opencmiss.neon.ui.zincwidgets.fieldchooserwidget import FieldChooserWidget
from opencmiss.neon.ui.zincwidgets.fieldtypechooserwidget import FieldTypeChooserWidget