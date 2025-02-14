from datetime import datetime
default_log_file = 'log.txt'

def read():
    with open(default_log_file, 'r') as file:
        conteudo = file.read()
    return conteudo

def add(data=''):
    with open(default_log_file, 'a') as file:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        file.write(f'{now} {data}\n')

def report_bug(error_msg=''):
    with open('error_log.txt', 'a') as file:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        file.write(f'{now} {error_msg}\n')
        print('An error occurred, see log_error.txt for more details.')
    

# por enquanto não é necessário limpar o log
# def remove(default_log_file):
#     with open(default_log_file, 'w'):
#         pass
