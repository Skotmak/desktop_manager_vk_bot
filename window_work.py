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
        MainWindow2.resize(840, 800)
        MainWindow2.setMinimumSize(QtCore.QSize(840, 800))
        MainWindow2.setMaximumSize(QtCore.QSize(840, 800))
        MainWindow2.setStyleSheet("background-color: rgb(245, 247, 250);\n"
"opacity: 1;")
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setStyleSheet("background: #F5F7FA;\n"
"opacity: 1;")
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 80, 820, 711))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.b_thu_1 = QtWidgets.QPushButton(self.tab_1)
        self.b_thu_1.setGeometry(QtCore.QRect(190, 340, 170, 100))
        font = QtGui.QFont()
        self.b_thu_1.setFont(font)
        self.b_thu_1.setStyleSheet("QPushButton{\n"
"background: #FFFFFF ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"border: 1px solid #e5e5e5;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #e8e8e8;\n"
"}")
        self.b_thu_1.setObjectName("b_thu_1")
        self.b_tue_0 = QtWidgets.QPushButton(self.tab_1)
        self.b_tue_0.setGeometry(QtCore.QRect(10, 120, 170, 100))
        font = QtGui.QFont()
        self.b_tue_0.setFont(font)
        self.b_tue_0.setStyleSheet("QPushButton{\n"
"background: #FFFFFF ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"border: 1px solid #e5e5e5;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #e8e8e8;\n"
"}")
        self.b_tue_0.setObjectName("b_tue_0")
        self.b_fri_1 = QtWidgets.QPushButton(self.tab_1)
        self.b_fri_1.setGeometry(QtCore.QRect(190, 450, 170, 100))
        font = QtGui.QFont()
        self.b_fri_1.setFont(font)
        self.b_fri_1.setStyleSheet("QPushButton{\n"
"background: #FFFFFF ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"border: 1px solid #e5e5e5;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #e8e8e8;\n"
"}")
        self.b_fri_1.setObjectName("b_fri_1")
        self.b_fri_0 = QtWidgets.QPushButton(self.tab_1)
        self.b_fri_0.setGeometry(QtCore.QRect(10, 450, 170, 100))
        font = QtGui.QFont()
        self.b_fri_0.setFont(font)
        self.b_fri_0.setStyleSheet("QPushButton{\n"
"background: #FFFFFF ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"border: 1px solid #e5e5e5;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #e8e8e8;\n"
"}")
        self.b_fri_0.setObjectName("b_fri_0")
        self.b_sat_1 = QtWidgets.QPushButton(self.tab_1)
        self.b_sat_1.setGeometry(QtCore.QRect(190, 560, 170, 100))
        font = QtGui.QFont()
        self.b_sat_1.setFont(font)
        self.b_sat_1.setStyleSheet("QPushButton{\n"
"background: #FFFFFF ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"border: 1px solid #e5e5e5;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #e8e8e8;\n"
"}")
        self.b_sat_1.setObjectName("b_sat_1")
        self.b_tue_1 = QtWidgets.QPushButton(self.tab_1)
        self.b_tue_1.setGeometry(QtCore.QRect(190, 120, 170, 100))
        font = QtGui.QFont()
        self.b_tue_1.setFont(font)
        self.b_tue_1.setStyleSheet("QPushButton{\n"
"background: #FFFFFF ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"border: 1px solid #e5e5e5;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #e8e8e8;\n"
"}")
        self.b_tue_1.setObjectName("b_tue_1")
        self.b_wed_0 = QtWidgets.QPushButton(self.tab_1)
        self.b_wed_0.setGeometry(QtCore.QRect(10, 230, 170, 100))
        font = QtGui.QFont()
        self.b_wed_0.setFont(font)
        self.b_wed_0.setStyleSheet("QPushButton{\n"
"background: #FFFFFF ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"border: 1px solid #e5e5e5;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #e8e8e8;\n"
"}")
        self.b_wed_0.setObjectName("b_wed_0")
        self.b_mon_0 = QtWidgets.QPushButton(self.tab_1)
        self.b_mon_0.setGeometry(QtCore.QRect(10, 10, 170, 100))
        font = QtGui.QFont()
        self.b_mon_0.setFont(font)
        self.b_mon_0.setStyleSheet("QPushButton{\n"
"background: #FFFFFF ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"border: 1px solid #e5e5e5;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #e8e8e8;\n"
"}")
        self.b_mon_0.setObjectName("b_mon_0")
        self.b_wed_1 = QtWidgets.QPushButton(self.tab_1)
        self.b_wed_1.setGeometry(QtCore.QRect(190, 230, 170, 100))
        font = QtGui.QFont()
        self.b_wed_1.setFont(font)
        self.b_wed_1.setStyleSheet("QPushButton{\n"
"background: #FFFFFF ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"border: 1px solid #e5e5e5;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #e8e8e8;\n"
"}")
        self.b_wed_1.setObjectName("b_wed_1")
        self.b_mon_1 = QtWidgets.QPushButton(self.tab_1)
        self.b_mon_1.setGeometry(QtCore.QRect(190, 10, 170, 100))
        font = QtGui.QFont()
        self.b_mon_1.setFont(font)
        self.b_mon_1.setStyleSheet("QPushButton{\n"
"background: #FFFFFF ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"border: 1px solid #e5e5e5;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #e8e8e8;\n"
"}")
        self.b_mon_1.setObjectName("b_mon_1")
        self.b_sat_0 = QtWidgets.QPushButton(self.tab_1)
        self.b_sat_0.setGeometry(QtCore.QRect(10, 560, 170, 100))
        font = QtGui.QFont()
        self.b_sat_0.setFont(font)
        self.b_sat_0.setStyleSheet("QPushButton{\n"
"background: #FFFFFF ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"border: 1px solid #e5e5e5;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #e8e8e8;\n"
"}")
        self.b_sat_0.setObjectName("b_sat_0")
        self.b_thu_0 = QtWidgets.QPushButton(self.tab_1)
        self.b_thu_0.setGeometry(QtCore.QRect(10, 340, 170, 100))
        font = QtGui.QFont()
        self.b_thu_0.setFont(font)
        self.b_thu_0.setStyleSheet("QPushButton{\n"
"background: #FFFFFF ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"border: 1px solid #e5e5e5;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #e8e8e8;\n"
"}")
        self.b_thu_0.setObjectName("b_thu_0")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_1)
        self.plainTextEdit.setGeometry(QtCore.QRect(370, 80, 431, 501))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.clear_PTE = QtWidgets.QPushButton(self.tab_1)
        self.clear_PTE.setGeometry(QtCore.QRect(369, 625, 211, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clear_PTE.setFont(font)
        self.clear_PTE.setStyleSheet("QPushButton{\n"
"background: #FFFFFF ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"color: #0079C2;\n"
"text-transform: uppercase;\n"
"font-weight: medium; \n"
"border: 1px solid #e5e5e5;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #e8e8e8;\n"
"}")
        self.clear_PTE.setObjectName("clear_PTE")
        self.send_changes = QtWidgets.QPushButton(self.tab_1)
        self.send_changes.setGeometry(QtCore.QRect(590, 625, 220, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.send_changes.setFont(font)
        self.send_changes.setStyleSheet("QPushButton{\n"
"background: #03A9F4 ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"color: #FFFFFF;\n"
"text-transform: uppercase;\n"
"font-weight: medium; \n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #0079C2;\n"
"}")
        self.send_changes.setObjectName("send_changes")
        self.label_5 = QtWidgets.QLabel(self.tab_1)
        self.label_5.setGeometry(QtCore.QRect(370, 10, 160, 30))
        font = QtGui.QFont()
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"font-weight: medium; ")
        self.label_5.setObjectName("label_5")
        self.l_day = QtWidgets.QLabel(self.tab_1)
        self.l_day.setGeometry(QtCore.QRect(530, 10, 271, 30))
        font = QtGui.QFont()
        self.l_day.setFont(font)
        self.l_day.setStyleSheet("letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"font-weight: medium; ")
        self.l_day.setText("")
        self.l_day.setObjectName("l_day")
        self.label_6 = QtWidgets.QLabel(self.tab_1)
        self.label_6.setGeometry(QtCore.QRect(370, 590, 170, 30))
        font = QtGui.QFont()
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"font-weight: medium; ")
        self.label_6.setObjectName("label_6")
        self.l_status = QtWidgets.QLabel(self.tab_1)
        self.l_status.setGeometry(QtCore.QRect(540, 590, 250, 30))
        font = QtGui.QFont()
        self.l_status.setFont(font)
        self.l_status.setStyleSheet("letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"font-weight: medium; ")
        self.l_status.setText("")
        self.l_status.setObjectName("l_status")
        self.label_7 = QtWidgets.QLabel(self.tab_1)
        self.label_7.setGeometry(QtCore.QRect(370, 50, 241, 30))
        font = QtGui.QFont()
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"font-weight: medium; ")
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(self.tab_1)
        self.line.setGeometry(QtCore.QRect(370, 40, 431, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.PTE_temp = QtWidgets.QPlainTextEdit(self.tab_2)
        self.PTE_temp.setGeometry(QtCore.QRect(10, 310, 650, 211))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PTE_temp.setFont(font)
        self.PTE_temp.setStyleSheet("")
        self.PTE_temp.setObjectName("PTE_temp")
        self.DE_temp = QtWidgets.QDateEdit(self.tab_2)
        self.DE_temp.setGeometry(QtCore.QRect(10, 570, 771, 51))
        font = QtGui.QFont()
        self.DE_temp.setFont(font)
        self.DE_temp.setStyleSheet("letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"font-weight: medium; ")
        self.DE_temp.setObjectName("DE_temp")
        self.clear_PTE_temp = QtWidgets.QPushButton(self.tab_2)
        self.clear_PTE_temp.setGeometry(QtCore.QRect(670, 400, 120, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clear_PTE_temp.setFont(font)
        self.clear_PTE_temp.setStyleSheet("QPushButton{\n"
"background: #FFFFFF ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"color: #0079C2;\n"
"text-transform: uppercase;\n"
"font-weight: medium; \n"
"border: 1px solid #e5e5e5;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #e8e8e8;\n"
"}")
        self.clear_PTE_temp.setObjectName("clear_PTE_temp")
        self.send_chages_temp = QtWidgets.QPushButton(self.tab_2)
        self.send_chages_temp.setGeometry(QtCore.QRect(670, 310, 120, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.send_chages_temp.setFont(font)
        self.send_chages_temp.setStyleSheet("QPushButton{\n"
"background: #03A9F4 ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"color: #FFFFFF;\n"
"text-transform: uppercase;\n"
"font-weight: medium; \n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #0079C2;\n"
"}")
        self.send_chages_temp.setObjectName("send_chages_temp")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(10, 630, 171, 20))
        font = QtGui.QFont()
        self.label.setFont(font)
        self.label.setStyleSheet("letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"font-weight: medium; ")
        self.label.setObjectName("label")
        self.l_status_2 = QtWidgets.QLabel(self.tab_2)
        self.l_status_2.setGeometry(QtCore.QRect(180, 630, 250, 21))
        font = QtGui.QFont()
        self.l_status_2.setFont(font)
        self.l_status_2.setStyleSheet("letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"font-weight: medium; ")
        self.l_status_2.setText("")
        self.l_status_2.setObjectName("l_status_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 280, 250, 30))
        font = QtGui.QFont()
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"font-weight: medium; ")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(10, 5, 250, 20))
        font = QtGui.QFont()
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"font-weight: medium; ")
        self.label_4.setObjectName("label_4")
        self.delete_temp_note = QtWidgets.QPushButton(self.tab_2)
        self.delete_temp_note.setGeometry(QtCore.QRect(670, 30, 120, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delete_temp_note.setFont(font)
        self.delete_temp_note.setStyleSheet("QPushButton{\n"
"background: #03A9F4 ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"color: #FFFFFF;\n"
"text-transform: uppercase;\n"
"font-weight: medium; \n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #0079C2;\n"
"}")
        self.delete_temp_note.setObjectName("delete_temp_note")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(10, 530, 251, 31))
        font = QtGui.QFont()
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"font-weight: medium; ")
        self.label_8.setObjectName("label_8")
        self.TW_temp = QtWidgets.QTreeWidget(self.tab_2)
        self.TW_temp.setGeometry(QtCore.QRect(10, 30, 651, 241))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.TW_temp.setFont(font)
        self.TW_temp.setStyleSheet("")
        self.TW_temp.setObjectName("TW_temp")
        self.TW_temp.header().setSortIndicatorShown(True)
        self.refresh_btn_tab2 = QtWidgets.QPushButton(self.tab_2)
        self.refresh_btn_tab2.setGeometry(QtCore.QRect(670, 120, 120, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.refresh_btn_tab2.setFont(font)
        self.refresh_btn_tab2.setStyleSheet("QPushButton{\n"
"background: #FFFFFF ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"color: #0079C2;\n"
"text-transform: uppercase;\n"
"font-weight: medium; \n"
"border: 1px solid #e5e5e5;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #e8e8e8;\n"
"}")
        self.refresh_btn_tab2.setObjectName("refresh_btn_tab2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.stud_tab = QtWidgets.QTreeWidget(self.tab)
        self.stud_tab.setGeometry(QtCore.QRect(0, 0, 641, 671))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.stud_tab.setFont(font)
        self.stud_tab.setStyleSheet("")
        self.stud_tab.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.stud_tab.setAnimated(False)
        self.stud_tab.setColumnCount(5)
        self.stud_tab.setObjectName("stud_tab")
        self.stud_tab.header().setCascadingSectionResizes(False)
        self.stud_tab.header().setHighlightSections(False)
        self.stud_tab.header().setSortIndicatorShown(False)
        self.stud_tab.header().setStretchLastSection(True)
        self.add_stud_btn = QtWidgets.QPushButton(self.tab)
        self.add_stud_btn.setGeometry(QtCore.QRect(649, 20, 141, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_stud_btn.setFont(font)
        self.add_stud_btn.setStyleSheet("QPushButton{\n"
"background: #03A9F4 ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"color: #FFFFFF;\n"
"text-transform: uppercase;\n"
"font-weight: medium; \n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #0079C2;\n"
"}")
        self.add_stud_btn.setObjectName("add_stud_btn")
        self.delete_stud_btn = QtWidgets.QPushButton(self.tab)
        self.delete_stud_btn.setGeometry(QtCore.QRect(649, 110, 141, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.delete_stud_btn.setFont(font)
        self.delete_stud_btn.setStyleSheet("QPushButton{\n"
"background: #03A9F4 ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"color: #FFFFFF;\n"
"text-transform: uppercase;\n"
"font-weight: medium; \n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #0079C2;\n"
"}")
        self.delete_stud_btn.setObjectName("delete_stud_btn")
        self.refresh_btn_tab3 = QtWidgets.QPushButton(self.tab)
        self.refresh_btn_tab3.setGeometry(QtCore.QRect(649, 200, 141, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.refresh_btn_tab3.setFont(font)
        self.refresh_btn_tab3.setStyleSheet("QPushButton{\n"
"background: #03A9F4 ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"color: #FFFFFF;\n"
"text-transform: uppercase;\n"
"font-weight: medium; \n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #0079C2;\n"
"}")
        self.refresh_btn_tab3.setObjectName("refresh_btn_tab3")
        self.edit_stud_btn = QtWidgets.QPushButton(self.tab)
        self.edit_stud_btn.setGeometry(QtCore.QRect(649, 290, 141, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.edit_stud_btn.setFont(font)
        self.edit_stud_btn.setStyleSheet("QPushButton{\n"
"background: #03A9F4 ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"color: #FFFFFF;\n"
"text-transform: uppercase;\n"
"font-weight: medium; \n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #0079C2;\n"
"}")
        self.edit_stud_btn.setObjectName("edit_stud_btn")
        self.open_stud_marks = QtWidgets.QPushButton(self.tab)
        self.open_stud_marks.setGeometry(QtCore.QRect(649, 380, 141, 80))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.open_stud_marks.setFont(font)
        self.open_stud_marks.setStyleSheet("background: #0079C2 ;\n"
"border-radius: 4px;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"color: #FFFFFF;\n"
"text-transform: uppercase;\n"
"opacity: 1;\n"
"font-weight: medium; ")
        self.open_stud_marks.setObjectName("open_stud_marks")
        self.tabWidget.addTab(self.tab, "")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 842, 60))
        self.frame.setStyleSheet("background: #0079C2 ;\n"
"border: 1px solid #e5e5e5;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(-1, -1, 170, 60))
        font = QtGui.QFont()
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #f10909, stop:1 #0079C2);\n"
"letter-spacing: 0px;\n"
"text-transform: uppercase;\n"
"font-weight: medium; \n"
"border: 1px solid rgb(255, 255, 255);\n"
"color: white;\n"
"border-style: solid;\n"
"border-width: 1px; \n"
"border-color: #0079C2;")
        self.label_2.setLineWidth(0)
        self.label_2.setObjectName("label_2")
        self.group_comboBox = QtWidgets.QComboBox(self.frame)
        self.group_comboBox.setGeometry(QtCore.QRect(180, 15, 241, 31))
        font = QtGui.QFont()
        self.group_comboBox.setFont(font)
        self.group_comboBox.setStyleSheet("letter-spacing: 0px;\n"
"background-color: rgb(255, 255, 255);\n"
"text-transform: uppercase;\n"
"border-radius: 0px;\n"
"color: black;\n"
"border-style: solid;\n"
"border-width: 1px; \n"
"border-color: black;")
        self.group_comboBox.setFrame(True)
        self.group_comboBox.setObjectName("group_comboBox")
        self.group_comboBox.addItem("")
        self.goups_setting_btn = QtWidgets.QPushButton(self.frame)
        self.goups_setting_btn.setGeometry(QtCore.QRect(430, 10, 40, 40))
        self.goups_setting_btn.setStyleSheet("QPushButton{\n"
"background: #FFFFFF ;\n"
"border-radius: 4px;\n"
"opacity: 1;\n"
"text-align: center;\n"
"letter-spacing: 0px;\n"
"color: #0079C2;\n"
"text-transform: uppercase;\n"
"font-weight: medium; \n"
"border: 1px solid #e5e5e5;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #e8e8e8;\n"
"}")
        self.goups_setting_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("cog.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.goups_setting_btn.setIcon(icon)
        self.goups_setting_btn.setIconSize(QtCore.QSize(20, 20))
        self.goups_setting_btn.setFlat(True)
        self.goups_setting_btn.setObjectName("goups_setting_btn")
        self.l_name = QtWidgets.QLabel(self.frame)
        self.l_name.setEnabled(True)
        self.l_name.setGeometry(QtCore.QRect(610, 10, 141, 39))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_name.sizePolicy().hasHeightForWidth())
        self.l_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.l_name.setFont(font)
        self.l_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.l_name.setAutoFillBackground(False)
        self.l_name.setStyleSheet("letter-spacing: 0px;\n"
"font-weight: medium; \n"
"border: 1px solid rgb(255, 255, 255);\n"
"text-align: right;\n"
"color: white;\n"
"border-style: solid;\n"
"border-width: 1px; \n"
"border-color: #0079C2;")
        self.l_name.setTextFormat(QtCore.Qt.AutoText)
        self.l_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l_name.setWordWrap(False)
        self.l_name.setObjectName("l_name")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(750, 10, 31, 39))
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setStyleSheet("border: 1px solid rgb(255, 255, 255);\n"
"color: white;\n"
"border-style: solid;\n"
"border-width: 1px; \n"
"border-color: #0079C2;")
        self.label_9.setObjectName("label_9")
        self.exit_btn = QtWidgets.QPushButton(self.frame)
        self.exit_btn.setGeometry(QtCore.QRect(790, 10, 40, 40))
        self.exit_btn.setStyleSheet("QPushButton{\n"
"background: #ff4b4b ; \n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background: #ff0000;\n"
"border-radius: 10px;\n"
"}")
        self.exit_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("logout.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn.setIcon(icon1)
        self.exit_btn.setIconSize(QtCore.QSize(20, 20))
        self.exit_btn.setFlat(True)
        self.exit_btn.setObjectName("exit_btn")
        MainWindow2.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow2)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "???????????????????? ??????????????????"))
        self.b_thu_1.setText(_translate("MainWindow2", "??????????????\n"
"(???????????????? ????????????)"))
        self.b_tue_0.setText(_translate("MainWindow2", "??????????????\n"
"(???????????? ????????????)"))
        self.b_fri_1.setText(_translate("MainWindow2", "??????????????\n"
"(???????????????? ????????????)"))
        self.b_fri_0.setText(_translate("MainWindow2", "??????????????\n"
"(???????????? ????????????)"))
        self.b_sat_1.setText(_translate("MainWindow2", "??????????????\n"
"(???????????????? ????????????)"))
        self.b_tue_1.setText(_translate("MainWindow2", "??????????????\n"
"(???????????????? ????????????)"))
        self.b_wed_0.setText(_translate("MainWindow2", "??????????\n"
"(???????????? ????????????)"))
        self.b_mon_0.setText(_translate("MainWindow2", "??????????????????????\n"
"(???????????? ????????????)"))
        self.b_wed_1.setText(_translate("MainWindow2", "??????????\n"
"(???????????????? ????????????)"))
        self.b_mon_1.setText(_translate("MainWindow2", "??????????????????????\n"
"(???????????????? ????????????)"))
        self.b_sat_0.setText(_translate("MainWindow2", "??????????????\n"
"(???????????? ????????????)"))
        self.b_thu_0.setText(_translate("MainWindow2", "??????????????\n"
"(???????????? ????????????)"))
        self.clear_PTE.setText(_translate("MainWindow2", "???????????????? ??????????????????"))
        self.send_changes.setText(_translate("MainWindow2", "?????????????????? ??????????????????"))
        self.label_5.setText(_translate("MainWindow2", "?????????????????? ????????:"))
        self.label_6.setText(_translate("MainWindow2", "???????????? ??????????????????:"))
        self.label_7.setText(_translate("MainWindow2", "?????????????? ?????????? ??????????????????:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow2", "?????????????? ????????????????????"))
        self.clear_PTE_temp.setText(_translate("MainWindow2", "????????????????\n"
"??????????\n"
"??????????????????"))
        self.send_chages_temp.setText(_translate("MainWindow2", "??????????????????\n"
"??????????\n"
"??????????????????"))
        self.label.setText(_translate("MainWindow2", "???????????? ??????????????????:"))
        self.label_3.setText(_translate("MainWindow2", "?????????????? ?????????? ??????????????????:"))
        self.label_4.setText(_translate("MainWindow2", "?????????????????????????????? ??????????????:"))
        self.delete_temp_note.setText(_translate("MainWindow2", "??????????????\n"
"????????????"))
        self.label_8.setText(_translate("MainWindow2", "???????????????? ???????? ??????????????????:"))
        self.TW_temp.headerItem().setText(0, _translate("MainWindow2", "???????? ??????????????"))
        self.TW_temp.headerItem().setText(1, _translate("MainWindow2", "?????????? ??????????????"))
        self.refresh_btn_tab2.setText(_translate("MainWindow2", "????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow2", "?????????????????? ??????????????????"))
        self.stud_tab.setSortingEnabled(False)
        self.stud_tab.headerItem().setText(0, _translate("MainWindow2", "???"))
        self.stud_tab.headerItem().setText(1, _translate("MainWindow2", "??????????????"))
        self.stud_tab.headerItem().setText(2, _translate("MainWindow2", "??????"))
        self.stud_tab.headerItem().setText(3, _translate("MainWindow2", "????????????????"))
        self.stud_tab.headerItem().setText(4, _translate("MainWindow2", "?????????? ??????????????????????????"))
        self.add_stud_btn.setText(_translate("MainWindow2", "????????????????\n"
"????????????????"))
        self.delete_stud_btn.setText(_translate("MainWindow2", "??????????????\n"
"????????????????"))
        self.refresh_btn_tab3.setText(_translate("MainWindow2", "????????????????"))
        self.edit_stud_btn.setText(_translate("MainWindow2", "??????????????????\n"
"????????????"))
        self.open_stud_marks.setText(_translate("MainWindow2", "??????????\n"
"????????????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow2", "???????????? ??????????????????"))
        self.label_2.setText(_translate("MainWindow2", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">KMV Development</span></p></body></html>"))
        self.group_comboBox.setCurrentText(_translate("MainWindow2", "???????????????? ????????????"))
        self.group_comboBox.setItemText(0, _translate("MainWindow2", "???????????????? ????????????"))
        self.goups_setting_btn.setWhatsThis(_translate("MainWindow2", "?????????? ???? ?????????????? ????????????"))
        self.l_name.setText(_translate("MainWindow2", "????????????????????????"))
        self.label_9.setText(_translate("MainWindow2", "<img src=\'account.svg\' />"))
        self.exit_btn.setWhatsThis(_translate("MainWindow2", "?????????? ???? ?????????????? ????????????"))
