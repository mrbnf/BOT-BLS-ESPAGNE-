# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mygui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(855, 554)
        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(300, 30, 211, 41))
        self.startButton.setObjectName("startButton")
        self.manualCheckBox = QtWidgets.QCheckBox(Dialog)
        self.manualCheckBox.setEnabled(True)
        self.manualCheckBox.setGeometry(QtCore.QRect(800, 70, 41, 25))
        self.manualCheckBox.setAutoFillBackground(False)
        self.manualCheckBox.setText("")
        self.manualCheckBox.setObjectName("manualCheckBox")
        self.loginAllCheckBox = QtWidgets.QCheckBox(Dialog)
        self.loginAllCheckBox.setGeometry(QtCore.QRect(800, 40, 31, 25))
        self.loginAllCheckBox.setText("")
        self.loginAllCheckBox.setChecked(False)
        self.loginAllCheckBox.setObjectName("loginAllCheckBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(730, 40, 71, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(730, 70, 61, 20))
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 831, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.addTable = QtWidgets.QTableWidget(Dialog)
        self.addTable.setGeometry(QtCore.QRect(10, 480, 721, 51))
        self.addTable.setObjectName("addTable")
        self.addTable.setColumnCount(0)
        self.addTable.setRowCount(0)
        self.addButton = QtWidgets.QPushButton(Dialog)
        self.addButton.setGeometry(QtCore.QRect(730, 500, 88, 27))
        self.addButton.setObjectName("addButton")
        self.deleteButton = QtWidgets.QPushButton(Dialog)
        self.deleteButton.setGeometry(QtCore.QRect(750, 460, 88, 21))
        self.deleteButton.setObjectName("deleteButton")
        self.calenderBox = QtWidgets.QComboBox(Dialog)
        self.calenderBox.setGeometry(QtCore.QRect(730, 10, 79, 27))
        self.calenderBox.setObjectName("calenderBox")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(650, 10, 67, 19))
        self.label_3.setObjectName("label_3")
        self.selfieCheckBox = QtWidgets.QCheckBox(Dialog)
        self.selfieCheckBox.setGeometry(QtCore.QRect(20, 20, 92, 25))
        self.selfieCheckBox.setChecked(True)
        self.selfieCheckBox.setObjectName("selfieCheckBox")
        self.paymentCheckBox = QtWidgets.QCheckBox(Dialog)
        self.paymentCheckBox.setGeometry(QtCore.QRect(20, 60, 92, 25))
        self.paymentCheckBox.setChecked(True)
        self.paymentCheckBox.setObjectName("paymentCheckBox")
        self.saveButton = QtWidgets.QPushButton(Dialog)
        self.saveButton.setGeometry(QtCore.QRect(660, 460, 88, 21))
        self.saveButton.setObjectName("saveButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.startButton.setText(_translate("Dialog", "Start Notifications"))
        self.label.setText(_translate("Dialog", "Login All"))
        self.label_2.setText(_translate("Dialog", " Manual"))
        self.addButton.setText(_translate("Dialog", "Add"))
        self.deleteButton.setText(_translate("Dialog", "Delete"))
        self.label_3.setText(_translate("Dialog", "Calender"))
        self.selfieCheckBox.setText(_translate("Dialog", "Selfie Auto"))
        self.paymentCheckBox.setText(_translate("Dialog", "Payment Auto"))
        self.saveButton.setText(_translate("Dialog", "Save"))
