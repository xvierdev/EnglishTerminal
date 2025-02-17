from util import now, calcular_hash, criptografar_hash, descriptografar_hash

RECORDS = 'records.txt'
PASSWORD = 'Xjd4=r#$%_&+-*/'

def write_records(name, points):
    with open(RECORDS, 'a') as records:
        records.writelines(f'{now()} {name} {points}\n')

    # Calcular o hash do arquivo records.txt
    hash_records = calcular_hash("records.txt")
    # Criptografar o hash com a senha
    criptografado = criptografar_hash(hash_records, PASSWORD)
    # Gravar o hash criptografado no arquivo hash.txt
    with open("hash.txt", "w") as f:
        f.write(criptografado)

def load_records():
    try:
        # Descriptografar o hash do arquivo hash.txt
        with open("hash.txt", "r") as f:
            criptografado = f.read()
            hash_descriptografado = descriptografar_hash(criptografado, PASSWORD)
            # Recalcular o hash do arquivo records.txt
            hash_records_novo = calcular_hash("records.txt")
            # Verificar se o hash foi adulterado
            if hash_descriptografado == hash_records_novo:
                with open(RECORDS, 'r') as records:
                    return sorted(records, key=lambda x: int(x.split()[-1]), reverse=True)[:3]
            else:
                print ('records file has been corrupted!n')
                return 0
    except FileNotFoundError:
        return ''