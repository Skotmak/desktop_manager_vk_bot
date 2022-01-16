import sys
import pymongo #pip install pymongo[srv]
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from window_auth import *
from work import *




class Gui(QtWidgets.QMainWindow):
    client = pymongo.MongoClient("mongodb+srv://user:2467531max@cluster0.najw2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Авторизация в \"Бот РУДН\"")
        self.centerOnScreen()
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
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
                    message_log = "Успешная авторизация!"
                    QtWidgets.QMessageBox.about(self, "Уведомление", message_log)
                    self.authorization_status = True
                    self.close()
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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Gui()
    window.show()
    work = WorkGui()
    
    sys.exit(app.exec_())