#from typing import Counter
import PyQt5
from main import Gui
from PyQt5.QtCore import *
from window_work import *
from PyQt5.QtWidgets import QTableWidgetItem
from add_stud import AddStudGui
from window_add_stud import *

all_students = False


class WorkGui(Gui):

    refresh_tab3 = False
    
    def __init__(self, parent=None):
        self.add_stud = AddStudGui()
        super().__init__()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)
        self.centerOnScreen()
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint)
        self.db = Gui.client.timetable
        self.db_stud = Gui.client.stuff
        self.coll = self.db.ussual
        self.coll_temp = self.db.temp
        self.coll_stud = self.db_stud.students
        self.current_id = 0
        #self.current_id_temp = 0
        self.n = 0
        self.ui.plainTextEdit.setReadOnly(True)
        if self.refresh_tab3 != False:
            self.download_tab(tab=3, refresh=1)
            self.refresh_tab3 = False
        

        # Ставит дату по умолчанию на текущую дату
        self.today = QtCore.QDate.currentDate()
        self.ui.DE_temp.setDate(self.today)


        # Загрузка таблиц 2 и 3
        self.download_tab(tab=2, refresh=0)
        self.download_tab(tab=3, refresh=0)
        

        ''' TAB 1 '''
        ''' 0 - чётная неделя   1 - не чётная неделя '''
        self.ui.b_mon_0.clicked.connect(lambda day: self.get_monday(day=0))
        self.ui.b_tue_0.clicked.connect(lambda day: self.get_tuesday(day=0))
        self.ui.b_wed_0.clicked.connect(lambda day: self.get_wednesday(day=0))
        self.ui.b_thu_0.clicked.connect(lambda day: self.get_thursday(day=0))
        self.ui.b_fri_0.clicked.connect(lambda day: self.get_friday(day=0))
        self.ui.b_sat_0.clicked.connect(lambda day: self.get_saturday(day=0))

        self.ui.b_mon_1.clicked.connect(lambda day: self.get_monday(day=1))
        self.ui.b_tue_1.clicked.connect(lambda day: self.get_tuesday(day=1))
        self.ui.b_wed_1.clicked.connect(lambda day: self.get_wednesday(day=1))
        self.ui.b_thu_1.clicked.connect(lambda day: self.get_thursday(day=1))
        self.ui.b_fri_1.clicked.connect(lambda day: self.get_friday(day=1))
        self.ui.b_sat_1.clicked.connect(lambda day: self.get_saturday(day=1))

        self.ui.plainTextEdit.textChanged.connect(lambda lab_stat=self.ui.l_status: self.get_focus(lab_stat))
        self.ui.clear_PTE.clicked.connect(lambda tab_num: self.clear_button(tab_num=1))
        self.ui.send_changes.clicked.connect(self.send_changes_to_db)

        ''' TAB 2 '''
        self.ui.PTE_temp.textChanged.connect(lambda lab_stat=self.ui.l_status_2: self.get_focus(lab_stat))
        self.ui.send_chages_temp.clicked.connect(self.send_temp)
        self.ui.clear_PTE_temp.clicked.connect(lambda tab_num: self.clear_button(tab_num=2))
        self.ui.delete_temp_note.clicked.connect(self.delete_temp)
        self.ui.refresh_btn_tab2.clicked.connect(lambda tab: self.download_tab(tab=2, refresh=1))
        


        ''' TAB 3 '''
        self.ui.add_stud_btn.clicked.connect(self.open_window_add_stud)
        self.ui.refresh_btn_tab3.clicked.connect(lambda tab: self.download_tab(tab=3, refresh=1))
        # self.ui.delete_stud_btn.clicked.connect(lambda tab: self.delete_all_items_in_tab(del_tab=3)) Доделай функцию delete_all_items_in_tab на удаление определённой строки


        ''' End tab '''


        ''' Функции '''
    
    def delete_all_items_in_tab(self, del_tab): # https://stackoverflow.com/questions/13062327/how-to-delete-qtreewidgetitem Доделай на удаление определённой строки
        if del_tab == 2:
            '''
            self.temp_tab_items = 0
            for temp_tab_items in range(0, self.count_temp):
                self.ui.TW_temp.removeItemWidget(self.temp_tab_items, 0)
                self.ui.TW_temp.removeItemWidget(self.temp_tab_items, 1)
                self.temp_tab_items += 1
            '''
            return
        elif del_tab == 3:
            '''
            self.stud_tab_items = 0
            for stud_tab_items in range(0, self.count_stud):
                self.ui.stud_tab.clear()
                
                #self.ui.stud_tab.removeItemWidget(self.stud_tab_items, 0)
                #self.ui.stud_tab.removeItemWidget(self.stud_tab_items, 1)
                #self.ui.stud_tab.removeItemWidget(self.stud_tab_items, 2)
                #self.ui.stud_tab.removeItemWidget(self.stud_tab_items, 3)
                
                self.stud_tab_items += 1
            '''
            return


    def open_window_add_stud(self):
        if all_students == True:
            message_error_stud = "Превышено количество студентов!\nПожалуйста, проверьте актуальность стдентов"
            QtWidgets.QMessageBox.critical(self, "Ошибка", message_error_stud)
        else:
            self.add_stud.show()

    
    def download_tab(self, tab, refresh):
        if tab == 2:
            '''
            self.count_temp = self.coll_temp.find().count()
            if refresh == 1:
                self.ui.TW_temp.clear()
                print('deteted tab 2')
            self.n_temp = 0
            for n_temp in range(0, self.count_temp):
                item_2 = QtWidgets.QTreeWidgetItem(self.ui.TW_temp)
                self.ui.TW_temp.addTopLevelItem(item_2)
                res_temp = self.coll_temp.find({"roleEvent": 'temp'})
                self.date_temp = res_temp["date"]
                self.text_temp = res_temp["text"]
                self.ui.TW_temp.topLevelItem(n_temp).setText(0, self.date_temp)
                self.ui.TW_temp.topLevelItem(n_temp).setText(1, self.text_temp)
                self.n_temp += 1
            '''
            print('downloaded tab 2')     
        elif tab == 3: 
            self.count_stud = self.coll_stud.find().count()
            #if self.count_stud >= 50:
                #all_students = True
            if refresh == 1:
                self.ui.stud_tab.clear()
                print('deteted tab 3')
            self.n_stud = 0
            self.true_count_stud = 0
            while self.true_count_stud != self.count_stud:
                for n_stud in range(0, 50):
                    item_1 = QtWidgets.QTreeWidgetItem(self.ui.stud_tab)
                    self.ui.stud_tab.addTopLevelItem(item_1)
                    res_stud = self.coll_stud.find_one({"_id": n_stud})
                    #''!'
                    print('-----------------')
                    print(n_stud, " = ", res_stud)
                    print('-----------------')
                    #''!'
                    if res_stud == None:
                        n_stud += 1
                    else:
                        self.l_name = res_stud["l_name"]
                        self.f_name = res_stud["f_name"]
                        self.m_name = res_stud["m_name"]
                        self.number = res_stud["number"]
                        self.ui.stud_tab.topLevelItem(n_stud).setText(0, self.l_name)
                        self.ui.stud_tab.topLevelItem(n_stud).setText(1, self.f_name)
                        self.ui.stud_tab.topLevelItem(n_stud).setText(2, self.m_name)
                        self.ui.stud_tab.topLevelItem(n_stud).setText(3, self.number)
                        self.n_stud += 1
                        self.true_count_stud += 1
                        if self.true_count_stud == self.count_stud:
                            break
            print('downloaded tab 3')
        return
    

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if self.auth_win_status == True and event.type() == QtCore.QEvent.KeyPress:
            if event.key() == 16777220 or event.key() == 16777221: # (F12 16777275) (ENTER 16777220 or 16777221 - this for NUMPAD)
                self.auth_win_status == False    
        return


    def get_focus(self, lab_stat):
        if lab_stat == self.ui.l_status:
            lab_stat.setText('Редактируется')
        elif lab_stat == self.ui.l_status_2:
            lab_stat.setText('Редактируется')
        return


    def clear_button(self, tab_num):
        if tab_num == 1:
            self.ui.plainTextEdit.setPlainText('')
            self.ui.plainTextEdit.setReadOnly(True)
            self.ui.l_day.setText('')
            self.current_id = 0
            self.ui.l_status.setText('')
        elif tab_num == 2:
            #self.current_id_temp = 0
            self.ui.PTE_temp.setPlainText('')
            self.ui.l_status_2.setText('')
        return


    def send_temp(self): # не готова
        self.ui.l_status_2.setText('Запись добавлена!')
        self.text_temp = self.ui.PTE_temp.toPlainText()
        self.event_data = self.ui.DE_temp.dateTime().toString('dd-MM-yyyy') #date().toPyDate()
        print(self.ui.DE_temp.date().toPyDate())
        #self.event_data_str = str(self.event_data)

        self.ui.TW_temp.setItem(self.n, 0, QTableWidgetItem(self.text_temp))
        self.ui.TW_temp.setItem(self.n, 1,  QTableWidgetItem(self.event_data))
        self.n += 1
        
        self.ui.TW_temp.setRowCount(self.n_note + 1) 

        return


    def delete_temp(self): # не готова
        self.ui.l_status_2.setText('Запись удалена!')
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

    def base_changes(self):
        self.ui.l_status.setText('Неизменено')
        self.ui.plainTextEdit.setReadOnly(False)
        return

    # 0 - чётная неделя, 1 - не чётная неделя
    def get_monday(self, day):
        if day == 0:
            res = self.coll.find_one({"_id": "10"})
            self.current_id = 10
            self.ui.plainTextEdit.setPlainText(res["shedule"])
            self.ui.l_day.setText('Понедельник (чётная неделя)')
        elif day == 1:
            res = self.coll.find_one({"_id": "11"})
            self.current_id = 11
            self.ui.plainTextEdit.setPlainText(res["shedule"])
            self.ui.l_day.setText('Понедельник (нечётная неделя)')
        self.base_changes()
        return
    

    def get_tuesday(self, day):
        if day == 0:
            res = self.coll.find_one({"_id": "20"})
            self.current_id = 20
            self.ui.plainTextEdit.setPlainText(res["shedule"])
            self.ui.l_day.setText('Вторник (чётная неделя)')
        elif day == 1:
            res = self.coll.find_one({"_id": "21"})
            self.current_id = 21
            self.ui.plainTextEdit.setPlainText(res["shedule"])
            self.ui.l_day.setText('Вторник (нечётная неделя)')
        self.base_changes()
        return


    def get_wednesday(self, day):
        if day == 0:
            res = self.coll.find_one({"_id": "30"})
            self.current_id = 30
            self.ui.plainTextEdit.setPlainText(res["shedule"])
            self.ui.l_day.setText('Среда (чётная неделя)')
        elif day == 1:
            res = self.coll.find_one({"_id": "31"})
            self.current_id = 31
            self.ui.plainTextEdit.setPlainText(res["shedule"])
            self.ui.l_day.setText('Среда (нечётная неделя)')
        self.base_changes()
        return


    def get_thursday(self, day):
        if day == 0:
            res = self.coll.find_one({"_id": "40"})
            self.current_id = 40
            self.ui.plainTextEdit.setPlainText(res["shedule"])
            self.ui.l_day.setText('Четверг (чётная неделя)')
        elif day == 1:
            res = self.coll.find_one({"_id": "41"})
            self.current_id = 41
            self.ui.plainTextEdit.setPlainText(res["shedule"])
            self.ui.l_day.setText('Четверг (нечётная неделя)')
        self.base_changes()
        return


    def get_friday(self, day):
        if day == 0:
            res = self.coll.find_one({"_id": "50"})
            self.current_id = 50
            self.ui.plainTextEdit.setPlainText(res["shedule"])
            self.ui.l_day.setText('Пятница (чётная неделя)')
        elif day == 1:
            res = self.coll.find_one({"_id": "51"})
            self.current_id = 51
            self.ui.plainTextEdit.setPlainText(res["shedule"])
            self.ui.l_day.setText('Пятница (нечётная неделя)')
        self.base_changes()
        return


    def get_saturday(self, day):
        if day == 0:
            res = self.coll.find_one({"_id": "60"})
            self.current_id = 60
            self.ui.plainTextEdit.setPlainText(res["shedule"])
            self.ui.l_day.setText('Суббота (чётная неделя)')
        elif day == 1:
            res = self.coll.find_one({"_id": "61"})
            self.current_id = 61
            self.ui.plainTextEdit.setPlainText(res["shedule"])
            self.ui.l_day.setText('Суббота (нечётная неделя)')
        self.base_changes()
        return


    ''' TAB 3 '''
    
