# Gerenciador de Recordes do jogador.

import os, util, logs

#=============CONSTANTES============#

RECORDS = 'records.txt'
HASH = 'hash.txt'
PASSWORD = 'Xjd4=r#$%_&+-*/'

#==========RECORD_MANAGER==========#

def write_records(name, points):
    try:
        with open(RECORDS, 'a') as records:
            records.writelines(f'{util.now()} {name} {points}\n')

        hash_records = util.calcular_hash("records.txt")
        criptografado = util.criptografar_hash(hash_records, PASSWORD)
        with open(HASH, "w") as f:
            f.write(criptografado)
    except Exception as e:
        logs.report_bug(e)
        print(f'Error: {e}')

def load_records():
    try:
        with open(HASH, "r") as f:
            criptografado = f.read()
            hash_descriptografado = util.descriptografar_hash(criptografado, PASSWORD)
            hash_records_novo = util.calcular_hash(RECORDS)
            
            if hash_descriptografado == hash_records_novo:
                with open(RECORDS, 'r') as records:
                    records = sorted(records, key=lambda x: int(x.split()[-1]), reverse=True)[:3]
                    if records != '':
                        return records
                    else:
                        return 'No records found!'
            else:
                print ('Records file has been corrupted!\n')
                os.remove(RECORDS)
                os.remove(HASH)
                return 0
    except FileNotFoundError as e:
        logs.report_bug(e)
        return ''
    except PermissionError as e:
        logs.report_bug(e)
        return ''