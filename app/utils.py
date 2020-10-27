import random
import xlrd

from random import randint

def readExcelDocument(file):
    workbook = xlrd.open_workbook(file)
    worksheet = workbook.sheet_by_name(SheetNameList[0])
    print( 'num_rows, num_cells', worksheet.nrows, worksheet.ncols )

def drawDiagram():
    data = {
        # line : id_function, Sequence, Operation Type, Description, Node1, Node2 
        "a":["1","1","Col","Lorem ipsum dolor sit amet, consectetur adipiscing elit","AX23","BY12"], 
        "b":["1","2","Tra","Donec fringilla, erat non suscipit faucibus, léo mi porta enim","BY12","CF43"],
        "c":["1","3","Tra","Proin quis tortor pharetra, pulvinar sem viate, lobortis","BY12","CG54"],
        "d":["1","4","Fer","Nulla vel mollis sem. Quisque consectetur maximus ornare.","CG54","TR89"],
        "e":["1","5","Fer","Aliquam erat volutpar. Curabitur et magna","CF43","DS09"],
        "f":["2","1","Col","Cras Suscipit hendrerit feugiat Viva porta sed consecta","AB56","KJ65"],
        "g":["2","2","Tra","Ipsum proin quis tortora maxima Aenean lobortis","KJ65","HF32"],
        "h":["2","3","Fer","Laculis euis mod In hac habitasse platea dictumus. Etiam dictum","HF32","ZX12"],
    }

    print('drawing diagram...')
