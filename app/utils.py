import random
import xlrd

from random import randint

def readExcelDocument(file):
    workbook = xlrd.open_workbook(file)
    worksheet = workbook.sheet_by_name(SheetNameList[0])
    print( 'num_rows, num_cells', worksheet.nrows, worksheet.ncols )

def drawDiagram():
    print('drawing diagram...')
