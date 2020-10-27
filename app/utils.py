import random
import xlrd
import numpy as np
#import turtle
from random import randint

#TODO:  create a function for save excel document ( https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/ )

def readExcelDocument():
    workbook = xlrd.open_workbook('read_excel_file_with_python.xlsx')
    worksheet = workbook.sheet_by_name(SheetNameList[0])
    print( 'num_rows, num_cells', worksheet.nrows, worksheet.ncols )



"""
def draw_random_line():
    turtle.penup()
    turtle.goto(-200,-200)
    turtle.setheading(45)
    turtle.pendown()

    while True : 
        # une couleur, un angle et une distance aléatoires...
        rgb_r = randint(0,255) 
        rgb_g = randint(0,255) 
        rgb_b = randint(0,255) 
        angle = randint(-10,10)
        nbpas = randint(1,10) 
        # ... pour comamnder la tortue
        turtle.color(rgb_r,rgb_g, rgb_b)
        turtle.left(angle)
        turtle.forward(nbpas)
"""

