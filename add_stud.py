
from main import *
from PyQt5.QtCore import *
from window_add_stud import *
#import work
from random import randint
#import main



class AddStudGui(Gui):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self)
        self.centerOnScreen()
        #self.setWindowModality(Qt.ApplicationModal) # эта функция блокирует использование другого окна пока это окно работает
        self.db_stud = Gui().client.stuff
        self.coll_stud = self.db_stud.students
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

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if self.auth_win_status == True and event.type() == QtCore.QEvent.KeyPress:
            if event.key() == 16777220 or event.key() == 16777221: # (F12 16777275) (ENTER 16777220 or 16777221 - this for NUMPAD)
                self.auth_win_status == False    
        return


    def get_focus_stud(self):
        self.ui.status_new_stud.setText('Редактируется')
        return


    def clear_button_stud(self):
        self.ui.pte_f_name.setPlainText('')
        self.ui.pte_l_name.setPlainText('')
        self.ui.pte_m_name.setPlainText('')
        self.ui.pte_number.setPlainText('')
        self.ui.status_new_stud.setText('')
        #WorkGui(Gui).download_tab(tab=3, refresh=1)
        return



    def add_new_stud(self):
        y = 1
        x = 1
        print('y=1')
        print('x=1')
        print('---------------')
        while y == x:
            x = randint(0, 1000)
            y = self.coll_stud.find_one({"_id": x})
            x = randint(0, 1000)
            print('x = ', x)
            print('y = ', y)
            print('no')
            print('---------------')
        print('yes')

        self.new_f_name = self.ui.pte_f_name.toPlainText()
        self.new_l_name = self.ui.pte_l_name.toPlainText()
        self.new_m_name = self.ui.pte_m_name.toPlainText()
        self.new_number = self.ui.pte_number.toPlainText()
        self.data = {'_id': x, 'l_name': self.new_l_name, 'f_name': self.new_f_name, 'm_name': self.new_m_name, 'number': self.new_number, 'role': 'student'}
        self.coll_stud.insert_one(self.data)
        print('Success!')
        #WorkGui(Gui).download_tab(tab=3, refresh=1)


        #WorkGui().download_tab(tab=3, refresh=0)


        return


        
        
        
        
        


