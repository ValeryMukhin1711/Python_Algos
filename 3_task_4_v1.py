"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""

import uuid
import hashlib
 
salt = uuid.uuid4().hex    
def hash_url(url):
    return hashlib.sha256(salt.encode() + url.encode()).hexdigest() + ':' + salt
def check_url(cash_dict,url):
    if hash_url(url) in cash_dict.keys():
        return True
    else :
        cash_dict[hashed_url] = url
        return False
cash_dict ={}
while True:
    new_url = input('Input new url or press enter for quit ')
    if new_url =="":
        print("Now in cash")
        for i in cash_dict.keys():
            print (f"{cash_dict[i]} : {i}")
        break
    else:
        hashed_url = hash_url(new_url)
        print('String for cash: ' + hashed_url)
        if check_url (cash_dict, new_url):
            print('Url alredy in cash')
        else:
            print('New url appended to cash')
