# write logs library
import datetime
from pathlib import Path

LOG_DIR = Path(__file__).parent / 'logs'
LOG_DIR.mkdir(exist_ok=True)  # Create the logs directory once, when the module is loaded

def get_log_file_path():
    '''Returns the log file path based on the current date.'''
    date_str = datetime.datetime.now().strftime('%Y-%m-%d')
    return LOG_DIR / f'log_{date_str}.log'

def write_log(message, level='INFO', module=__file__):
    '''Writes a log message to the log file.'''
    try:
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_file_path = get_log_file_path()
        with open(log_file_path, 'a', encoding='utf-8') as f:
            f.write(f'{date} {level} [{Path(module).name}] {message}\n')
    except IOError as e:
        print(f'Error writing to log file: {e}')

if __name__ == '__main__':
    write_log('Log test', 'INFO', __file__)