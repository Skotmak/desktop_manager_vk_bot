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
        self.current_id = 0
        self.n = 0
        self.ui.plainTextEdit.setReadOnly(True)

        # Ставит дату по умолчанию на текущую дату
        self.today = QtCore.QDate.currentDate()
        self.ui.DE_temp.setDate(self.today)

        self.del_item_tab3_status = True

        self.sel_item_tab3 = ''
        self.sel_item_tab3_str = ''
        self.sel_item_tab3_int = -1
        print('START selected item is ', self.sel_item_tab3)

        # сообщение для кнопки удалить студента
        self.message_error_del_item = "Вы не выбрали строку!\nПожалуйста, выберите строку для удаления"

        # Загрузка таблиц 2 и 3
        if main.frirst_update_on_start == 0:
            self.download_tab(tab=2, refresh=0)
            self.download_tab(tab=3, refresh=0)
            main.frirst_update_on_start += 1

        ''' TAB 1 '''
        '''day - день недели; parity - четность недели: 0 - чётная неделя   1 - не чётная неделя '''
        self.ui.b_mon_0.clicked.connect(
            lambda day: self.get_day(day=1, parity=0))
        self.ui.b_tue_0.clicked.connect(
            lambda day: self.get_day(day=2, parity=0))
        self.ui.b_wed_0.clicked.connect(
            lambda day: self.get_day(day=3, parity=0))
        self.ui.b_thu_0.clicked.connect(
            lambda day: self.get_day(day=4, parity=0))
        self.ui.b_fri_0.clicked.connect(
            lambda day: self.get_day(day=5, parity=0))
        self.ui.b_sat_0.clicked.connect(
            lambda day: self.get_day(day=6, parity=0))

        self.ui.b_mon_1.clicked.connect(
            lambda day: self.get_day(day=1, parity=1))
        self.ui.b_tue_1.clicked.connect(
            lambda day: self.get_day(day=2, parity=1))
        self.ui.b_wed_1.clicked.connect(
            lambda day: self.get_day(day=3, parity=1))
        self.ui.b_thu_1.clicked.connect(
            lambda day: self.get_day(day=4, parity=1))
        self.ui.b_fri_1.clicked.connect(
            lambda day: self.get_day(day=5, parity=1))
        self.ui.b_sat_1.clicked.connect(
            lambda day: self.get_day(day=6, parity=1))

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
        self.ui.delete_stud_btn.clicked.connect(
            lambda del_tab: self.delete_item_in_tab(del_tab=3))
        self.ui.refresh_btn_tab3.clicked.connect(
            lambda tab: self.download_tab(tab=3, refresh=1))
        self.ui.stud_tab.itemClicked.connect(self.onItemClicked)

        ''' End tab '''

        ''' Functions '''

    def onItemClicked(self):
        self.sel_item_tab3 = self.ui.stud_tab.currentItem()
        if self.sel_item_tab3.text(0) != '':
            self.sel_item_tab3_int = int(self.sel_item_tab3.text(0))
            print('selected item is ', self.sel_item_tab3_int)
            self.del_item_tab3_status = True
            print(self.del_item_tab3_status)

        else:
            self.sel_item_tab3_str = str(self.sel_item_tab3.text(0))
            self.sel_item_tab3_int = -1
            print('selected item is null')
            return

    def delete_item_in_tab(self, del_tab):
        if self.sel_item_tab3_int >= 0:
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
                if self.del_item_tab3_status == True:
                    cursor_delete_tab3_item = self.client.cursor()
                    cursor_delete_tab3_item.execute(
                        """DELETE FROM students WHERE id_students = (?)""", (self.sel_item_tab3_int,))
                    print('***', 'Succesful delete item = ',
                          self.sel_item_tab3_int, '***')
                    self.client.commit()
                    cursor_delete_tab3_item.close()
                    self.download_tab(tab=3, refresh=1)
                    self.del_item_tab3_status = False
                    return
                elif self.del_item_tab3_status == False:
                    QtWidgets.QMessageBox.critical(
                        self, "Ошибка", self.message_error_del_item)
        elif self.sel_item_tab3_str == '':
            QtWidgets.QMessageBox.critical(
                self, "Ошибка", self.message_error_del_item)
        else:
            QtWidgets.QMessageBox.critical(
                self, "Ошибка", self.message_error_del_item)

    def open_window_add_stud(self):
        if all_students == True:
            message_error_stud = "Превышено количество студентов!\nПожалуйста, проверьте актуальность стдентов"
            QtWidgets.QMessageBox.critical(self, "Ошибка", message_error_stud)
        else:
            self.add_stud.show()

    def download_tab(self, tab, refresh):
        if tab == 2:
            timetable_temp_cursor = self.client.cursor()
            timetable_temp_cursor.execute("""SELECT * FROM timetable_temp""")
            temp_results = timetable_temp_cursor.fetchall()
            self.count_temp_event = len(temp_results)
            #print("count temp event: ", self.count_temp_event)
            timetable_temp_cursor.close()
            if refresh == 1:
                self.ui.TW_temp.clear()
                print("--- --- ---")
                print('deteted tab 2')
                print("--- --- ---")
            for n_stud_tab2 in range(0, self.count_temp_event):
                item_1 = QtWidgets.QTreeWidgetItem(self.ui.TW_temp)
                self.ui.TW_temp.addTopLevelItem(item_1)
                cursor_download_tab2 = self.client.cursor()
                cursor_download_tab2.execute(
                    """SELECT * FROM timetable_temp WHERE id_event_temp = (?)""", (n_stud_tab2,))
                self.res_stud_tab2 = cursor_download_tab2.fetchone()
                #print('***', self.res_stud_tab2, '***')
                cursor_download_tab2.close()
                # print('-----------------')
                #print(n_stud_tab2, " = ", self.res_stud_tab2[0])
                # print('-----------------')
                if self.res_stud_tab2 == None:
                    n_stud_tab2 += 1
                else:
                    self.text_event_temp = self.res_stud_tab2[1]
                    #print('text_event_temp = ' + self.text_event_temp)
                    self.date_event_temp = self.res_stud_tab2[2]
                    #print('date_event_temp = ' + self.date_event_temp)
                    self.ui.TW_temp.topLevelItem(
                        n_stud_tab2).setText(0, self.res_stud_tab2[2])
                    self.ui.TW_temp.topLevelItem(
                        n_stud_tab2).setText(1, self.res_stud_tab2[1])
                    n_stud_tab2 += 1
            print('downloaded tab 2')
        elif tab == 3:
            stud_cursor = self.client.cursor()
            stud_cursor.execute("""SELECT * FROM students""")
            results = stud_cursor.fetchall()
            self.count_stud = len(results)
            #print("count students: ", self.count_stud)
            stud_cursor.close()
            if self.count_stud >= 50:
                self.all_students = True
            if refresh == 1:
                # self.ui.stud_tab.takeTopLevelItem(self.ui.stud_tab.indexOfTopLevelItem(0))
                self.ui.stud_tab.clear()
                print("--- --- ---")
                print('deteted tab 3')
                print("--- --- ---")
            self.true_count_stud = 0
            self.res_stud_tab3 = 0
            while self.true_count_stud != self.count_stud:
                for n_stud_tab3 in range(0, 50):
                    item_1 = QtWidgets.QTreeWidgetItem(self.ui.stud_tab)
                    self.ui.stud_tab.addTopLevelItem(item_1)
                    cursor_download_tab3 = self.client.cursor()
                    # print(n_stud_tab3)
                    cursor_download_tab3.execute(
                        """SELECT * FROM students WHERE id_students = (?)""", (n_stud_tab3,))
                    self.res_stud_tab3 = cursor_download_tab3.fetchone()
                    #print('***', self.res_stud_tab3, '***')
                    cursor_download_tab3.close()
                    if self.res_stud_tab3 == None:
                        n_stud_tab3 += 1
                    else:
                        # print('-----------------')
                        #print(n_stud_tab3, " = ", self.res_stud_tab3[0])
                        # print('-----------------')
                        self.ID_SQL = str(self.res_stud_tab3[0])
                        #print('ID = ' + self.ID_SQL)
                        self.l_nameSQL = str(self.res_stud_tab3[2])
                        #print('l_name = ' + self.l_nameSQL)
                        self.f_nameSQL = str(self.res_stud_tab3[1])
                        #print('f_name = ' + self.f_nameSQL)
                        self.m_nameSQL = str(self.res_stud_tab3[3])
                        #print('m_name = ' + self.m_nameSQL)
                        self.numberSQL = str(self.res_stud_tab3[4])
                        #print('number = ', self.numberSQL)
                        self.ui.stud_tab.topLevelItem(
                            n_stud_tab3).setText(0, self.ID_SQL)
                        self.ui.stud_tab.topLevelItem(
                            n_stud_tab3).setText(1, self.l_nameSQL)
                        self.ui.stud_tab.topLevelItem(
                            n_stud_tab3).setText(2, self.f_nameSQL)
                        self.ui.stud_tab.topLevelItem(
                            n_stud_tab3).setText(3, self.m_nameSQL)
                        self.ui.stud_tab.topLevelItem(
                            n_stud_tab3).setText(4, self.numberSQL)
                        n_stud_tab3 += 1
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
            self.send_id_message_tab1 = self.current_id
            self.send_id_and_text = (self.text, self.send_id_message_tab1)
            cursor_send_day = self.client.cursor()
            cursor_send_day.execute(
                """UPDATE timetable_ussual SET text_event_ussual = ? WHERE id_event_ussual = ?""", self.send_id_and_text)
            self.client.commit()
            cursor_send_day.close()
            self.ui.l_status.setText('Изменения приняты!')
            return
        else:
            self.ui.l_status.setText('')
            return

    def base_changes(self):
        self.ui.l_status.setText('Неизменено')
        self.ui.plainTextEdit.setReadOnly(False)
        return

    def get_day(self, day, parity):
        cursor_get_day = self.client.cursor()
        if day == 1:
            if parity == 0:
                self.current_id = 10
                self.ui.l_day.setText('Понедельник (чётная неделя)')
                cursor_get_day.execute(
                    """SELECT * FROM timetable_ussual WHERE id_event_ussual = (?)""", (self.current_id,))
            elif parity == 1:
                self.current_id = 11
                self.ui.l_day.setText('Понедельник (нечётная неделя)')
                cursor_get_day = self.client.cursor()
                cursor_get_day.execute(
                    """SELECT * FROM timetable_ussual WHERE id_event_ussual = (?)""", (self.current_id,))
        elif day == 2:
            if parity == 0:
                self.current_id = 20
                self.ui.l_day.setText('Вторник (чётная неделя)')
                cursor_get_day.execute(
                    """SELECT * FROM timetable_ussual WHERE id_event_ussual = (?)""", (self.current_id,))
            elif parity == 1:
                self.current_id = 21
                self.ui.l_day.setText('Вторник (нечётная неделя)')
                cursor_get_day.execute(
                    """SELECT * FROM timetable_ussual WHERE id_event_ussual = (?)""", (self.current_id,))
        elif day == 3:
            if parity == 0:
                self.current_id = 30
                self.ui.l_day.setText('Среда (чётная неделя)')
                cursor_get_day.execute(
                    """SELECT * FROM timetable_ussual WHERE id_event_ussual = (?)""", (self.current_id,))
            elif parity == 1:
                self.current_id = 31
                self.ui.l_day.setText('Среда (нечётная неделя)')
                cursor_get_day.execute(
                    """SELECT * FROM timetable_ussual WHERE id_event_ussual = (?)""", (self.current_id,))
        elif day == 4:
            if parity == 0:
                self.current_id = 40
                self.ui.l_day.setText('Четверг (чётная неделя)')
                cursor_get_day.execute(
                    """SELECT * FROM timetable_ussual WHERE id_event_ussual = (?)""", (self.current_id,))
            elif parity == 1:
                self.current_id = 41
                self.ui.l_day.setText('Четверг (нечётная неделя)')
                cursor_get_day.execute(
                    """SELECT * FROM timetable_ussual WHERE id_event_ussual = (?)""", (self.current_id,))
        elif day == 5:
            if parity == 0:
                self.current_id = 50
                self.ui.l_day.setText('Пятница (чётная неделя)')
                cursor_get_day.execute(
                    """SELECT * FROM timetable_ussual WHERE id_event_ussual = (?)""", (self.current_id,))
            elif parity == 1:
                self.current_id = 51
                self.ui.l_day.setText('Пятница (нечётная неделя)')
                cursor_get_day.execute(
                    """SELECT * FROM timetable_ussual WHERE id_event_ussual = (?)""", (self.current_id,))
        elif day == 6:
            if parity == 0:
                self.current_id = 60
                self.ui.l_day.setText('Суббота (чётная неделя)')
                cursor_get_day.execute(
                    """SELECT * FROM timetable_ussual WHERE id_event_ussual = (?)""", (self.current_id,))
            elif parity == 1:
                self.current_id = 61
                self.ui.l_day.setText('Суббота (нечётная неделя)')
                cursor_get_day.execute(
                    """SELECT * FROM timetable_ussual WHERE id_event_ussual = (?)""", (self.current_id,))
        self.res_timetable = cursor_get_day.fetchone()
        print('***', self.res_timetable, '***')
        cursor_get_day.close()
        self.ui.plainTextEdit.setPlainText(self.res_timetable[1])
        self.base_changes()


if __name__ == '__main__':
    self_work = WorkGui()
