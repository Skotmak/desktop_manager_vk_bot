import sys
import pymongo
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 170)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 581, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Логин"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.pushButton_2.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.pushButton.setText(_translate("MainWindow", "Войти"))
        

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(801, 690)
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 8, 791, 681))
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
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.l_name.setFont(font)
        self.l_name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.l_name.setAutoFillBackground(False)
        self.l_name.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.l_name.setTextFormat(QtCore.Qt.AutoText)
        self.l_name.setAlignment(QtCore.Qt.AlignCenter)
        self.l_name.setWordWrap(False)
        self.l_name.setObjectName("l_name")
        self.verticalLayout.addWidget(self.l_name)
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.b_thu_1 = QtWidgets.QPushButton(self.tab_1)
        self.b_thu_1.setGeometry(QtCore.QRect(170, 310, 170, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.b_thu_1.setFont(font)
        self.b_thu_1.setObjectName("b_thu_1")
        self.b_tue_0 = QtWidgets.QPushButton(self.tab_1)
        self.b_tue_0.setGeometry(QtCore.QRect(0, 110, 170, 100))
        self.b_tue_0.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.b_tue_0.setObjectName("b_tue_0")
        self.b_fri_1 = QtWidgets.QPushButton(self.tab_1)
        self.b_fri_1.setGeometry(QtCore.QRect(170, 410, 170, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.b_fri_1.setFont(font)
        self.b_fri_1.setObjectName("b_fri_1")
        self.b_fri_0 = QtWidgets.QPushButton(self.tab_1)
        self.b_fri_0.setGeometry(QtCore.QRect(0, 410, 170, 100))
        self.b_fri_0.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.b_fri_0.setObjectName("b_fri_0")
        self.b_sat_1 = QtWidgets.QPushButton(self.tab_1)
        self.b_sat_1.setGeometry(QtCore.QRect(170, 510, 170, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.b_sat_1.setFont(font)
        self.b_sat_1.setObjectName("b_sat_1")
        self.b_tue_1 = QtWidgets.QPushButton(self.tab_1)
        self.b_tue_1.setGeometry(QtCore.QRect(170, 110, 170, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.b_tue_1.setFont(font)
        self.b_tue_1.setObjectName("b_tue_1")
        self.b_wed_0 = QtWidgets.QPushButton(self.tab_1)
        self.b_wed_0.setGeometry(QtCore.QRect(0, 210, 170, 100))
        self.b_wed_0.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.b_wed_0.setObjectName("b_wed_0")
        self.b_mon_0 = QtWidgets.QPushButton(self.tab_1)
        self.b_mon_0.setGeometry(QtCore.QRect(0, 10, 170, 100))
        self.b_mon_0.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.b_mon_0.setObjectName("b_mon_0")
        self.b_wed_1 = QtWidgets.QPushButton(self.tab_1)
        self.b_wed_1.setGeometry(QtCore.QRect(170, 210, 170, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.b_wed_1.setFont(font)
        self.b_wed_1.setObjectName("b_wed_1")
        self.b_mon_1 = QtWidgets.QPushButton(self.tab_1)
        self.b_mon_1.setGeometry(QtCore.QRect(170, 10, 170, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.b_mon_1.setFont(font)
        self.b_mon_1.setObjectName("b_mon_1")
        self.b_sat_0 = QtWidgets.QPushButton(self.tab_1)
        self.b_sat_0.setGeometry(QtCore.QRect(0, 510, 170, 100))
        self.b_sat_0.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.b_sat_0.setObjectName("b_sat_0")
        self.b_thu_0 = QtWidgets.QPushButton(self.tab_1)
        self.b_thu_0.setGeometry(QtCore.QRect(0, 310, 170, 100))
        self.b_thu_0.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.b_thu_0.setObjectName("b_thu_0")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_1)
        self.plainTextEdit.setGeometry(QtCore.QRect(350, 80, 431, 451))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.clear_PTE = QtWidgets.QPushButton(self.tab_1)
        self.clear_PTE.setGeometry(QtCore.QRect(349, 575, 211, 35))
        self.clear_PTE.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.clear_PTE.setObjectName("clear_PTE")
        self.send_changes = QtWidgets.QPushButton(self.tab_1)
        self.send_changes.setGeometry(QtCore.QRect(560, 575, 220, 35))
        self.send_changes.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.send_changes.setObjectName("send_changes")
        self.label_5 = QtWidgets.QLabel(self.tab_1)
        self.label_5.setGeometry(QtCore.QRect(350, 10, 160, 30))
        self.label_5.setObjectName("label_5")
        self.l_day = QtWidgets.QLabel(self.tab_1)
        self.l_day.setGeometry(QtCore.QRect(510, 10, 271, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.l_day.setFont(font)
        self.l_day.setText("")
        self.l_day.setObjectName("l_day")
        self.label_6 = QtWidgets.QLabel(self.tab_1)
        self.label_6.setGeometry(QtCore.QRect(350, 540, 170, 30))
        self.label_6.setObjectName("label_6")
        self.l_status = QtWidgets.QLabel(self.tab_1)
        self.l_status.setGeometry(QtCore.QRect(520, 540, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.l_status.setFont(font)
        self.l_status.setText("")
        self.l_status.setObjectName("l_status")
        self.label_7 = QtWidgets.QLabel(self.tab_1)
        self.label_7.setGeometry(QtCore.QRect(350, 50, 241, 30))
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(self.tab_1)
        self.line.setGeometry(QtCore.QRect(350, 40, 431, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.PTE_temp = QtWidgets.QPlainTextEdit(self.tab_2)
        self.PTE_temp.setGeometry(QtCore.QRect(0, 300, 650, 201))
        self.PTE_temp.setObjectName("PTE_temp")
        self.DE_temp = QtWidgets.QDateEdit(self.tab_2)
        self.DE_temp.setGeometry(QtCore.QRect(0, 510, 771, 51))
        self.DE_temp.setObjectName("DE_temp")
        self.clear_PTE_temp = QtWidgets.QPushButton(self.tab_2)
        self.clear_PTE_temp.setGeometry(QtCore.QRect(660, 419, 120, 80))
        self.clear_PTE_temp.setObjectName("clear_PTE_temp")
        self.send_chages_temp = QtWidgets.QPushButton(self.tab_2)
        self.send_chages_temp.setGeometry(QtCore.QRect(660, 300, 120, 80))
        self.send_chages_temp.setObjectName("send_chages_temp")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(0, 570, 171, 20))
        self.label.setObjectName("label")
        self.l_status_2 = QtWidgets.QLabel(self.tab_2)
        self.l_status_2.setGeometry(QtCore.QRect(180, 570, 111, 20))
        self.l_status_2.setObjectName("l_status_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(0, 270, 251, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(0, 10, 250, 20))
        self.label_4.setObjectName("label_4")
        self.delete_temp_note = QtWidgets.QPushButton(self.tab_2)
        self.delete_temp_note.setGeometry(QtCore.QRect(660, 30, 120, 80))
        self.delete_temp_note.setObjectName("delete_temp_note")
        self.TW_temp = QtWidgets.QTableWidget(self.tab_2)
        self.TW_temp.setGeometry(QtCore.QRect(0, 30, 651, 241))
        self.TW_temp.setObjectName("TW_temp")
        self.TW_temp.setColumnCount(2)
        self.TW_temp.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.TW_temp.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TW_temp.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TW_temp.setHorizontalHeaderItem(1, item)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow2.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow2)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "Управление ботом РУДН"))
        self.l_name.setText(_translate("MainWindow2", "Привет, пользователь!"))
        self.b_thu_1.setText(_translate("MainWindow2", "Четверг\n"
"(нечётная неделя)"))
        self.b_tue_0.setText(_translate("MainWindow2", "Вторник\n"
"(чётная неделя)"))
        self.b_fri_1.setText(_translate("MainWindow2", "Пятница\n"
"(нечётная неделя)"))
        self.b_fri_0.setText(_translate("MainWindow2", "Пятница\n"
"(чётная неделя)"))
        self.b_sat_1.setText(_translate("MainWindow2", "Суббота\n"
"(нечётная неделя)"))
        self.b_tue_1.setText(_translate("MainWindow2", "Вторник\n"
"(нечётная неделя)"))
        self.b_wed_0.setText(_translate("MainWindow2", "Среда\n"
"(чётная неделя)"))
        self.b_mon_0.setText(_translate("MainWindow2", "Понедельник\n"
"(чётная неделя)"))
        self.b_wed_1.setText(_translate("MainWindow2", "Среда\n"
"(нечётная неделя)"))
        self.b_mon_1.setText(_translate("MainWindow2", "Понедельник\n"
"(нечётная неделя)"))
        self.b_sat_0.setText(_translate("MainWindow2", "Суббота\n"
"(чётная неделя)"))
        self.b_thu_0.setText(_translate("MainWindow2", "Четверг\n"
"(чётная неделя)"))
        self.clear_PTE.setText(_translate("MainWindow2", "Сбросить изменения"))
        self.send_changes.setText(_translate("MainWindow2", "Применить изменения"))
        self.label_5.setText(_translate("MainWindow2", "Выбранный день:"))
        self.label_6.setText(_translate("MainWindow2", "Статус изменения:"))
        self.label_7.setText(_translate("MainWindow2", "Введите текст сообщения:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow2", "Обычное расписание"))
        self.clear_PTE_temp.setText(_translate("MainWindow2", "Сбросить"))
        self.send_chages_temp.setText(_translate("MainWindow2", "Отправить"))
        self.label.setText(_translate("MainWindow2", "Статус изменения:"))
        self.l_status_2.setText(_translate("MainWindow2", " "))
        self.label_3.setText(_translate("MainWindow2", "Введите текст сообщения:"))
        self.label_4.setText(_translate("MainWindow2", "Запланированные события:"))
        self.delete_temp_note.setText(_translate("MainWindow2", "Удалить"))
        item = self.TW_temp.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow2", "Дата"))
        item = self.TW_temp.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow2", "Текст"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow2", "Временные изменения"))



class Gui(QtWidgets.QMainWindow):
    client = pymongo.MongoClient("mongodb+srv://user:2467531max@cluster0.najw2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Авторизация в \"Бот РУДН\"")
        self.centerOnScreen()
        self.authorization_status = False
        self.auth_win_status = True
        #self.client = pymongo.MongoClient("mongodb+srv://user:2467531max@cluster0.najw2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton.setAutoDefault(True)
        self.ui.pushButton_2.clicked.connect(self.register)

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if self.auth_win_status == True and event.type() == QtCore.QEvent.KeyPress:
            if event.key() == 16777220 or event.key() == 16777221: # (F12 16777275) (ENTER 16777220 or 16777221 - this for NUMPAD)
                self.login()    
        return

    # центрируем окно
    def centerOnScreen(self):
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move(int(resolution.width() // 2) - int(self.frameSize().width() // 2), int(resolution.height() // 2) - int(self.frameSize().height()) // 2)


    def check_data(self):
        login = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        # Пытаемся найти ник в коллекции
        if login and passw:
            search_login = self.client.admindb.users.find_one({"login": login})
            if search_login:  # Если нашли значение
                return "value_exists"
            else:  # Если значения нет
                return "value_not_found"
        # Если данные не заполнены
        else:
            return "no_data_avaliable"


    def login(self):
        if self.authorization_status is False:
            result = self.check_data()  
            if result == "value_exists":
                login = self.ui.lineEdit.text()
                passw = self.ui.lineEdit_2.text()
                user_document = self.client.admindb.users.find_one({"login": login})
                if user_document and passw == user_document["password"]:
                    message = "Успешная авторизация!"
                    QtWidgets.QMessageBox.about(self, "Уведомление", message)
                    self.authorization_status = True
                    window.close()
                    self.auth_win_status = False
                    work.show()
                    if login == "max":
                        work.ui.l_name.setText("Привет, Макс!")
                    elif login == "maftuna":
                        work.ui.l_name.setText("Привет, Мафтуна!")
                    elif login == "sergo":
                        work.ui.l_name.setText("Привет, Серега!")
                else:
                    message = "Данные введены некорректно!"
                    QtWidgets.QMessageBox.about(self, "Ошибка", message)
            elif result == "value_not_found":
                message = "Такой пользователь не зарегистрирован!"
                QtWidgets.QMessageBox.about(self, "Уведомление", message)
            elif result == "no_data_avaliable":
                message = "Необходимо ввести данные!"
                QtWidgets.QMessageBox.about(self, "Ошибка", message)
        else:
            message = "Вы уже авторизованы!"
            QtWidgets.QMessageBox.about(self, "Ошибка", message)      


    def register(self):
        if self.authorization_status is False:
            result = self.check_data()
            if result == "value_exists":
                message = "Такой логин уже используется!"
                QtWidgets.QMessageBox.about(self, "Ошибка", message)
            elif result == "value_not_found":
                data = {
                    'nickname': self.ui.lineEdit.text(),
                    'password': self.ui.lineEdit_2.text()  # Пароли не хешируются
                }
                self.client.testdb.users.insert_one(data)
                message = "Регистрация прошла успешно!"
                QtWidgets.QMessageBox.about(self, "Уведомление", message)
                self.authorization_status = True
            elif result == "no_data_avaliable":
                message = "Необходимо ввести данные!"
                QtWidgets.QMessageBox.about(self, "Ошибка", message)
        else:
            message = "Вы уже авторизованы!"
            QtWidgets.QMessageBox.about(self, "Ошибка", message)

class WorkGui(Gui):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)
        self.centerOnScreen()
        self.db = Gui.client.timetable
        self.coll = self.db.ussual
        self.current_id = 0

        self.ui.plainTextEdit.textChanged.connect(self.get_focus)

        ''' 0 - чётная неделя   1 - не чётная неделя '''
        self.ui.b_mon_0.clicked.connect(self.get_monday_0)
        self.ui.b_tue_0.clicked.connect(self.get_tuesday_0)
        self.ui.b_wed_0.clicked.connect(self.get_wednesday_0)
        self.ui.b_thu_0.clicked.connect(self.get_thursday_0)
        self.ui.b_fri_0.clicked.connect(self.get_friday_0)
        self.ui.b_sat_0.clicked.connect(self.get_saturday_0)

        self.ui.b_mon_1.clicked.connect(self.get_monday_1)
        self.ui.b_tue_1.clicked.connect(self.get_tuesday_1)
        self.ui.b_wed_1.clicked.connect(self.get_wednesday_1)
        self.ui.b_thu_1.clicked.connect(self.get_thursday_1)
        self.ui.b_fri_1.clicked.connect(self.get_friday_1)
        self.ui.b_sat_1.clicked.connect(self.get_saturday_1)

        self.ui.clear_PTE.clicked.connect(self.clear_plainTE)
        self.ui.send_changes.clicked.connect(self.send_changes_to_db)


    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if self.auth_win_status == True and event.type() == QtCore.QEvent.KeyPress:
            if event.key() == 16777220 or event.key() == 16777221: # (F12 16777275) (ENTER 16777220 or 16777221 - this for NUMPAD)
                self.auth_win_status == False    
        return

    def get_focus(self):
        self.ui.l_status.setText('Редактируется')
        return
        
    # 0 - чётная неделя
    def get_monday_0(self):
        res = self.coll.find_one({"_id": "10"})
        self.current_id = 10
        self.ui.plainTextEdit.setPlainText(res["shedule"])
        self.ui.l_day.setText('Понедельник (чётная неделя)')
        self.ui.l_status.setText('Неизменено')
        return
    
    def get_tuesday_0(self):
        res = self.coll.find_one({"_id": "20"})
        self.current_id = 20
        self.ui.plainTextEdit.setPlainText(res["shedule"])
        self.ui.l_day.setText('Вторник (чётная неделя)')
        self.ui.l_status.setText('Неизменено')
        return

    def get_wednesday_0(self):
        res = self.coll.find_one({"_id": "30"})
        self.current_id = 30
        self.ui.plainTextEdit.setPlainText(res["shedule"])
        self.ui.l_day.setText('Среда (чётная неделя)')
        self.ui.l_status.setText('Неизменено')
        return

    def get_thursday_0(self):
        res = self.coll.find_one({"_id": "40"})
        self.current_id = 40
        self.ui.plainTextEdit.setPlainText(res["shedule"])
        self.ui.l_day.setText('Четверг (чётная неделя)')
        self.ui.l_status.setText('Неизменено')
        return

    def get_friday_0(self):
        res = self.coll.find_one({"_id": "50"})
        self.current_id = 50
        self.ui.plainTextEdit.setPlainText(res["shedule"])
        self.ui.l_day.setText('Пятница (чётная неделя)')
        self.ui.l_status.setText('Неизменено')
        return

    def get_saturday_0(self):
        res = self.coll.find_one({"_id": "60"})
        self.current_id = 60
        self.ui.plainTextEdit.setPlainText(res["shedule"])
        self.ui.l_day.setText('Суббота (чётная неделя)')
        self.ui.l_status.setText('Неизменено')
        return

    # 1 - не чётная неделя
    def get_monday_1(self):
        res = self.coll.find_one({"_id": "11"})
        self.current_id = 11
        self.ui.plainTextEdit.setPlainText(res["shedule"])
        self.ui.l_day.setText('Понедельник (нечётная неделя)')
        self.ui.l_status.setText('Неизменено')
        return
    
    def get_tuesday_1(self):
        res = self.coll.find_one({"_id": "21"})
        self.current_id = 21
        self.ui.plainTextEdit.setPlainText(res["shedule"])
        self.ui.l_day.setText('Вторник (нечётная неделя)')
        self.ui.l_status.setText('Неизменено')
        return

    def get_wednesday_1(self):
        res = self.coll.find_one({"_id": "31"})
        self.current_id = 31
        self.ui.plainTextEdit.setPlainText(res["shedule"])
        self.ui.l_day.setText('Среда (нечётная неделя)')
        self.ui.l_status.setText('Неизменено')
        return

    def get_thursday_1(self):
        res = self.coll.find_one({"_id": "41"})
        self.current_id = 41
        self.ui.plainTextEdit.setPlainText(res["shedule"])
        self.ui.l_day.setText('Четверг (нечётная неделя)')
        self.ui.l_status.setText('Неизменено')
        return

    def get_friday_1(self):
        res = self.coll.find_one({"_id": "51"})
        self.current_id = 51
        self.ui.plainTextEdit.setPlainText(res["shedule"])
        self.ui.l_day.setText('Пятница (нечётная неделя)')
        self.ui.l_status.setText('Неизменено')
        return

    def get_saturday_1(self):
        res = self.coll.find_one({"_id": "61"})
        self.current_id = 61
        self.ui.plainTextEdit.setPlainText(res["shedule"])
        self.ui.l_day.setText('Суббота (нечётная неделя)')
        self.ui.l_status.setText('Неизменено')
        return

    def send_changes_to_db(self):
        if self.current_id != 0:
            self.text = self.ui.plainTextEdit.toPlainText()
            current = {"_id": str(self.current_id)}
            new_data = {"$set": {"shedule": self.text}}
            self.coll.update_one(current, new_data)
            self.ui.l_status.setText('Изменения приняты!')
            return
        else:
            self.ui.l_status.setText('')
            return

    def clear_plainTE(self):
        self.ui.plainTextEdit.setPlainText('')
        self.ui.l_day.setText('')
        self.current_id = 0
        self.ui.l_status.setText('')
        return



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Gui()
    window.show()
    work = WorkGui()
    sys.exit(app.exec_())