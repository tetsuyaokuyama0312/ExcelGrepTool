import os
import datetime

DEFAULT_OUT_DIR = 'output'
DEFAULT_FILENAME_DATETIME_FORMAT = '%Y%m%d_%H%M%S'


def write_results(results: list, path: str = None):
    if path is None:
        os.makedirs(DEFAULT_OUT_DIR, exist_ok=True)
        path = get_default_path()

    with open(path, encoding='utf_8', mode='w', newline='') as f:
        write(f, '=============== RESULT ===============')
        for result in results:
            write_result(f, result)
        write(f, '======================================')


def write_result(f, result):
    write(f, '--------------------------------------')
    write(f, 'File path:')
    write_with_indent(f, result.file_path)

    write(f, 'Sheet tile:')
    write_with_indent(f, result.sheet_title)

    write(f, 'Cell location:')
    write_with_indent(f, result.cell_location)

    write(f, 'Matched text:')
    write_with_indent(f, result.matched_text)

    write(f, 'Grep word:')
    write_with_indent(f, result.grep_word)
    write(f, '--------------------------------------')

    write(f, '')


def write_with_indent(f, value, indent_level=1):
    write(f, '{}{}'.format('\t' * indent_level, value))


def write(f, value):
    f.write(f'{value}\n')


def get_default_path():
    return os.path.join(DEFAULT_OUT_DIR, f'result_{now_str()}.txt')


def now_str():
    return datetime.datetime.now().strftime(DEFAULT_FILENAME_DATETIME_FORMAT)
