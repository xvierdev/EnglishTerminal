import os
try:
    file_path = os.path.dirname(os.path.abspath(__file__))
    with open(file_path + '\\wordlist.txt', 'w', encoding='utf-8') as refined_file:
        with open(file_path +'\\brute_wordlist.txt', 'r', encoding='utf-8') as file:
            for line in file.readlines():
                if not line.startswith('#'):
                    line_split = line.split(' ')
                    if len(line_split) >= 3 and line_split[1] != line_split[2]:
                        refined_file.write(line.lower())
                        print(f'Added {line} to "wordlist.txt"')
except FileNotFoundError as e:
    print('File not found.')