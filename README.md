# Взламываем школьный дневник

**db_hack** - это набор функций, для изменения оценок, замечаний в школьном дневнике.


## Требования

- Python 3.6 или выше
- [Электронный дневник школы](https://github.com/devmanorg/e-diary/)
- [Архив с базой данных](https://dvmn.org/filer/canonical/1562234129/166/)


## Запуск

Скачайте и запустите электронный дневник школы. Вот [документация](https://github.com/devmanorg/e-diary/)

Скачайте архив с базой данных, распакуйте и положите файл базы данных `schoolbase.sqlite3` рядом с файлом `manage.py`.

Положите файл `db_hack.py` рядом с файлом `manage.py`.

Запустите Django Shell:
```sh
$ python manage.py shell
Python 3.8.10 (default, Jun  2 2021, 10:49:15) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
```

Импортируйте файл `db_hack.py`
```python
>>> import db_hack
```

Теперь можно найти ученика, которому будем исправлять оценки. Если никого не найдено или найдено слишком много учеников скрипт сообщит. В случае удачного выполнения скрипт ничего не выводит:
```python
>>> schollkid = db_hack.get_schoolkid("Йохан")
Ученик с таким именем не найден.

>>> schollkid = db_hack.get_schoolkid("Иван")
Учеников с таким именем слишком много. Попробуйте добавить фамилию или отчество.

>>> schollkid = db_hack.get_schoolkid("Фролов Иван")
```

Исправим все двойки и тройки на пятёрки:
```python
>>> db_hack.fix_marks(schoolkid)
```

Удалим все замечания:
```python
>>> db_hack.remove_chastisements(schoolkid)
```

Добавим похвалу по какому-нибудь предмету:
```python
>>> db_hack.create_commendation(schoolkid, "Математика")
```
Текст похвалы и урок выбираются случайным образом, так что никто ничего не заподозрит!

## Цели проекта

Код написан в учебных целях — для курса по Python на сайте [Devman](https://dvmn.org).