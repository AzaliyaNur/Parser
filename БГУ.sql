CREATE TABLE Инфокоммуникационные_технологии_и_системы_связи (
	 nomer integer,
     id varchar(2000),
	 summa INTEGER,
	 summa1 INTEGER,
	 ball1 integer,
	 ball2 integer,
	 ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Инфокоммуникационные_технологии_и_системы_связи
FROM 'D:\Azalea\programs\Azd\11.03.02_ФТИ_Инфокоммуникационные технологии и системы связи_О_Б.HTML.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Информационная_безопасность (
	 nomer integer,
     id varchar(2000),
	 summa INTEGER,
	 summa1 INTEGER,
	 ball1 integer,
	 ball2 integer,
	 ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Информационная_безопасность
FROM 'D:\Azalea\programs\Azd\10.03.01_ИИГУ_Информационная безопасность_О_Б.HTML.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Математика (
	 nomer integer,
     id varchar(2000),
	 summa INTEGER,
	 summa1 INTEGER,
	 ball1 integer,
	 ball2 integer,
	 ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Математика
FROM 'D:\Azalea\programs\Azd\01.03.01_ФМИТ_Математика_О_Б.HTML.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Математика_и_компьютерные_науки (
	 nomer integer,
     id varchar(2000),
	 summa INTEGER,
	 summa1 INTEGER,
	 ball1 integer,
	 ball2 integer,
	 ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Математика_и_компьютерные_науки
FROM 'D:\Azalea\programs\Azd\02.03.01_ФМИТ_Математика и компьютерные науки_О_Б.HTML.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');



CREATE TABLE Математическое_обеспечение_и_администрирование_информационных_систем (
	 nomer integer,
     id varchar(2000),
	 summa INTEGER,
	 summa1 INTEGER,
	 ball1 integer,
	 ball2 integer,
	 ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Математическое_обеспечение_и_администрирование_информационных_систем
FROM 'D:\Azalea\programs\Azd\02.03.03_ФМИТ_Математическое обеспечение и администрирование информационных систем_О_Б.HTML.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');



CREATE TABLE Наноматериалы (
	 nomer integer,
     id varchar(2000),
	 summa INTEGER,
	 summa1 INTEGER,
	 ball1 integer,
	 ball2 integer,
	 ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Наноматериалы
FROM 'D:\Azalea\programs\Azd\28.03.03_ФТИ_Наноматериалы_О_Б.HTML.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');



CREATE TABLE Прикладная_информатика (
	 nomer integer,
     id varchar(2000),
	 summa INTEGER,
	 summa1 INTEGER,
	 ball1 integer,
	 ball2 integer,
	 ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Прикладная_информатика
FROM 'D:\Azalea\programs\Azd\09.03.03_ФМИТ_Прикладная информатика_О_Б.HTML.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Прикладная_математика_и_информатика (
	 nomer integer,
     id varchar(2000),
	 summa INTEGER,
	 summa1 INTEGER,
	 ball1 integer,
	 ball2 integer,
	 ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Прикладная_математика_и_информатика
FROM 'D:\Azalea\programs\Azd\01.03.02_ФМИТ_Прикладная математика и информатика_О_Б.HTML.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');



CREATE TABLE Прикладные_математика_и_физика (
	 nomer integer,
     id varchar(2000),
	 summa INTEGER,
	 summa1 INTEGER,
	 ball1 integer,
	 ball2 integer,
	 ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Прикладные_математика_и_физика
FROM 'D:\Azalea\programs\Azd\03.03.01_ФТИ_Прикладные математика и физика_О_Б.HTML.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');




CREATE TABLE Технологические_машины_и_оборудование (
	 nomer integer,
     id varchar(2000),
	 summa INTEGER,
	 summa1 INTEGER,
	 ball1 integer,
	 ball2 integer,
	 ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Технологические_машины_и_оборудование
FROM 'D:\Azalea\programs\Azd\15.03.02_ИНЖ_Технологические машины и оборудование_О_Б.HTML.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');



CREATE TABLE Электроника_и_наноэлектроника (
	 nomer integer,
     id varchar(2000),
	 summa INTEGER,
	 summa1 INTEGER,
	 ball1 integer,
	 ball2 integer,
	 ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Электроника_и_наноэлектроника
FROM 'D:\Azalea\programs\Azd\11.03.04_ФТИ_Электроника и наноэлектроника_О_Б.HTML.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');