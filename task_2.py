"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш
Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""
import hashlib
import os

users = {}  # Простое демо хранилище

# Add a user
username = 'Brent'  # Имя пользователя
password = 'mypassword'  # Пароль пользователя

salt = os.urandom(32)  # Новая соль для данного пользователя
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
users[username] = {  # Хранение ключа и соли
    'salt': salt,
    'key': key
}

# Попытка проверки 1 (неправильный пароль)
username = 'Brent'
password = 'notmypassword'

salt = users[username]['salt']  # Получение соли
key = users[username]['key']  # Получение правильного ключа
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

assert key != new_key  # Ключи не совпадают, следовательно, пароли не совпадают

# Попытка проверки 2 (правильный пароль)
username = 'Brent'
password = 'mypassword'

salt = users[username]['salt']
key = users[username]['key']
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

assert key == new_key  # Ключи совпадают, следовательно, и пароли совпадают

# Добавление нового пользователя
username = 'Jarrod'
password = 'my$ecur3p@$$w0rd'

salt = os.urandom(32)  # Новая соль для данного пользователя
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
users[username] = {
    'salt': salt,
    'key': key
}

# Проверяем правильно ли введен пароль
username = 'Jarrod'
password = 'my$ecur3p@$$w0rd'

salt = users[username]['salt']
key = users[username]['key']
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

assert key == new_key  # Ключи совпадают, поэтому совпадают пароли и у этого пользователя

