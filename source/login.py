import db
import util

login = input('login: ')
password = input('password: ')

db.insert_user(login, password)
user = db.read_user(login)
if user[1] == util.hash_text('abc'):
    print('success')
else:
    print('fail')