import util
import logs

# Constantes
HASH_FILE = 'records_hash.txt'

def write_records(name, points):
    """Escreve um novo recorde e atualiza o hash."""
    try:
        records = util.get_records_from_db()
        records.append((util.now(), name, points))
        records.sort(key=lambda x: x[2], reverse=True)
        records = records[:5]  # Mantém apenas os 5 melhores

        util.save_records_to_db(records)

        hash_records = util.calcular_hash(records)
        with open(HASH_FILE, "w") as f:
            f.write(hash_records)

    except IOError as e:
        logs.report_bug(f"Erro ao escrever recordes: {e}")
        print(f'Error: {e}')

def load_records():
    """Carrega e verifica os recordes, retornando os 5 melhores."""
    records = util.get_records_from_db()
    if not records:
        return []

    try:
        with open(HASH_FILE, "r") as f:
            hash_armazenado = f.read()
        hash_records_novo = util.calcular_hash(records)

        if hash_armazenado == hash_records_novo:
            return records
        else:
            print('Arquivo de hash corrompido!\n')
            util.save_records_to_db([])  # Limpa os recordes
            #os.remove(HASH_FILE) #Remover essa linha, pois o arquivo hash não precisa ser deletado.
            return []

    except (FileNotFoundError, IOError, ValueError) as e:
        logs.report_bug(f"Erro ao carregar recordes: {e}")
        return []