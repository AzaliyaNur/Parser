USE [Ugatu]
GO



CREATE TABLE Прикладная_математика_и_информатика (
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Прикладная_математика_и_информатика
FROM 'D:\Azalea\programs\Azd\01.03.02 Прикладная математика и информатика.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Прикладная_математика(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Прикладная_математика
FROM 'D:\Azalea\programs\Azd\01.03.04 Прикладная математика.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE  Математика_и_компьютерные_науки (
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Математика_и_компьютерные_науки
FROM 'D:\Azalea\programs\Azd\02.03.01 Математика и компьютерные науки.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Математическое_обеспечение_и_администрирование_информационных_систем (
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Математическое_обеспечение_и_администрирование_информационных_систем
FROM 'D:\Azalea\programs\Azd\02.03.03 Математическое обеспечение и администрирование информационных систем.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');





CREATE TABLE Информатика_и_вычислительная_техника (
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Информатика_и_вычислительная_техника
FROM 'D:\Azalea\programs\Azd\09.03.01 Информатика и вычислительная техника.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Информационные_системы_и_технологии(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Информационные_системы_и_технологии
FROM 'D:\Azalea\programs\Azd\09.03.02 Информационные системы и технологии.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE  Прикладная_информатика (
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Прикладная_информатика
FROM 'D:\Azalea\programs\Azd\09.03.03 Прикладная информатика.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Программная_инженерия (
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Программная_инженерия
FROM 'D:\Azalea\programs\Azd\09.03.04 Программная инженерия.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Информационная_безопасность (
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Информационная_безопасность
FROM 'D:\Azalea\programs\Azd\10.03.01 Информационная безопасность.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');

CREATE TABLE Инфокоммуникационные_технологии_и_системы_связи(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Инфокоммуникационные_технологии_и_системы_связи
FROM 'D:\Azalea\programs\Azd\11.03.02 Инфокоммуникационные технологии и системы связи.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Электроника_и_наноэлектроника(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Электроника_и_наноэлектроника
FROM 'D:\Azalea\programs\Azd\11.03.04 Электроника и наноэлектроника.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Приборостроение(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Приборостроение
FROM 'D:\Azalea\programs\Azd\12.03.01 Приборостроение.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');



CREATE TABLE Биотехнические_системы_и_технологии(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Биотехнические_системы_и_технологии
FROM 'D:\Azalea\programs\Azd\12.03.04 Биотехнические системы и технологии.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Теплоэнергетика_и_теплотехника(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Теплоэнергетика_и_теплотехника
FROM 'D:\Azalea\programs\Azd\13.03.01 Теплоэнергетика и теплотехника.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Электроэнергетика_и_электротехника(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Электроэнергетика_и_электротехника
FROM 'D:\Azalea\programs\Azd\13.03.02 Электроэнергетика и электротехника.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Энергетическое_машиностроение(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Энергетическое_машиностроение
FROM 'D:\Azalea\programs\Azd\13.03.03 Энергетическое машиностроение.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Машиностроение(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Машиностроение
FROM 'D:\Azalea\programs\Azd\15.03.01 Машиностроение.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Технологические_машины_и_оборудование(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Технологические_машины_и_оборудование
FROM 'D:\Azalea\programs\Azd\15.03.02 Технологические машины и оборудование.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Автоматизация_технологических_процессов_и_производств(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Автоматизация_технологических_процессов_и_производств
FROM 'D:\Azalea\programs\Azd\15.03.04 Автоматизация технологических процессов и производств.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');



CREATE TABLE Конструкторско_технологическое_обеспечение_машиностроительных_производств(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Конструкторско_технологическое_обеспечение_машиностроительных_производств
FROM 'D:\Azalea\programs\Azd\15.03.05 Конструкторско-технологическое обеспечение машиностроительных производств.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Мехатроника_и_робототехника(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Мехатроника_и_робототехника
FROM 'D:\Azalea\programs\Azd\15.03.06 Мехатроника и робототехника.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');

CREATE TABLE Техносферная_безопасность(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Техносферная_безопасность
FROM 'D:\Azalea\programs\Azd\20.03.01 Техносферная безопасность.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');

CREATE TABLE Материаловедение_и_технологии_материалов(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Материаловедение_и_технологии_материалов
FROM 'D:\Azalea\programs\Azd\22.03.01 Материаловедение и технологии материалов.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');

CREATE TABLE Авиастроение(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Авиастроение
FROM 'D:\Azalea\programs\Azd\24.03.04 Авиастроение.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');

CREATE TABLE Двигатели_летательных_аппаратов(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Двигатели_летательных_аппаратов
FROM 'D:\Azalea\programs\Azd\24.03.05 Двигатели летательных аппаратов.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');

CREATE TABLE Техническая_эксплуатация_летательных_аппаратов_и_двигателей(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Техническая_эксплуатация_летательных_аппаратов_и_двигателей
FROM 'D:\Azalea\programs\Azd\25.03.01 Техническая эксплуатация летательных аппаратов и двигателей.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Стандартизация_и_метрология(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Стандартизация_и_метрология
FROM 'D:\Azalea\programs\Azd\27.03.01 Стандартизация и метрология.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');

CREATE TABLE Управление_в_технических_системах(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Управление_в_технических_системах
FROM 'D:\Azalea\programs\Azd\27.03.04 Управление в технических системах.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');

CREATE TABLE Инноватика(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Инноватика
FROM 'D:\Azalea\programs\Azd\27.03.05 Инноватика.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');

CREATE TABLE Наноинженерия(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Наноинженерия
FROM 'D:\Azalea\programs\Azd\28.03.02 Наноинженерия.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Безопасность_информационных_технологий_в_правоохранительной_сфере(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Безопасность_информационных_технологий_в_правоохранительной_сфере
FROM 'D:\Azalea\programs\Azd\10.05.05 Безопасность информационных технологий в правоохранительной сфере.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Инфокоммуникационные_технологии_и_системы_специальной_связи(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Инфокоммуникационные_технологии_и_системы_специальной_связи
FROM 'D:\Azalea\programs\Azd\11.05.04 Инфокоммуникационные технологии и системы специальной связи.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Специальные_электромеханические_системы(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Специальные_электромеханические_системы
FROM 'D:\Azalea\programs\Azd\13.05.02 Специальные электромеханические системы.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Проектирование_технологических_машин_и_комплексов(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Проектирование_технологических_машин_и_комплексов
FROM 'D:\Azalea\programs\Azd\15.05.01 Проектирование технологических машин и комплексов.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');

CREATE TABLE Пожарная_безопасность(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Пожарная_безопасность
FROM 'D:\Azalea\programs\Azd\20.05.01 Пожарная безопасность.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');

CREATE TABLE Наземные_транспортно_технологические_средства(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Наземные_транспортно_технологические_средства
FROM 'D:\Azalea\programs\Azd\23.05.01 Наземные транспортно-технологические средства.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Проектирование_авиационных_и_ракетных_двигателей(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Проектирование_авиационных_и_ракетных_двигателей
FROM 'D:\Azalea\programs\Azd\24.05.02 Проектирование авиационных и ракетных двигателей.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');



CREATE TABLE Системы_управления_летательными_аппаратами(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Системы_управления_летательными_аппаратами
FROM 'D:\Azalea\programs\Azd\24.05.06 Системы управления летательными аппаратами.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


CREATE TABLE Специальные_организационно_технические_системы(
	 id VARCHAR(2000),
    ball INTEGER,
	ball1 INTEGER,
	ball2 INTEGER,
	ball3 INTEGER,
	ud INTEGER,
    sogl VARCHAR(2000)
)

BULK INSERT Специальные_организационно_технические_системы
FROM 'D:\Azalea\programs\Azd\27.05.01 Специальные организационно-технические системы.csv'
WITH (FIRSTROW=1, FIELDTERMINATOR = ';', ROWTERMINATOR = '\n');


-р; = Да
=р фЁєующ ёяхЎшры№эюёЄш; = На другой специальности
=хЄ; = Нет