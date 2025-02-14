import LogsCode

#exemplo
print("Conteúdo do arquivo padrão:", LogsCode.read()) #mostra o conteúdo do arquivo logs.txt(se não tiver nenhum ele não mostra nada)

LogsCode.add(dado='oi eu sou um abacaxi') #adiciona o texto entre aspas simples no arquivo logs.txt

print("Conteúdo atualizado do arquivo padrão:", LogsCode.read()) #mostra o conteúdo atualizado do arquivo

LogsCode.remove() #apaga todos os dados do arquivo

print("todos os dados foram apagados")

#também é possível escolher o arquivo para adicionar ou ler, exemplo:

LogsCode.read(name_file="nome do arquivo entre as aspas")

LogsCode.add(name_file="nome do arquivo entre as aspas" dado="dados...")

LogsCode.read(name_file="nome do arquivo entre as aspas")