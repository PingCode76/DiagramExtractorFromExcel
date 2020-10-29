import random
import xlrd
import turtle
from turtle import *

from random import randint

import svgwrite
from .SvgTurtle import SvgTurtle
#from .utils import drawDiagram
#import svgTurtle

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

    #write("mon_texte",False,align='Left',font=('Arial',16,'normal')).

    print(turtle.heading())  #Affiche 0.0 : le crayon pointe vers le point bleu : Est
    turtle.left(90)  #Pointe vers le point jaune : Nord
    turtle.right(270)  #Pointe vers le point vert : Ouest
    turtle.setheading(0)  #Pointe de nouveau vers le point bleu
    turtle.setheading(-90)  #Pointe à l'opposé du point jaune : Sud
    print(turtle.heading())  #Affiche '270.0'

    #diagram = turtle.getscreen()

    # try to export diagram in eps or svg with this function 
    #diagram.getcanvas().postscript(file="diagram.eps")
    #turtle.bye()
    #turtle.mainloop()
    #wn.mainloop()

def encode_file(draw_func, filename, size):
    drawing = svgwrite.Drawing(filename, size=size)
    drawing.add(drawing.rect(fill='white', size=("100%", "100%")))
    t = SvgTurtle(drawing)
    Turtle._screen = t.screen
    Turtle._pen = t
    draw_func()
    drawing.save()
    #turtle.bye()


def exportDraw():
    encode_file(drawDiagram, 'diagram.svg', size=("500px", "500px"))
    print('Draw exported in svg.')

exportDraw()

