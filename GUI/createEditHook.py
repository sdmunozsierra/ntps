# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createEditHook.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Hook.hook_manager import hookManager
from pyglobals import h_manager

class Ui_CreateEditHookWindow(object):
    #Signal to send to GUI
    #signal = pyqtSignal(int)

    def adding(self):

        name = self.newHookName.text()
        hookdescription = self.newHookDescription.text()
        filepath = self.newHookPath.text()

        print("File path before sent to manager: ",filepath)
        print("Name", name)

        # manager = hookManager()
        # ntps.
        h_manager.addhook(name, hookdescription, False, 0, filepath)

    def browse(self):
        filebrowser = QtWidgets.QFileDialog()
        filebrowser.setNameFilters(["Python files (*.py)"])
        filebrowser.selectNameFilter("Python files (*.py)")
        filters = "Python files (*.py)"
        selectedfilter = "Python files (*.py))"

        filename = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QFileDialog(),"File Dialog", '', filters, selectedfilter)



        if filename[0] == '':
            return

        _translate = QtCore.QCoreApplication.translate

        self.newHookPath.setText(_translate("CreateEditHookWindow", filename[0]))


    def setupUi(self, CreateEditHookWindow):
        CreateEditHookWindow.setObjectName("CreateEditHookWindow")
        CreateEditHookWindow.resize(400, 214)
        self.horizontalLayout = QtWidgets.QHBoxLayout(CreateEditHookWindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.newHookNameLabel = QtWidgets.QLabel(CreateEditHookWindow)
        self.newHookNameLabel.setObjectName("newHookNameLabel")
        self.horizontalLayout_2.addWidget(self.newHookNameLabel)
        self.newHookName = QtWidgets.QLineEdit(CreateEditHookWindow)
        self.newHookName.setAlignment(QtCore.Qt.AlignCenter)
        self.newHookName.setObjectName("newHookName")
        self.horizontalLayout_2.addWidget(self.newHookName)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.newHookDescriptionlabel = QtWidgets.QLabel(CreateEditHookWindow)
        self.newHookDescriptionlabel.setObjectName("newHookDescriptionlabel")
        self.horizontalLayout_3.addWidget(self.newHookDescriptionlabel)
        self.newHookDescription = QtWidgets.QLineEdit(CreateEditHookWindow)
        self.newHookDescription.setAlignment(QtCore.Qt.AlignCenter)
        self.newHookDescription.setObjectName("newHookDescription")
        self.horizontalLayout_3.addWidget(self.newHookDescription)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.newHookPathLabel = QtWidgets.QLabel(CreateEditHookWindow)
        self.newHookPathLabel.setObjectName("newHookPathLabel")
        self.horizontalLayout_4.addWidget(self.newHookPathLabel)
        self.newHookPath = QtWidgets.QLineEdit(CreateEditHookWindow)
        self.newHookPath.setAlignment(QtCore.Qt.AlignCenter)
        self.newHookPath.setObjectName("newHookPath")
        self.horizontalLayout_4.addWidget(self.newHookPath)
        self.newHookBrowseButton = QtWidgets.QPushButton(CreateEditHookWindow)
        self.newHookBrowseButton.setObjectName("newHookBrowseButton")

        self.newHookBrowseButton.clicked.connect(self.browse)

        self.horizontalLayout_4.addWidget(self.newHookBrowseButton)

        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.newHookSaveButton = QtWidgets.QPushButton(CreateEditHookWindow)
        self.newHookSaveButton.setObjectName("newHookSaveButton")
        #Save button
        self.newHookSaveButton.clicked.connect(self.adding)
        self.newHookSaveButton.clicked.connect(CreateEditHookWindow.close)
        #GUI call



        self.horizontalLayout_5.addWidget(self.newHookSaveButton)
        self.newHookCancelButton = QtWidgets.QPushButton(CreateEditHookWindow)
        self.newHookCancelButton.setObjectName("newHookCancelButton")
        self.horizontalLayout_5.addWidget(self.newHookCancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(CreateEditHookWindow)
        self.newHookCancelButton.clicked.connect(CreateEditHookWindow.close)
        QtCore.QMetaObject.connectSlotsByName(CreateEditHookWindow)

    def retranslateUi(self, CreateEditHookWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateEditHookWindow.setWindowTitle(_translate("CreateEditHookWindow", "Create/Edit Hook"))
        self.newHookNameLabel.setText(_translate("CreateEditHookWindow", "Hook Name"))
        self.newHookName.setText(_translate("CreateEditHookWindow", "Hook name"))
        self.newHookDescriptionlabel.setText(_translate("CreateEditHookWindow", "Description"))
        self.newHookDescription.setText(_translate("CreateEditHookWindow", "Description"))
        self.newHookPathLabel.setText(_translate("CreateEditHookWindow", "Hook Path"))
        self.newHookPath.setText(_translate("CreateEditHookWindow", "Hook path"))
        self.newHookBrowseButton.setText(_translate("CreateEditHookWindow", "Browse"))
        self.newHookSaveButton.setText(_translate("CreateEditHookWindow", "Save"))
        self.newHookCancelButton.setText(_translate("CreateEditHookWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateEditHookWindow = QtWidgets.QDialog()
    ui = Ui_CreateEditHookWindow()
    ui.setupUi(CreateEditHookWindow)
    CreateEditHookWindow.show()
    sys.exit(app.exec_())
