import source.db.users as users
import util

login = input('login: ')
password = input('password: ')

users.insert_user(login, password)
user = users.read_user(login)
if user[1] == util.hash_text('abc'):
    print('success')
else:
    print('fail')