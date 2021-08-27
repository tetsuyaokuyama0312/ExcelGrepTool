from dataclasses import dataclass


@dataclass
class GrepMatchedResult:
    file_path: str
    sheet_title: str
    cell_location: str
    matched_text: str
    grep_word: str
