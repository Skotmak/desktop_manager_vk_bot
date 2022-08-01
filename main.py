from http import client
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from window_auth import *
import work
import sqlite3
import sys

from socket import *
from getpass import getpass
from cryptography.fernet import Fernet
import base64

frirst_update_on_start = 0
login_var = 1
# user_role_and_group_id = 2


class Client:
    def __init__(self, ip, port):
        self.cli = socket(AF_INET, SOCK_STREAM)
        self.cli.connect(
            (ip, port)
        )

        symbols = {
            '0': 'Q', '1': 'W', '2': 'E', '3': 'R', '4': 'T', '5': 'Y', '6': 'U', '7': 'I', '8': 'O', '9': 'P',
        }
        p = self.cli.getsockname()[0].replace('.', '')
        i = 0
        key = ''
        while len(key) != 32:
            key = f'{key}{symbols[p[i]]}'
            i += 1
            if i == len(p):
                i = 0
        key = key.encode()
        key = base64.urlsafe_b64encode(key)
        self.f = Fernet(key)

    def sender(self, text):
        text = text.encode()
        text = self.f.encrypt(text)
        try:
            self.cli.send(text)
        except Exception as e:
            pass

    def get_msg(self):
        data = self.cli.recv(1024)
        data = self.f.decrypt(data)
        msg = data.decode()
        return msg

    def auth(self):
        server_answer = self.get_msg()

        if server_answer == 'Type you password.':
            self.sender('root')

            answer = self.get_msg()

            if answer == 'Access is allowed!':
                return 1

            if answer == 'Access denied!':
                return 0

        elif server_answer == 'Access is allowed!':
            return 1

        elif server_answer == 'Access denied!':
            return 0

    def connect(self):

        connection = self.auth()
        if connection:
            print('Connected!')
            # self.listen()
        else:
            print('Access denied!')

    def listen(self):
        while True:
            data = input('Enter request to server: ')
            if not(data in ('disconnect', 'exit')):
                try:
                    self.sender(data)
                    msg = self.get_msg()
                except Exception as e:
                    print(e)
                    print('Server disconnected!')
                    msg = 'Server disconnected!'

                if msg != 'default answer':
                    if msg == 'Server disconnected!':
                        exit()

                    else:
                        # server message processing
                        text1 = msg.split('\n')
                        text = '\t'
                        for i in text1:
                            text = f'{text}{i}\n\t'
                        text = text.rstrip()

                        print(f'SERVER ANSWER:\n{text}')

            else:
                self.sender('disconnect')
                self.cli.close()
                print('Exiting...')
                exit()


class Gui(QtWidgets.QMainWindow):
    client = sqlite3.connect('vk_bot_db.db')
    user_role_and_group_id = (0, 0, 0)

    def __init__(self, parent=None):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.centerOnScreen()
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint |
                            QtCore.Qt.WindowCloseButtonHint)
        self.authorization_status = False
        self.auth_win_status = True
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton.setAutoDefault(True)
        self.ui.pushButton_2.clicked.connect(self.register)
        #self.user_role_and_group_id = None
        self.flag_check_user_group_id = False

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
        global login_var
        login_var = self.ui.lineEdit_2.text()
        passw = self.ui.lineEdit.text()
        cur1 = self.client.cursor()
        search_login = 0
        # Пытаемся найти ник в коллекции
        if login_var and passw:
            for search_login in cur1.execute("""SELECT login FROM users WHERE login = (?)""", (login_var,)):
                print('***login: ', search_login, '***')
            cur1.close()  # ! можно и не закрывать после каждого запроса, хотя я хз. Можно потом с той же переменной открыть курсор
            if search_login:  # Если нашли значение
                return "value_exists"
            else:  # Если значения нет
                print(search_login)
                print(login_var)
                return "value_not_found"
        # Если данные не заполнены
        else:
            return "no_data_avaliable"

    def login(self):
        global user_role_and_group_id
        global user_role_and_group_id_status
        global flag_check_user_group_id
        if self.authorization_status is False:
            # if authorization_status is False:
            result = self.check_data()
            if result == "value_exists":
                login_var = self.ui.lineEdit_2.text()
                passw = self.ui.lineEdit.text()
                cur1 = self.client.cursor()
                user_document = 0
                for user_document in cur1.execute("""SELECT password FROM users WHERE login = (?) AND password = (?)""", (login_var, passw,)):
                    print('***pass:', user_document, '***')
                if user_document and passw == user_document[0]:
                    message_log = "Успешная авторизация!"
                    print('----- success login -----')
                    for user_role_and_group_id in cur1.execute("""SELECT login, user_role, user_group_id FROM users WHERE login = (?) AND password = (?)""", (login_var, passw,)):
                        print('***user_role_and_group_id: ',
                              user_role_and_group_id, '***')
                    flag_check_user_group_id = True
                    user_role_and_group_id_status = user_role_and_group_id[2]
                    QtWidgets.QMessageBox.about(
                        self, "Уведомление", message_log)
                    self.authorization_status = True
                    self.close()
                    self.auth_win_status = False
                    work.WorkGui(user_role_and_group_id_status).show()
                    #work.WorkGui.check_user_group_id(work.WorkGui(), user_role_and_group_id_status, login_var)
                    #work = work.WorkGui()
                    # work.show()

                    cur_login_name = self.client.cursor()
                    for user_name_db in cur_login_name.execute("""SELECT user_name FROM users WHERE login = (?) AND password = (?)""", (login_var, passw,)):
                        print('***', user_name_db, '***')
                    #user_name = str(user_name_db[0])
                    # work.WorkGui().ui.l_name.setText(user_name)
                    cur_login_name.close()
                    cur1.close()
                    return user_role_and_group_id
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
    # Для решение проблемы с повторной авторизацией необходимо за коментить window.close() и work.show()
    # window.close()  # ! это закрывает первое окно с авторизацией
    #work = work.WorkGui()
    # work.show()  # ! это открывает второе окно с рабочей областью
    Client('192.168.0.110', 7000).connect()
    sys.exit(app.exec_())
