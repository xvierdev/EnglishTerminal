def read(name_file='logs.txt'):
    
    with open(name_file, 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo

def add(name_file='logs.txt', dado=''):

    with open(name_file, 'a') as arquivo:
        arquivo.write(dado + '\n')

def remove(name_file= 'logs.txt'):

    with open(name_file, 'w'): 
        
     pass
