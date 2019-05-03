# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saveFuzzedPackets.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_saveFuzzedWindow(object):
    def setupUi(self, saveFuzzedWindow):
        saveFuzzedWindow.setObjectName("saveFuzzedWindow")
        saveFuzzedWindow.resize(467, 213)
        self.horizontalLayout = QtWidgets.QHBoxLayout(saveFuzzedWindow)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fuzzedPcapLabel = QtWidgets.QLabel(saveFuzzedWindow)
        self.fuzzedPcapLabel.setObjectName("fuzzedPcapLabel")
        self.horizontalLayout_2.addWidget(self.fuzzedPcapLabel)
        self.fuzzedPcap = QtWidgets.QLineEdit(saveFuzzedWindow)
        self.fuzzedPcap.setAlignment(QtCore.Qt.AlignCenter)
        self.fuzzedPcap.setObjectName("fuzzedPcap")
        self.horizontalLayout_2.addWidget(self.fuzzedPcap)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fuzzedDescriptionLabel = QtWidgets.QLabel(saveFuzzedWindow)
        self.fuzzedDescriptionLabel.setObjectName("fuzzedDescriptionLabel")
        self.horizontalLayout_3.addWidget(self.fuzzedDescriptionLabel)
        self.fuzzedDescription = QtWidgets.QLineEdit(saveFuzzedWindow)
        self.fuzzedDescription.setAlignment(QtCore.Qt.AlignCenter)
        self.fuzzedDescription.setObjectName("fuzzedDescription")
        self.horizontalLayout_3.addWidget(self.fuzzedDescription)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.fuzzedSaveButton = QtWidgets.QPushButton(saveFuzzedWindow)
        self.fuzzedSaveButton.setObjectName("fuzzedSaveButton")
        self.horizontalLayout_5.addWidget(self.fuzzedSaveButton)
        self.fuzzedCancelButton = QtWidgets.QPushButton(saveFuzzedWindow)
        self.fuzzedCancelButton.setObjectName("fuzzedCancelButton")
        self.horizontalLayout_5.addWidget(self.fuzzedCancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(saveFuzzedWindow)
        self.fuzzedCancelButton.clicked.connect(saveFuzzedWindow.close)
        QtCore.QMetaObject.connectSlotsByName(saveFuzzedWindow)

    def retranslateUi(self, saveFuzzedWindow):
        _translate = QtCore.QCoreApplication.translate
        saveFuzzedWindow.setWindowTitle(_translate("saveFuzzedWindow", "Save Fuzzed Packets"))
        self.fuzzedPcapLabel.setText(_translate("saveFuzzedWindow", "Fuzzed PCAP Name"))
        self.fuzzedPcap.setText(_translate("saveFuzzedWindow", "PCAP File"))
        self.fuzzedDescriptionLabel.setText(_translate("saveFuzzedWindow", "Description"))
        self.fuzzedDescription.setText(_translate("saveFuzzedWindow", "Description"))
        self.fuzzedSaveButton.setText(_translate("saveFuzzedWindow", "Save"))
        self.fuzzedCancelButton.setText(_translate("saveFuzzedWindow", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    saveFuzzedWindow = QtWidgets.QDialog()
    ui = Ui_saveFuzzedWindow()
    ui.setupUi(saveFuzzedWindow)
    saveFuzzedWindow.show()
    sys.exit(app.exec_())

