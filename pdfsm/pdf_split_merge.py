import argparse
import re
from collections import OrderedDict
from typing import List

import PyPDF2


def interpret_page_numbers(page_numbers: str) -> List[int]:
    numbers = []

    page_numbers_list = page_numbers.replace(" ", "").split(",")

    if len(page_numbers_list) == 0:
        raise ValueError("There are no page numbers determined")

    for p in page_numbers_list:
        if len(re.findall(r"-", p)) == 1:
            start_n, end_n = p.split("-")
            start_n = int(start_n)
            end_n = int(end_n)
            numbers.extend(list(range(start_n, end_n + 1)))
        else:
            numbers.append(int(p))

    return sorted(list(set(numbers)))


def interpret_config_file(file_path: str, file_encoding: str = None) -> dict:
    with open(file_path, "r", encoding=file_encoding) as f:
        lines = f.readlines()

    d = OrderedDict()

    for i, line in enumerate(lines):
        l = line.split(".pdf")

        if len(l) != 2:
            raise ValueError("Something is wrong with the config file at line: {0} -> {1}".format(i + 1, line))

        pdf_file_path = l[0] + ".pdf"
        page_numbers = interpret_page_numbers(l[1])

        d[pdf_file_path] = page_numbers

    return d


def extract_interesting_pdf_pages(pdf_dict: dict) -> list:
    pages = []
    for pdf_file_path, page_numbers in pdf_dict.items():
        pdf = PyPDF2.PdfFileReader(pdf_file_path)
        for i in page_numbers:
            p = i - 1
            try:
                pages.append(pdf.getPage(p))
            except:
                print("There is no page: {0} in pdf file: {1}, so it is skipped".format(p, pdf_file_path))
    return pages


def merge_pdf_pages(pdf_pages: list) -> PyPDF2.PdfFileWriter:
    pdf = PyPDF2.PdfFileWriter()
    for p in pdf_pages:
        pdf.addPage(p)
    return pdf


def split_and_merge():
    parser = argparse.ArgumentParser(description='Split then merge .pdf files')
    parser.add_argument('-i', '--input', required=True, type=str)
    parser.add_argument('-o', '--output', required=True, type=str)
    parser.add_argument('-e', '--encoding', default=None, type=str)

    args = vars(parser.parse_args())

    input_config_file_path = args["input"]
    file_encoding = args["encoding"]
    output_pdf_file_path = args["output"]

    pdf_dict = interpret_config_file(input_config_file_path, file_encoding)
    interesting_pdf_pages = extract_interesting_pdf_pages(pdf_dict)
    pdf = merge_pdf_pages(interesting_pdf_pages)

    with open(output_pdf_file_path, "wb") as f:
        pdf.write(f)

    print("[*] Final number of pages in the new document: {0}".format(pdf.getNumPages()))
    print("[*] Split and Merge is done! File is written to path: {0}".format(output_pdf_file_path))
