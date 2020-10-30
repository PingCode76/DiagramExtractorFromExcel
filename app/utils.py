import random
import os.path
import os
import shutil
import xlrd
import turtle
from turtle import *
#from Tkinter import *

from random import randint

import svgwrite
from .SvgTurtle import SvgTurtle
from .diagram import *

def encode_file(draw_func, filename, size):
    drawing = svgwrite.Drawing(filename, size=size)
    #drawing.add(drawing.rect(fill='white', size=("100%", "100%")))
    #drawing.add(drawing.line((440, 280), (1180, 280), stroke='#f00', stroke_width=7))
    #drawing.__init__(filename=u'static/noname.svg')
    t = SvgTurtle(drawing)
    Turtle._screen = t.screen
    Turtle._pen = t
    draw_func()
    drawing.save()

    # The SVG file have a form, but this form is not displaying in webpage


def exportDraw():
    encode_file(drawDiagram, 'app/static/img/diagram.svg', size=("500px", "500px"))
    #shutil.move('./' + os.path.abspath(os.path.dirname(__file__)) + '/diagram.svg', 'static/img/diagram.svg')
    #print('Draw exported in svg.')

exportDraw()

