import itertools
import threading
import warnings

from file_extractor import extract_files
from grep import grep
from parallel import invoke_and_join_all

EXCEL_FILE_EXTENSIONS = ('.xlsx', '.xlsm')


def process(input_paths: list, grep_words: list):
    target_files = extract_files(input_paths, EXCEL_FILE_EXTENSIONS)

    task = create_task(target_files)

    grep_matched_results_list = invoke_and_join_all(task, target_files, grep_words=grep_words)

    grep_matched_results = itertools.chain.from_iterable(grep_matched_results_list)
    grep_matched_results = sorted(grep_matched_results, key=lambda x: (x.file_path, x.cell_location, x.grep_word))

    print()
    print('=============== RESULT ===============')
    for result in grep_matched_results:
        print_grep_matched_result(result)
        print()
    print('======================================')


def create_task(target_files: list):
    n_files = len(target_files)
    counter = itertools.count(start=1)
    lock = threading.RLock()

    def task(target_file: str, grep_words: list):
        result = grep(target_file, grep_words)
        with lock:
            print(f'{next(counter)} / {n_files} files completed', flush=True)
        return result

    return task


def print_grep_matched_result(result):
    print('--------------------------------------')
    print('File path:')
    indent_print(result.file_path)
    print('Sheet tile:')
    indent_print(result.sheet_title)
    print('Cell location:')
    indent_print(result.cell_location)
    print('Matched text:')
    indent_print(result.matched_text)
    print('Grep word:')
    indent_print(result.grep_word)
    print('--------------------------------------')


def indent_print(value, indent_level=1):
    print('{}{}'.format('\t' * indent_level, value))


if __name__ == '__main__':
    warnings.simplefilter('ignore')

    input_file_paths = input('Enter input file paths(semicolon(;) is interpreted as a separator): ').split(';')
    grep_words = input('Enter grep words(semicolon(;) is interpreted as a separator): ').split(';')

    process(input_file_paths, grep_words)
