import os
try:
    itens_filter = set()
    category_filter = set()
    word_list = []
    file_path = os.path.dirname(os.path.abspath(__file__))
    with open(file_path + '\\wordlist.txt', 'w', encoding='utf-8') as refined_file:
        with open(file_path +'\\brute_wordlist.md', 'r', encoding='utf-8') as file:
            for line in file.readlines():
                text_filter = not line.startswith('#') and not line.startswith('<!--') ant not line.startswith('-->')
                if text_filter:
                    stripped_lower_line = line.lower().strip()
                    line_split =  stripped_lower_line.split(' ')
                    if len(line_split) >= 3 and line_split[1] != line_split[2]:
                        if stripped_lower_line not in itens_filter:
                            category_filter.add(line_split[0])
                            itens_filter.add(stripped_lower_line)
                            refined_file.write(stripped_lower_line + '\n')
    print(f'added {len(itens_filter)} lines ({len(category_filter)} categories) to wordlist.txt')
except FileNotFoundError as e:
    print('File not found.')

def check_in (word, set_list):
    return word in set_list