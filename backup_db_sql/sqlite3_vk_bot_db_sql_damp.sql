BEGIN TRANSACTION;CREATE TABLE "groups" (
	"id_group"	INTEGER NOT NULL UNIQUE,
	"name_group"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("id_group" AUTOINCREMENT)
);INSERT INTO "groups" VALUES(1,'НПв-181');INSERT INTO "groups" VALUES(2,'Тестовая группа 1');INSERT INTO "groups" VALUES(3,'Тестовая группа 2');CREATE TABLE "marks" (
	"id_mark"	INTEGER NOT NULL UNIQUE,
	"name_subject"	TEXT NOT NULL,
	"student_id"	INTEGER NOT NULL,
	FOREIGN KEY("student_id") REFERENCES "students"("id_students"),
	PRIMARY KEY("id_mark" AUTOINCREMENT)
);DELETE FROM "sqlite_sequence";INSERT INTO "sqlite_sequence" VALUES('timetable_temp',2);INSERT INTO "sqlite_sequence" VALUES('students',50);INSERT INTO "sqlite_sequence" VALUES('groups',3);INSERT INTO "sqlite_sequence" VALUES('users',3);CREATE TABLE "students" (
	"id_students"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"surname"	TEXT NOT NULL,
	"patronymic"	TEXT,
	"student_number"	INTEGER NOT NULL UNIQUE,
	"group_id"	INTEGER,
	FOREIGN KEY("group_id") REFERENCES "groups"("id_group"),
	PRIMARY KEY("id_students" AUTOINCREMENT)
);INSERT INTO "students" VALUES(0,'Максим','Кочетков','Владимирович',222034304,NULL);INSERT INTO "students" VALUES(1,'Сергей','Зайцев','Владимирович',123456789,NULL);INSERT INTO "students" VALUES(2,'Николай','Николаев','Олегович',8765876,NULL);INSERT INTO "students" VALUES(6,'Кристиан','Михайлов','Олегович',213423423,NULL);INSERT INTO "students" VALUES(38,'ggggg','hhhhh','jjjjj',5465462,NULL);INSERT INTO "students" VALUES(50,'Михаил','Козлов','Алексеевич',34234243,NULL);CREATE TABLE "timetable_temp" (
	"id_event_temp"	INTEGER NOT NULL UNIQUE,
	"text_event_temp"	TEXT NOT NULL,
	"date_event"	TEXT NOT NULL,
	PRIMARY KEY("id_event_temp" AUTOINCREMENT)
);INSERT INTO "timetable_temp" VALUES(0,'Тестовое временное событие №1','06.05.2022');INSERT INTO "timetable_temp" VALUES(1,'Тестовое временное событие №2','07.05.2022');CREATE TABLE "timetable_ussual" (
	"id_event_ussual"	INTEGER NOT NULL UNIQUE,
	"text_event_ussual"	TEXT,
	"group_id"	INTEGER NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "groups"("id_group"),
	PRIMARY KEY("id_event_ussual")
);INSERT INTO "timetable_ussual" VALUES(10,'Всем привет! Сегодня у нас пара по искусственному интеллекту',1);INSERT INTO "timetable_ussual" VALUES(11,'Всем привет! Сегодня занятий нет :)',1);INSERT INTO "timetable_ussual" VALUES(20,'Всем привет! Сегодня занятий нет :)',1);INSERT INTO "timetable_ussual" VALUES(21,'Всем привет! Сегодня занятий нет :)',1);INSERT INTO "timetable_ussual" VALUES(30,'Всем привет! Сегодня у нас пара по английскому языку для слабой группы',1);INSERT INTO "timetable_ussual" VALUES(31,'Всем привет! Сегодня у нас пара по английскому языку для сильной группы',1);INSERT INTO "timetable_ussual" VALUES(40,'Всем привет! Сегодня занятий нет :)',1);INSERT INTO "timetable_ussual" VALUES(41,'Всем привет! Сегодня занятий нет :)',1);INSERT INTO "timetable_ussual" VALUES(50,'Всем привет! Сегодня занятий нет :)',1);INSERT INTO "timetable_ussual" VALUES(51,'Всем привет! Сегодня занятий нет :)',1);INSERT INTO "timetable_ussual" VALUES(60,'Всем привет! Сегодня у нас пары в MS Teams',1);INSERT INTO "timetable_ussual" VALUES(61,'Всем привет! Сегодня у нас очные пары в университете на орджо',1);CREATE TABLE "users" (
	"id_user"	INTEGER NOT NULL UNIQUE,
	"login"	TEXT NOT NULL UNIQUE,
	"password"	TEXT NOT NULL UNIQUE,
	"user_name"	TEXT NOT NULL,
	"user_role"	INTEGER,
	"user_group_id"	INTEGER,
	PRIMARY KEY("id_user" AUTOINCREMENT),
	FOREIGN KEY("user_group_id") REFERENCES "groups"("id_group")
);INSERT INTO "users" VALUES(1,'max','1','Максим',1,NULL);INSERT INTO "users" VALUES(2,'sergo','2','Сергей',2,2);INSERT INTO "users" VALUES(3,'nastya','3','Анастасия',2,1);COMMIT;