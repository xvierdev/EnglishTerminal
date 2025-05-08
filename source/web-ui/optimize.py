import os
try:
    itens = set()
    category = set()
    file_path = os.path.dirname(os.path.abspath(__file__))
    with open(file_path + '\\wordlist.txt', 'w', encoding='utf-8') as refined_file:
        with open(file_path +'\\brute_wordlist.md', 'r', encoding='utf-8') as file:
            for line in file.readlines():
                if not line.startswith('#'):
                    stripped_lower_line = line.lower().strip()
                    line_split =  stripped_lower_line.split(' ')
                    if len(line_split) >= 3 and line_split[1] != line_split[2]:
                        category.add(line_split[0])
                        itens.add(stripped_lower_line+'\n')
        refined_file.writelines(itens)
    print(f'added {len(itens)} lines ({len(category)} categories) to wordlist.txt')
except FileNotFoundError as e:
    print('File not found.')