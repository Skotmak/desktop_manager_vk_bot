import sqlite3
import traceback
import sys

login = ('max',)
passw = (1,)

try:
    sql_con = sqlite3.connect('vk_bot_db.db')
    cursor = sql_con.cursor()
    print("База данных подключена к SQLite")
    print("-------------------------")
    '''
    cur1 = sql_con.cursor()
    for i in cur1.execute("""SELECT login FROM users WHERE login = (?)""", login):
      print(i)
    cur1.close()
    cur1 = sql_con.cursor()
    print("-------------------------")
    for i in cur1.execute("""SELECT password FROM users WHERE password = ?""", passw):
      print(i)
    print("-------------------------")
    cursor.execute("select * from students")
    results = cursor.fetchall()
    print (len(results))
    a = len(results)
    print(a)
    '''
    for n_stud in range(0, 50):
        for res_stud in cursor.execute("""SELECT * FROM students WHERE id_students = (?)""", (n_stud,)):
            print('***', res_stud, '***')
    cursor.close()

    print("Запись успешно вставлена ​​в таблицу sqlitedb_developers ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Не удалось вставить данные в таблицу sqlite")
    print("Класс исключения: ", error.__class__)
    print("Исключение", error.args)
    print("Печать подробноcтей исключения SQLite: ")
    exc_type, exc_value, exc_tb = sys.exc_info()
    print(traceback.format_exception(exc_type, exc_value, exc_tb))
finally:
    if (sql_con):
        sql_con.close()
        print("Соединение с SQLite закрыто")
