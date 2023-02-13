# Bank security console

This is an internal repository for employees of the bank "Radiance".
If you got into this repository by accident, then you will not be able to run it, because you do not have access to the database, but you can freely use the layout code or see how database queries are implemented.
The security console is a website that can be connected to a remote database with visits and pass cards of our bank employees.


### How to install?

Python3 should already be installed.
Then use pip (or pip3, there is a conflict with Python2) to install dependencies.
Open the command line with the Win+R keys and enter:
```
pip install -r requirements.txt
```
It is recommended to use virtualenv/venv to isolate the project.
```
https://docs.python.org/3/library/venv.html
```


### Setting environment variables

Before starting, you need to create a ".env" file in the PATH_TO_THE_FOLDER_WITH_SCRIPT\project\ and configure the environment variables by writing in it:
```
SECRET_KEY = 'secret key'
```
where a secret key received from the bank director

```
ENGINE, HOST, PORT, NAME, USER, PASSWORD
```
database data received from the bank's system administrator

Example:

USER = 'user'

PASSWORD = 'password'

etc...

```
DEBUG=False
```
make sure that debug mode is disabled


### Command to run the script:
First run the installed virtual environment:
```
PATH_TO_THE_FOLDER_WITH_SCRIPT\venv\Scripts\Scripts\activate.bat
```
when successfully launched, the (Scripts) PATH_TO_THE_FOLDER_WITH_SCRIPT\venv\Scripts\Scripts\ will appear at the beginning of the line

Next, run the main file
```
python PATH_TO_THE_FOLDER_WITH_SCRIPT\\мападе.ру runserver 0.0.0.0:8000
```
If you have installed a virtual environment, then the command can be entered without the path to the script

We open the website at:
```
http://127.0.0.1:8000/
```


### Project goal
The code is written for educational purposes on an online course for web developers dvmn.org .



# Пульт охраны банка

Это внутренний репозиторий для сотрудников банка «Сияние». 
Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть как реализованы запросы к БД.
Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.


### Как установить?

Python3 должен быть уже установлен. 
Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей.
Открываем командную строку клавишами Win+R и вводим:
```
pip install -r requirements.txt
```
Рекомендуется использовать virtualenv/venv для изоляции проекта.
```
https://docs.python.org/3/library/venv.html
```


### Настройка переменных окружения

До запуска необходимо создать файл ".env" в папке ПУТЬ_К_ПАПКЕ_СО_СКРИПТОМ\project\
и настроить переменные окружения, прописав в нем:
```
SECRET_KEY = 'secret key'
```
где secret key - полученный от директора банка секретный ключ 

```
ENGINE, HOST, PORT, NAME, USER, PASSWORD
```
полученные от системного адмнистратора банка данные базы данных 

Пример:

USER = 'user'

PASSWORD = 'password'

и т.д....

```
DEBUG=False
```
убедиться, что отключен режим отладки


### Команда на запуск скрипта:
Сначала запускаем установленное виртуальное окружение:
```
ПУТЬ_К_ПАПКЕ_СО_СКРИПТОМ\venv\Scripts\Scripts\activate.bat
``` 
при успешном запуске вначале строки появится (Scripts) ПУТЬ_К_ПАПКЕ_СО_СКРИПТОМ\venv\Scripts\Scripts\

Далее запускаем основной файл 
```
python ПУТЬ_К_ПАПКЕ_СО_СКРИПТОМ\manage.py runserver 0.0.0.0:8000
```
Если вы установили виртуальное окружение, то команду можно вводить без пути к скрипту

Открываем сайт по адресу:
```
http://127.0.0.1:8000/
```


### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
