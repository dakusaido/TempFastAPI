# Примерный шаблон для работы с FastAPI с бд SQLAlchemy

### Как завести у себя (вводите по одной):

#### Если еще не клонировали с github
```shell
git clone git@github.com:dakusaido/TempFastAPI.git
cd TempFastAPI
```

#### Установка виртуального окружения
```shell
python3 -m venv venv
source ./venv/bin/activate
```

#### Установка необходимых компонентов
```shell
pip install -r requirements.txt
```

### Заполнение приватных ключей/токенов

Создаем файл `.env`.

Основываясь на файле `.env.example` заполняем файл `.env`

## Не забываем и про конфигурацию `venv` в PyCharm если вы работаете там

Переходим в `File > Settings > Project: TempFastAPI > Python Interpreter`

Смотрим на `Python Interpreter` и там должен быть `venv` от TestFastAPI

Если его нет, то добавляем: `Add Interpreter` > `Add Local Interpreter` > `Environment: Existing`

Выбираем свой `venv`, файл `venv/bin/python`


### Для запуска используем:

```shell
python main.py
```
