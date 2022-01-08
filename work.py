from main import Gui
from window_work import *
from PyQt5.QtWidgets import QTableWidgetItem

class WorkGui(Gui):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)
        self.centerOnScreen()
        self.db = Gui.client.timetable
        self.db_stud = Gui.client.stuff
        self.coll = self.db.ussual
        self.coll_temp = self.db.temp
        self.coll_stud = self.db_stud.students
        self.current_id = 0
        #self.current_id_temp = 0
        self.n = 0
        self.ui.plainTextEdit.setReadOnly(True)

        # Ставит дату по умолчанию на текущую дату
        self.today = QtCore.QDate.currentDate()
        self.ui.DE_temp.setDate(self.today)


        ''' Tab 2 '''
        # Действия при инициализации второй вкладки
        # подсчёт записей во второй вкладке
        self.count_temp = self.coll_temp.find().count()
        self.ui.TW_temp.setRowCount(self.count_temp)

        # Добавление заголовков
        self.ui.TW_temp.horizontalHeader().setVisible(True)
        self.ui.TW_temp.verticalHeader().setVisible(True)

        # Загрузка списка учащихся
        self.download_tab(tab=2)
        

        ''' Tab 3 '''
        # Действия при инициализации третьей вкладки
        # подсчёт записей в третьей вкладке
        self.count_stud = self.coll_stud.find().count()
        self.ui.stud_tab.setRowCount(self.count_stud)

        # Добавление заголовков
        self.ui.stud_tab.horizontalHeader().setVisible(True)
        self.ui.stud_tab.verticalHeader().setVisible(True)
        
        # Загрузка списка учащихся
        self.download_tab(tab=3)

        ''' Tab 4 '''
        self.download_tab(tab=4)
        

        ''' End tab '''


        #self.ui.TW_temp.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        #self.ui.TW_temp.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        # обнови дизайн документ там ошибка в заголовках
        #self.ui.TW_temp.sizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents) проблема в том что не могу поменять ширину столбцов. попоробуй через дизайнер поменять этот параметр

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

        ''' End tab '''


    def download_tab(self, tab):
        if tab == 3:
            self.n_stud = 0
            for n_stud in range(0, self.count_stud):
                res_stud = self.coll_stud.find_one({"_id": n_stud})
                self.l_name = res_stud["l_name"]
                self.f_name = res_stud["f_name"]
                self.m_name = res_stud["m_name"]
                self.number = res_stud["number"]
                self.ui.stud_tab.setItem(self.n_stud, 0, QTableWidgetItem(self.l_name))
                self.ui.stud_tab.setItem(self.n_stud, 1,  QTableWidgetItem(self.f_name))
                self.ui.stud_tab.setItem(self.n_stud, 2, QTableWidgetItem(self.m_name))
                self.ui.stud_tab.setItem(self.n_stud, 3,  QTableWidgetItem(self.number))
                self.n_stud += 1
        elif tab == 2:
            self.n_temp = 0
            for n_temp in range(0, self.count_temp):
                res_temp = self.coll_temp.find_one({"_id": n_temp})
                self.date_temp = res_temp["date"]
                self.text_temp = res_temp["text"]
                self.ui.TW_temp.setItem(self.n_temp, 0, QTableWidgetItem(self.date_temp))
                self.ui.TW_temp.setItem(self.n_temp, 1,  QTableWidgetItem(self.text_temp))
                self.n_temp += 1
        elif tab == 4: # (РАБОТАЕТ!!!! ДОДЕЛАЙ ДЛЯ 3 И 2 ВКЛАДКИ!!!)
            '''
            item_1 = QtWidgets.QTreeWidgetItem(self.ui.treeWidget)
            self.ui.treeWidget.addTopLevelItem(item_1)
            self.ui.treeWidget.topLevelItem(3).setText(3, "hi")
            '''
            self.n_stud = 0
            for n_stud in range(0, self.count_stud):
                item_1 = QtWidgets.QTreeWidgetItem(self.ui.treeWidget)
                self.ui.treeWidget.addTopLevelItem(item_1)
                res_stud = self.coll_stud.find_one({"_id": n_stud})
                self.l_name = res_stud["l_name"]
                self.f_name = res_stud["f_name"]
                self.m_name = res_stud["m_name"]
                self.number = res_stud["number"]
                self.ui.treeWidget.topLevelItem(n_stud).setText(0, self.l_name)
                self.ui.treeWidget.topLevelItem(n_stud).setText(1, self.f_name)
                self.ui.treeWidget.topLevelItem(n_stud).setText(2, self.m_name)
                self.ui.treeWidget.topLevelItem(n_stud).setText(3, self.number)
                self.n_stud += 1

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
    