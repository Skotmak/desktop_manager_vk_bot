from http import client
import sys
import pymongo  # pip install pymongo[srv]
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from window_auth import *
import work  # from work import *
import sqlite3
import traceback
import sys

frirst_update_on_start = 0

#global authorization_status
#authorization_status = False


class Gui(QtWidgets.QMainWindow):
    client = sqlite3.connect('vk_bot_db.db')

    def __init__(self, parent=None):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Авторизация в \"Бот РУДН\"")
        self.centerOnScreen()
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint |
                            QtCore.Qt.WindowCloseButtonHint)
        self.authorization_status = False
        self.auth_win_status = True
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton.setAutoDefault(True)
        self.ui.pushButton_2.clicked.connect(self.register)

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if self.auth_win_status == True and event.type() == QtCore.QEvent.KeyPress:
            # (F12 16777275) (ENTER 16777220 or 16777221 - this for NUMPAD)
            if event.key() == 16777220 or event.key() == 16777221:
                self.login()
        return

    # центрируем окно
    def centerOnScreen(self):
        resolution = QtWidgets.QDesktopWidget().screenGeometry()
        self.move(int(resolution.width() // 2) - int(self.frameSize().width() // 2),
                  int(resolution.height() // 2) - int(self.frameSize().height()) // 2)

    def check_data(self):
        #global search_login
        login = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        cur1 = self.client.cursor()
        search_login = 0
        # Пытаемся найти ник в коллекции
        if login and passw:
            for search_login in cur1.execute("""SELECT login FROM users WHERE login = (?)""", (login,)):
                print('***', search_login, '***')
            cur1.close()  # ! можно и не закрывать после каждого запроса, хотя я хз. Можно потом с той же переменной открыть курсор
            if search_login:  # Если нашли значение
                return "value_exists"
            else:  # Если значения нет
                print(search_login)
                print(login)
                return "value_not_found"
        # Если данные не заполнены
        else:
            return "no_data_avaliable"

    def login(self):
        #global user_document
        #global user_name_db
        #global work
        #self.work = work.WorkGui()
        if self.authorization_status is False:
            # if authorization_status is False:
            result = self.check_data()
            if result == "value_exists":
                login = self.ui.lineEdit.text()
                passw = self.ui.lineEdit_2.text()
                cur1 = self.client.cursor()
                user_document = 0
                for user_document in cur1.execute("""SELECT password FROM users WHERE password = ?""", (passw,)):
                    print('***', user_document, '***')
                if user_document and passw == user_document[0]:
                    message_log = "Успешная авторизация!"
                    print('----- success login -----')
                    QtWidgets.QMessageBox.about(
                        self, "Уведомление", message_log)
                    self.authorization_status = True
                    self.close()
                    self.auth_win_status = False
                    work.show()
                    # self.work.show()
                    '''
                    if self.work is None: 
                        self.work = work.WorkGui()
                    else:
                        self.work.show()
                    '''

                    cur_login_name = self.client.cursor()
                    for user_name_db in cur_login_name.execute("""SELECT user_name FROM users WHERE password = ?""", (passw,)):
                        print('***', user_name_db, '***')
                    user_name = str(user_name_db[0])
                    work.ui.l_name.setText(user_name)
                    cur_login_name.close()
                    cur1.close()
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
        message_reg = "Регистрация временно не работает!"
        QtWidgets.QMessageBox.critical(self, "Ошибка", message_reg)
        ''' ! Регистрация не настроена ! '''
    '''
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
    '''

    '''
    def kek(self): удали как получится сделать функцию обновления после добавления студентов
        
        message_gui = "wow kek! "
        QtWidgets.QMessageBox.critical(self, "Ошибка", message_gui)
        #work = WorkGui()
        print("--- --- ---")
        print(work)  # Не видит больше этот класс
        print("--- --- ---")
        #work.WorkGui().download_tab(3, 1)
    '''


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Gui()
    window.show()

    # window.close()  # ! это закрывает первое окно с авторизацией
    work = work.WorkGui()
    # work.show()  # ! это открывает второе окно с рабочей областью
    sys.exit(app.exec_())
