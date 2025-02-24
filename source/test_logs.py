import logs

#================================#
#=definição de funções de teste.=#
#================================#
def print_test():
    for line in logs.read_log():
        print(line, end='')

#================================#
#====rotinas de teste do log.====#
#================================#

# gravar 20 linhas no log.
for i in range (1, 21):
    logs.add_log_info(f'teste de gravação de log {i}.')

# printar log na tela
print_test()

# apagar conteúdo do arquivo de log
logs.clear_log()

# reportar um bug
logs.report_bug('Test Error ...')