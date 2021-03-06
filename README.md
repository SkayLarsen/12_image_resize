# Image Resizer

Скрипт изменяет размер изображения в одном из популярных графических форматов (jpg, png, gif, bmp).

В качестве обязательного аргумента принимает имя входного файла. Кроме этого, доступные следующие аргументы:

-h, --help — вывод справочной информации

-w, --width — ширина результирующего изображения

-H, --height — высота результирующего изображения

-s, --scale — коэффициент масштабирования

-o, --output — имя результирующего файла

* Если указана только ширина – высота считается так, чтобы сохранить пропорции изображения. И наоборот – если указана и ширина и высота, создаётся именно такое изображение (при несовпадении пропорций будет выведено предупреждение). 
* Если указан масштаб, то ширина и высота указаны быть не могут. 
* Если не указан путь до результирующего файла, то результат кладётся рядом с исходным файлом. Если исходный файл называется pic.jpg и имеет размер 100x200, то после вызова python image_resize.py --scale 2 pic.jpg появится файл pic__200x400.jpg.


# Quickstart

Скрипт требует для своей работы установленный интерпретатор Python версии 3.5, а также некоторые дополнительные зависимости, которые можно установить следующим образом:
```
pip install -r requirements.txt
```

Запуск на Linux:

```#!bash
$ python image_resize.py [args]
```
Запуск на Windows происходит аналогично.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
