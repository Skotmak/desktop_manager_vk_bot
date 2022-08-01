BEGIN TRANSACTION;CREATE TABLE "groups" (
	"id_group"	INTEGER NOT NULL UNIQUE,
	"name_group"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id_group" AUTOINCREMENT)
);INSERT INTO "groups" VALUES(0,'Выберите группу');INSERT INTO "groups" VALUES(1,'НПв-181');INSERT INTO "groups" VALUES(2,'Тестовая группа 2');INSERT INTO "groups" VALUES(3,'Тестовая группа 3');INSERT INTO "groups" VALUES(5,'тестовая группа 5');CREATE TABLE "marks" (
	"id_mark"	INTEGER NOT NULL UNIQUE,
	"name_subject"	TEXT NOT NULL,
	"student_id"	INTEGER NOT NULL,
	FOREIGN KEY("student_id") REFERENCES "students"("id_students"),
	PRIMARY KEY("id_mark" AUTOINCREMENT)
);DELETE FROM "sqlite_sequence";INSERT INTO "sqlite_sequence" VALUES('groups',5);INSERT INTO "sqlite_sequence" VALUES('timetable_ussual',24);INSERT INTO "sqlite_sequence" VALUES('timetable_temp',4);INSERT INTO "sqlite_sequence" VALUES('users',3);INSERT INTO "sqlite_sequence" VALUES('students',50);CREATE TABLE "students" (
	"id_students"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"surname"	TEXT NOT NULL,
	"patronymic"	TEXT,
	"student_number"	INTEGER NOT NULL UNIQUE,
	"group_students_id"	INTEGER,
	FOREIGN KEY("group_students_id") REFERENCES "groups"("id_group"),
	PRIMARY KEY("id_students" AUTOINCREMENT)
);INSERT INTO "students" VALUES(0,'Максим','Кочетков','Владимирович',222034304,1);INSERT INTO "students" VALUES(1,'Сергей','Зайцев','Владимирович',123456789,1);INSERT INTO "students" VALUES(2,'uuuu','uuuu','uuuu',7686867,1);INSERT INTO "students" VALUES(3,'iiii','iiii','iiii',8888,1);INSERT INTO "students" VALUES(6,'Кристиан','Михайлов','Олегович',213423423,2);INSERT INTO "students" VALUES(7,'effef','34234','fweff',324132,3);INSERT INTO "students" VALUES(8,'ewrwer','ewrwef','ewrwer',53452345,1);INSERT INTO "students" VALUES(12,'oooo','oooo','oooo',9999,1);INSERT INTO "students" VALUES(13,'naww','naww','naww',123123123,1);INSERT INTO "students" VALUES(14,'123','2121','213',431424,3);INSERT INTO "students" VALUES(15,'qaqaqa','qaqaqa','qaaqaqa',2312456456,1);INSERT INTO "students" VALUES(16,'nnnn','nnnn','nnnn',43333,2);INSERT INTO "students" VALUES(17,'2222','2222','2222',2222,1);INSERT INTO "students" VALUES(19,'cccccc','cccc','cccc',12222,1);INSERT INTO "students" VALUES(20,'retert','34234','trerh',5342462788,1);INSERT INTO "students" VALUES(22,'4444444','3333','656456',8988576,1);INSERT INTO "students" VALUES(23,'rrrrr','rrrrr','rrrrr',42344444,1);INSERT INTO "students" VALUES(24,'321','122','123',213,1);INSERT INTO "students" VALUES(28,'fgsdfgdfb','fdgsdfg','fbgdsfgtrg',124324324,1);INSERT INTO "students" VALUES(29,'tttttt','trrrr','tttt',435345455555,1);INSERT INTO "students" VALUES(32,'mmm','mmm','mmm',1111,1);INSERT INTO "students" VALUES(33,'wee','wee','wee',33333,1);INSERT INTO "students" VALUES(35,'r34ret','e3dew','t4545tyg',343423425665,1);INSERT INTO "students" VALUES(38,'ggggg','hhhhh','jjjjj',5465462,2);INSERT INTO "students" VALUES(39,'aaaaa','qqqqq','zzzz',11111,1);INSERT INTO "students" VALUES(40,'111','111','111',111,1);INSERT INTO "students" VALUES(41,'dddddd','ddddd','ddddd',32444444,1);INSERT INTO "students" VALUES(42,'wsss','wsss','wsss',12312314534534,1);INSERT INTO "students" VALUES(43,'erer','tere','ewtert',56757,2);INSERT INTO "students" VALUES(44,'yyyyy','tyyyyy','yyyyy',6567567,1);INSERT INTO "students" VALUES(46,'qweqweasd','eweqwe','sdfadsf',324787878,1);INSERT INTO "students" VALUES(47,'kikukiuk','iiikiki','uikiyu',65456456,1);INSERT INTO "students" VALUES(48,'uyutyur','yyutyut','klyuui',75675676,1);INSERT INTO "students" VALUES(50,'Михаил','Козлов','Алексеевич',34234243,2);CREATE TABLE "timetable_temp" (
	"id_event_temp"	INTEGER NOT NULL UNIQUE,
	"text_event_temp"	TEXT NOT NULL,
	"date_event"	TEXT NOT NULL,
	"group_temp_id"	INTEGER,
	PRIMARY KEY("id_event_temp" AUTOINCREMENT),
	FOREIGN KEY("group_temp_id") REFERENCES "groups"("id_group")
);INSERT INTO "timetable_temp" VALUES(0,'Тестовое временное событие №1','06.05.2022',1);INSERT INTO "timetable_temp" VALUES(1,'Тестовое временное событие №2','07.05.2022',1);INSERT INTO "timetable_temp" VALUES(2,'Test event temp 1','22.06.2022',2);INSERT INTO "timetable_temp" VALUES(3,'Test event temp 2','23.06.2022',2);INSERT INTO "timetable_temp" VALUES(4,'test temp event for 5 group','01.02.2022',5);CREATE TABLE "timetable_ussual" (
	"id_ussual"	INTEGER NOT NULL UNIQUE,
	"id_event_ussual"	INTEGER NOT NULL,
	"text_event_ussual"	TEXT,
	"group_ussual_id"	INTEGER NOT NULL,
	PRIMARY KEY("id_ussual" AUTOINCREMENT),
	FOREIGN KEY("group_ussual_id") REFERENCES "groups"("id_group")
);INSERT INTO "timetable_ussual" VALUES(1,10,'Всем привет! Сегодня у нас пара по искусственному интеллекту',1);INSERT INTO "timetable_ussual" VALUES(2,11,'Всем привет! Сегодня занятий нет :)',1);INSERT INTO "timetable_ussual" VALUES(3,20,'Всем привет! Сегодня занятий нет :)',1);INSERT INTO "timetable_ussual" VALUES(4,21,'Всем привет! Сегодня занятий нет :)',1);INSERT INTO "timetable_ussual" VALUES(5,30,'Всем привет! Сегодня у нас пара по английскому языку для слабой группы',1);INSERT INTO "timetable_ussual" VALUES(6,31,'Всем привет! Сегодня у нас пара по английскому языку для сильной группы',1);INSERT INTO "timetable_ussual" VALUES(7,40,'Всем привет! Сегодня занятий нет :)',1);INSERT INTO "timetable_ussual" VALUES(8,41,'Всем привет! Сегодня занятий нет :)',1);INSERT INTO "timetable_ussual" VALUES(9,50,'Всем привет! Сегодня занятий нет :)',1);INSERT INTO "timetable_ussual" VALUES(10,51,'Всем привет! Сегодня занятий нет :)',1);INSERT INTO "timetable_ussual" VALUES(11,60,'Всем привет! Сегодня у нас пары в MS Teams',1);INSERT INTO "timetable_ussual" VALUES(12,61,'Всем привет! Сегодня у нас очные пары в университете на орджо',1);INSERT INTO "timetable_ussual" VALUES(13,10,'test for 2nd group 10',2);INSERT INTO "timetable_ussual" VALUES(14,11,'test for 2nd group 11',2);INSERT INTO "timetable_ussual" VALUES(15,20,'test for 2nd group 20',2);INSERT INTO "timetable_ussual" VALUES(16,21,'test for 2nd group 21',2);INSERT INTO "timetable_ussual" VALUES(17,30,'test for 2nd group 30',2);INSERT INTO "timetable_ussual" VALUES(18,31,'test for 2nd group 31',2);INSERT INTO "timetable_ussual" VALUES(19,40,'test for 2nd group 40',2);INSERT INTO "timetable_ussual" VALUES(20,41,'test for 2nd group 41',2);INSERT INTO "timetable_ussual" VALUES(21,50,'test for 2nd group 50',2);INSERT INTO "timetable_ussual" VALUES(22,51,'test for 2nd group 51',2);INSERT INTO "timetable_ussual" VALUES(23,60,'test for 2nd group 60',2);INSERT INTO "timetable_ussual" VALUES(24,61,'test for 2nd group 61',2);CREATE TABLE "users" (
	"id_user"	INTEGER NOT NULL UNIQUE,
	"login"	TEXT NOT NULL UNIQUE,
	"password"	TEXT NOT NULL,
	"user_name"	TEXT NOT NULL,
	"user_role"	INTEGER,
	"user_group_id"	INTEGER,
	PRIMARY KEY("id_user" AUTOINCREMENT),
	FOREIGN KEY("user_group_id") REFERENCES "groups"("id_group")
);INSERT INTO "users" VALUES(1,'max','1','Максим',1,NULL);INSERT INTO "users" VALUES(2,'sergo','2','Сергей',2,1);INSERT INTO "users" VALUES(3,'nastya','3','Анастасия',2,2);COMMIT;