
import main
from PyQt5.QtCore import *
from window_add_stud import *
from random import randint
import work



class AddStudGui(main.Gui):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self)
        self.centerOnScreen()
        self.setWindowModality(Qt.ApplicationModal) # эта функция блокирует использование другого окна пока это окно работает
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        self.ui.close_btn.clicked.connect(self.close_add_stud)
        self.ui.add_btn.clicked.connect(self.add_new_stud)
        self.ui.clean_pte_btn.clicked.connect(self.clear_button_stud)
        
        self.ui.pte_f_name.textChanged.connect(self.get_focus_stud)
        self.ui.pte_l_name.textChanged.connect(self.get_focus_stud)
        self.ui.pte_m_name.textChanged.connect(self.get_focus_stud)
        self.ui.pte_number.textChanged.connect(self.get_focus_stud)
        

    def close_add_stud(self):
        self.close()


    '''
    def keyPressEvent(self, e):  # Классная штука. Закрывает окно по нажатию Esc
        if e.key() == Qt.Key_Escape:
            self.close()
    '''


    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if self.auth_win_status == True and event.type() == QtCore.QEvent.KeyPress:
            if event.key() == 16777220 or event.key() == 16777221: # (F12 16777275) (ENTER 16777220 or 16777221 - this for NUMPAD)
                self.auth_win_status == False    
        return

    def get_focus_stud(self):
        self.ui.status_new_stud.setText('Редактируется')
        return

    
    def clear_button_stud(self):
        self.ui.pte_f_name.setText('')
        self.ui.pte_l_name.setText('')
        self.ui.pte_m_name.setText('')
        self.ui.pte_number.setText('')
        self.ui.status_new_stud.setText('')
        return
    


    def add_new_stud(self):
        print('!!! start adding student !!!')
        y = 0
        x = 1
        #print('y=1')
        #print('x=1')
        #print('---------------')
        while y != x:    
            x = randint(0, 50)
            cursor_get_id_stud = self.client.cursor()
            #print(x)
            cursor_get_id_stud.execute(
                """SELECT * FROM students WHERE id_students = (?)""", (x,))
            y = cursor_get_id_stud.fetchone()
            #print('***', y, '***')
            cursor_get_id_stud.close()
            print('-----------------')
            print('add student')
            print('-----------------')
            if y == None:
                self.new_f_name = self.ui.pte_f_name.text()
                self.new_l_name = self.ui.pte_l_name.text()
                self.new_m_name = self.ui.pte_m_name.text()
                self.new_number = self.ui.pte_number.text()
                self.data = [(x, self.new_f_name, self.new_l_name, self.new_m_name, self.new_number)]
                cursor_add_student = self.client.cursor()
                cursor_add_student.executemany(
                    """INSERT INTO students (id_students, name, surname, patronymic, student_number) VALUES(?, ?, ?, ?, ?);""", self.data)
                self.client.commit()
                cursor_add_student.close()
                #print('x = ', x)
                #print('Success!')
                visual_x = x - 1
                message_add_stud = "Добавлен студент с номером: " + str(visual_x)
                print(message_add_stud)
                QtWidgets.QMessageBox.critical(self, "Ошибка", message_add_stud)
                self.close()
                #work.WorkGui().download_tab(3, 1)                
                self.ui.pte_f_name.setText('')
                self.ui.pte_l_name.setText('')
                self.ui.pte_m_name.setText('')
                self.ui.pte_number.setText('')
                self.ui.status_new_stud.setText('')
                break
            else:
                print('debag')
                #print('x = ', x)
                #print('y = ', y)
                #print('no')
                #print('---------------')
        work.WorkGui().download_tab(tab=3, refresh=1)
        print("Обновление прошло успешно") # проблем никаких нет вроде,но прога после добавления студента проходит 2 раза обновление и не обновляет

        return
