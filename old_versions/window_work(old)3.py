# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'work.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(800, 682)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 8, 791, 671))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.l_name = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_name.sizePolicy().hasHeightForWidth())
        self.l_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.l_name.setFont(font)
        self.l_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.l_name.setAutoFillBackground(False)
        self.l_name.setTextFormat(QtCore.Qt.AutoText)
        self.l_name.setAlignment(QtCore.Qt.AlignCenter)
        self.l_name.setWordWrap(False)
        self.l_name.setObjectName("l_name")
        self.verticalLayout.addWidget(self.l_name)
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 781, 591))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_3.addWidget(self.pushButton_9)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_3.addWidget(self.pushButton_7)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 781, 591))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pushButton_28 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_28.setObjectName("pushButton_28")
        self.verticalLayout_8.addWidget(self.pushButton_28)
        self.pushButton_29 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_29.setObjectName("pushButton_29")
        self.verticalLayout_8.addWidget(self.pushButton_29)
        self.pushButton_30 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_30.setObjectName("pushButton_30")
        self.verticalLayout_8.addWidget(self.pushButton_30)
        self.pushButton_31 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_31.setObjectName("pushButton_31")
        self.verticalLayout_8.addWidget(self.pushButton_31)
        self.pushButton_32 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_32.setObjectName("pushButton_32")
        self.verticalLayout_8.addWidget(self.pushButton_32)
        self.pushButton_33 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_33.setObjectName("pushButton_33")
        self.verticalLayout_8.addWidget(self.pushButton_33)
        self.pushButton_34 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_34.setObjectName("pushButton_34")
        self.verticalLayout_8.addWidget(self.pushButton_34)
        self.horizontalLayout_7.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.verticalLayout_9.addWidget(self.plainTextEdit_4)
        self.dateEdit = QtWidgets.QDateEdit(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_9.addWidget(self.dateEdit)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_35 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_35.setObjectName("pushButton_35")
        self.horizontalLayout_8.addWidget(self.pushButton_35)
        self.pushButton_36 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_36.sizePolicy().hasHeightForWidth())
        self.pushButton_36.setSizePolicy(sizePolicy)
        self.pushButton_36.setObjectName("pushButton_36")
        self.horizontalLayout_8.addWidget(self.pushButton_36)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7.addLayout(self.verticalLayout_9)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow2.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow2)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "Управление ботом РУДН"))
        self.l_name.setText(_translate("MainWindow2", "Привет, ИМЯ!"))
        self.pushButton_6.setText(_translate("MainWindow2", "Понедельник"))
        self.pushButton_8.setText(_translate("MainWindow2", "Вторник"))
        self.pushButton_9.setText(_translate("MainWindow2", "Среда"))
        self.pushButton_7.setText(_translate("MainWindow2", "Четверг"))
        self.pushButton_5.setText(_translate("MainWindow2", "Пятница"))
        self.pushButton_4.setText(_translate("MainWindow2", "Суббота"))
        self.pushButton.setText(_translate("MainWindow2", "Воскресенье"))
        self.pushButton_3.setText(_translate("MainWindow2", "Сбросить изменения"))
        self.pushButton_2.setText(_translate("MainWindow2", "Применить изменения"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow2", "Обычное расписание"))
        self.pushButton_28.setText(_translate("MainWindow2", "Понедельник"))
        self.pushButton_29.setText(_translate("MainWindow2", "Вторник"))
        self.pushButton_30.setText(_translate("MainWindow2", "Среда"))
        self.pushButton_31.setText(_translate("MainWindow2", "Четверг"))
        self.pushButton_32.setText(_translate("MainWindow2", "Пятница"))
        self.pushButton_33.setText(_translate("MainWindow2", "Суббота"))
        self.pushButton_34.setText(_translate("MainWindow2", "Воскресенье"))
        self.pushButton_35.setText(_translate("MainWindow2", "Сбросить изменения"))
        self.pushButton_36.setText(_translate("MainWindow2", "Применить изменения"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow2", "Временные изменения"))
