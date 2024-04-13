# Инструкция по получению скриншотов

## 1. Склонируйте репозиторий.
Например, для клонирования в C:\projects\avito_trainee_assignment
выполните команду
```
git clone https://github.com/netwop/avito_trainee_assignment C:\projects\avito_trainee_assignment
```

## 2. Установите playwright и pytest
```
pip install playwright pytest
playwright install
```

## 3. Перейдите в директорию с репозиторием
```
cd /d C:\projects\avito_trainee_assignment
```

## 4. Запустите тест
```
pytest get_screenshot.py
```
Если тест прошел успешно, в дирекории "output" появится скриншот 1.png
