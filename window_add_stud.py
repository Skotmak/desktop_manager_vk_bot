# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_stud.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow3(object):
    def setupUi(self, MainWindow3):
        MainWindow3.setObjectName("MainWindow3")
        MainWindow3.resize(714, 370)
        self.centralwidget = QtWidgets.QWidget(MainWindow3)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 711, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.l_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.l_1.setFont(font)
        self.l_1.setObjectName("l_1")
        self.verticalLayout.addWidget(self.l_1)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)
        self.pte_f_name = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pte_f_name.setFont(font)
        self.pte_f_name.setObjectName("pte_f_name")
        self.gridLayout.addWidget(self.pte_f_name, 1, 2, 1, 1)
        self.pte_number = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pte_number.setFont(font)
        self.pte_number.setObjectName("pte_number")
        self.gridLayout.addWidget(self.pte_number, 3, 2, 1, 1)
        self.pte_l_name = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pte_l_name.setFont(font)
        self.pte_l_name.setObjectName("pte_l_name")
        self.gridLayout.addWidget(self.pte_l_name, 0, 2, 1, 1)
        self.pte_m_name = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pte_m_name.setFont(font)
        self.pte_m_name.setObjectName("pte_m_name")
        self.gridLayout.addWidget(self.pte_m_name, 2, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.status_new_stud = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.status_new_stud.setFont(font)
        self.status_new_stud.setText("")
        self.status_new_stud.setObjectName("status_new_stud")
        self.horizontalLayout_2.addWidget(self.status_new_stud)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(80)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.add_btn.setFont(font)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout.addWidget(self.add_btn)
        self.clean_pte_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.clean_pte_btn.setFont(font)
        self.clean_pte_btn.setObjectName("clean_pte_btn")
        self.horizontalLayout.addWidget(self.clean_pte_btn)
        self.close_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.close_btn.setFont(font)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow3.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow3)

    def retranslateUi(self, MainWindow3):
        _translate = QtCore.QCoreApplication.translate
        MainWindow3.setWindowTitle(_translate("MainWindow3", "Добавление нового студента"))
        self.l_1.setText(_translate("MainWindow3", "<html><head/><body><p align=\"center\">Добавление нового студента</p></body></html>"))
        self.label_8.setText(_translate("MainWindow3", "<html><head/><body><p align=\"right\">Отчество:</p></body></html>"))
        self.label_6.setText(_translate("MainWindow3", "<html><head/><body><p align=\"right\">Номер студенческого:</p></body></html>"))
        self.label_9.setText(_translate("MainWindow3", "<html><head/><body><p align=\"right\">Имя:</p></body></html>"))
        self.label_7.setText(_translate("MainWindow3", "<html><head/><body><p align=\"right\">Фамилия:</p></body></html>"))
        self.label.setText(_translate("MainWindow3", "<html><head/><body><p align=\"right\">Статус:</p></body></html>"))
        self.add_btn.setText(_translate("MainWindow3", "Добавить"))
        self.clean_pte_btn.setText(_translate("MainWindow3", "Очистить"))
        self.close_btn.setText(_translate("MainWindow3", "Закрыть"))
