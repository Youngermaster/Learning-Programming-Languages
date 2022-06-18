import openpyxl as xl
import os
from copy import copy

if __name__ == "__main__":
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    DOCUMENT_PATH = os.path.join(ROOT_DIR, 'documents')

    # opening the source excel file
    filename = os.path.join(DOCUMENT_PATH, 'trading.xlsx')
    wb1 = xl.load_workbook(filename)
    ws1 = wb1.worksheets[0]

    # opening the destination excel file
    filename1 = os.path.join(DOCUMENT_PATH, 'test.xlsx')
    wb2 = xl.load_workbook(filename1)
    ws2 = wb2.active

    # calculate total number of rows and
    # columns in source excel file
    mr = ws1.max_row
    mc = ws1.max_column

    # copying the cell values from source
    # excel file to destination excel file
    for row in ws1.rows:
        for cell in row:
            new_cell = ws2.cell(row=cell.row, column=cell.col_idx,
                                value=cell.value)
            if cell.has_style:
                new_cell.font = copy(cell.font)
                new_cell.border = copy(cell.border)
                new_cell.fill = copy(cell.fill)
                new_cell.number_format = copy(cell.number_format)
                new_cell.protection = copy(cell.protection)
                new_cell.alignment = copy(cell.alignment)

    # saving the destination excel file
    wb2.save(str(filename1))
