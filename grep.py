import openpyxl as px

from grep_matched_result import GrepMatchedResult


def grep(file_path: str, grep_words: list):
    result = []
    wb = px.load_workbook(file_path)
    ws_and_cell_gen = ((ws, cell) for ws in wb for row in ws.rows for cell in row)

    for ws, cell in ws_and_cell_gen:
        value = cell.value
        if not value:
            continue

        value = str(value)
        for grep_word in grep_words:
            if grep_word in value:
                result.append(GrepMatchedResult(file_path, ws.title, cell.coordinate, value, grep_word))

    return result
