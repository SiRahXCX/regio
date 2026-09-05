import csv
from pypdf import PdfReader, PdfWriter
from openpyxl import load_workbook
from typing import Any


def fill_and_save_template(data: list[dict[str, Any]], template_path: str, output_path: str) -> None:
    for idx, row in enumerate(data):
        pdf_reader = PdfReader(template_path)
        pdf_writer = PdfWriter()
        pdf_writer.append(pdf_reader)

        pdf_writer.update_page_form_field_values(
            pdf_writer.pages[0],
            row
        )

        output_filename = f'{output_path}/output_{idx+1}.pdf'
        with open(output_filename, mode='wb') as output_file:
            pdf_writer.write(output_file)


def extract_data_from_csv(csv_path: str) -> list[dict[str, Any]]:
    with open(csv_path, mode='r', encoding='utf-8-sig') as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)
    return data


def extract_data_from_xlsx(xlsx_path: str) -> list[dict[str, Any]]:
    workbook = load_workbook(xlsx_path, read_only=True, data_only=True)
    worksheet = workbook.active 
    rows = worksheet.iter_rows(values_only=True)
    headers = next(rows)
    data = [dict(zip(headers, row)) for row in rows] 
    return data
