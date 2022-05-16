#import PyQt5
import main
from PyQt5.QtCore import *
import window_work
from PyQt5.QtWidgets import QTableWidgetItem
import add_stud
from window_add_stud import *

all_students = False


class WorkGui(main.Gui):
    def __init__(self, parent=None):
        self.add_stud = add_stud.AddStudGui()
        super().__init__()
        self.ui = window_work.Ui_MainWindow2()
        self.ui.setupUi(self)
        self.centerOnScreen()
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint |
                            QtCore.Qt.WindowCloseButtonHint)
        #self.db = main.Gui.client.timetable
        #self.db_stud = main.Gui.client.stuff
        #self.coll = self.db.ussual
        #self.coll_temp = self.db.temp
        #self.coll_stud = self.db_stud.students
        self.current_id = 0
        self.n = 0
        self.ui.plainTextEdit.setReadOnly(True)

        # Ставит дату по умолчанию на текущую дату
        self.today = QtCore.QDate.currentDate()
        self.ui.DE_temp.setDate(self.today)

        # Загрузка таблиц 2 и 3
        ###self.download_tab(tab=2, refresh=0)
        ###self.download_tab(tab=3, refresh=0)
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

        self.ui.plainTextEdit.textChanged.connect(
            lambda lab_stat=self.ui.l_status: self.get_focus(lab_stat))
        self.ui.clear_PTE.clicked.connect(
            lambda tab_num: self.clear_button(tab_num=1))
        self.ui.send_changes.clicked.connect(self.send_changes_to_db)

        ''' TAB 2 '''
        self.ui.PTE_temp.textChanged.connect(
            lambda lab_stat=self.ui.l_status_2: self.get_focus(lab_stat))
        self.ui.send_chages_temp.clicked.connect(self.send_temp)
        self.ui.clear_PTE_temp.clicked.connect(
            lambda tab_num: self.clear_button(tab_num=2))
        self.ui.delete_temp_note.clicked.connect(self.delete_temp)
        self.ui.refresh_btn_tab2.clicked.connect(
            lambda tab: self.download_tab(tab=2, refresh=1))

        ''' TAB 3 '''
        self.ui.add_stud_btn.clicked.connect(self.open_window_add_stud)
        self.ui.refresh_btn_tab3.clicked.connect(
            lambda tab: self.download_tab(tab=3, refresh=1))

        # self.ui.delete_stud_btn.clicked.connect(lambda tab: self.delete_all_items_in_tab(del_tab=3)) Доделай функцию delete_all_items_in_tab на удаление определённой строки

        ''' End tab '''

        ''' Функции '''

    # https://stackoverflow.com/questions/13062327/how-to-delete-qtreewidgetitem Доделай на удаление определённой строки
    def delete_all_items_in_tab(self, del_tab):
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
            #print('downloaded tab 2')
        elif tab == 3:
            # self.count_stud = self.coll_stud.find().count()
            cursor = self.client.cursor()
            cursor.execute("""SELECT * FROM students""")
            results = cursor.fetchall()
            self.count_stud = len(results)
            print("count: ", self.count_stud)
            cursor.close()
            if self.count_stud >= 50:
                self.all_students = True
            if refresh == 1:
                self.ui.stud_tab.clear()
                print("--- --- ---")
                print('deteted tab 3')
                print("--- --- ---")
            #self.n_stud = 0
            self.true_count_stud = 0
            self.res_stud = 0
            while self.true_count_stud != self.count_stud:
                for n_stud in range(0, 50):
                    item_1 = QtWidgets.QTreeWidgetItem(self.ui.stud_tab)
                    self.ui.stud_tab.addTopLevelItem(item_1)
                    cursor_download_tab = self.client.cursor()
                    #res_stud = self.coll_stud.find_one({"_id": n_stud})
                    #self.search_stud = 0
                    '''
                    for self.search_stud in cursor_download_tab.execute("""SELECT * FROM students"""):
                        print('1***1', self.search_stud, '1***1')
                        self.res_stud = cursor_download_tab.fetchone()
                        print('2***2', self.res_stud, '2***2')
                    '''
                    # for self.res_stud in cursor_download_tab.execute("""SELECT * FROM students WHERE id_students = (?)""", (n_stud,)):
                    # self.search_stud =
                    print(n_stud)
                    cursor_download_tab.execute(
                        """SELECT * FROM students WHERE id_students = (?)""", (n_stud,))
                    self.res_stud = cursor_download_tab.fetchone()
                    print('***', self.res_stud, '***')
                    #    print('***', self.res_stud, '***')
                    cursor_download_tab.close()
                    # ''!'
                    print('-----------------')
                    print(n_stud, " = ", self.res_stud[0])
                    print('-----------------')
                    # ''!'
                    if self.res_stud == None:
                        n_stud += 1
                    else:
                        #self.l_name = res_stud["l_name"]
                        #self.f_name = res_stud["f_name"]
                        #self.m_name = res_stud["m_name"]
                        #self.number = res_stud["number"]
                        self.l_nameSQL = str(self.res_stud[2])
                        print('l_name = ' + self.l_nameSQL)
                        self.f_nameSQL = str(self.res_stud[1])
                        print('f_name = ' + self.f_nameSQL)
                        self.m_nameSQL = str(self.res_stud[3])
                        print('m_name = ' + self.m_nameSQL)
                        self.numberSQL = str(self.res_stud[4])
                        print('number = ', self.numberSQL)
                        '''
                        self.ui.stud_tab.topLevelItem(n_stud).setText(0, self.l_nameSQL)
                        self.ui.stud_tab.topLevelItem(n_stud).setText(1, self.f_nameSQL)
                        self.ui.stud_tab.topLevelItem(n_stud).setText(2, self.m_nameSQL)
                        self.ui.stud_tab.topLevelItem(n_stud).setText(3, self.numberSQL)
                        '''
                        '''
                        tree = self.ui.stud_tab  # replace every 'tree' with your QTreeWidget
                        strings = [n_stud, self.l_nameSQL, self.f_nameSQL, self.m_nameSQL, self.numberSQL]
                        l = []  # list of QTreeWidgetItem to add
                        for i in strings:
                            l.append(QtWidgets.QTreeWidgetItem(i))  # create QTreeWidgetItem's and append them
                        tree.addTopLevelItems(l)  # add everything to the tree
                        '''
                        #rowcount = self.ui.stud_tab.topLevelItemCount()
                        '''self.ui.stud_tab.addTopLevelItem(
                           QtWidgets.QTreeWidgetItem(n_stud))'''
                        self.ui.stud_tab.topLevelItem(
                            n_stud).setText(0, self.l_nameSQL)
                        self.ui.stud_tab.topLevelItem(
                            n_stud).setText(1, self.f_nameSQL)
                        self.ui.stud_tab.topLevelItem(
                            n_stud).setText(2, self.m_nameSQL)
                        self.ui.stud_tab.topLevelItem(
                            n_stud).setText(3, self.numberSQL)

                        # !!!!!!!!!! Всё норм но при обновлении окно не обновляется
                        n_stud += 1
                        self.true_count_stud += 1
                        if self.true_count_stud == self.count_stud:
                            break
            print('downloaded tab 3')
        return

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if self.auth_win_status == True and event.type() == QtCore.QEvent.KeyPress:
            # (F12 16777275) (ENTER 16777220 or 16777221 - this for NUMPAD)
            if event.key() == 16777220 or event.key() == 16777221:
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

    def send_temp(self):  # не готова
        self.ui.l_status_2.setText('Запись добавлена!')
        self.text_temp = self.ui.PTE_temp.toPlainText()
        self.event_data = self.ui.DE_temp.dateTime().toString(
            'dd-MM-yyyy')  # date().toPyDate()
        print(self.ui.DE_temp.date().toPyDate())
        #self.event_data_str = str(self.event_data)

        self.ui.TW_temp.setItem(self.n, 0, QTableWidgetItem(self.text_temp))
        self.ui.TW_temp.setItem(self.n, 1,  QTableWidgetItem(self.event_data))
        self.n += 1

        self.ui.TW_temp.setRowCount(self.n_note + 1)

        return

    def delete_temp(self):  # не готова
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


'''
db_stud = main.Gui.client.stuff
coll_stud = db_stud.students

def download_tab(tab, refresh):
    #self_work = WorkGui()
    if 1 == 1:
        if tab == 2:
            ''!'
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
            ''!'
            #print('downloaded tab 2')     
        elif tab == 3: 
            count_stud = coll_stud.find().count()
            if count_stud >= 50:
                all_students = True
            if refresh == 1:
                WorkGui().ui.stud_tab.clear()
                print("--- --- ---")
                print('deteted tab 3')
                print("--- --- ---")
            n_stud = 0
            true_count_stud = 0
            while true_count_stud != count_stud:
                for n_stud in range(0, 50):
                    item_1 = QtWidgets.QTreeWidgetItem(WorkGui().ui.stud_tab) # self.ui.stud_tab
                    WorkGui().ui.stud_tab.addTopLevelItem(WorkGui().item_1)
                    res_stud = coll_stud.find_one({"_id": n_stud})
                    #''!'
                    print('-----------------')
                    print(n_stud, " = ", res_stud)
                    print('-----------------')
                    #''!'
                    if res_stud == None:
                        n_stud += 1
                    else:
                        l_name = res_stud["l_name"]
                        f_name = res_stud["f_name"]
                        m_name = res_stud["m_name"]
                        number = res_stud["number"]
                        WorkGui().ui.stud_tab.topLevelItem(n_stud).setText(0, l_name)
                        WorkGui().ui.stud_tab.topLevelItem(n_stud).setText(1, f_name)
                        WorkGui().ui.stud_tab.topLevelItem(n_stud).setText(2, m_name)
                        WorkGui().ui.stud_tab.topLevelItem(n_stud).setText(3, number)
                        n_stud += 1
                        true_count_stud += 1
                        if true_count_stud == count_stud:
                            break
            print('downloaded tab 3')
        return
'''


if __name__ == '__main__':
    self_work = WorkGui()
    #self_work.download_tab(tab=2, refresh=0)

    #download_tab(tab=3, refresh=0)
