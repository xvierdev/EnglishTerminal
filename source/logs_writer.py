import datetime
from pathlib import Path

def write_log(message, level="INFO", module=__file__):
    """Escreve uma mensagem de log no arquivo de log."""
    try:
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(get_log_file_path(), "a", encoding='utf-8') as f:
            f.write(f"{date} {level} [{Path(module).name}] {message}\n")
    except IOError as e:
        print(f"Erro ao escrever log: {e}")

def get_log_file_path():
    """Retorna o caminho do arquivo de log com base na data atual."""
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')
    log_dir = Path(__file__).parent / "logs"
    log_dir.mkdir(exist_ok=True)
    return log_dir / f"log_{date_str}.log"

if __name__ == "__main__":
    write_log("Teste de log", "INFO", __file__)