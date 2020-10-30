from .diagram import * 

def drawDiagram():

    ########## drawing Diagram ###############

    # Create nb Rectangle
    nbRectangleInDiagram = countRectangleSection(data) #tab

    # boucle nbRectangleInDiagram for create Rectangle
    #i = 0 
    #while i < nbRectangleInDiagram:

    x = -1000

    # foreach tab 
    for rectangle in nbRectangleInDiagram:
        #print(nbRectangleInDiagram) # 3 

        turtle.up()
        turtle.goto(x, 400)
        turtle.down()
        turtle.forward(300) #Forward turtle by 150 units ( width )
        turtle.left(90) #Turn turtle by 90 degree
        turtle.forward(600) #Forward turtle by 80 units ( height )
        turtle.left(90) #Turn turtle by 90 degree
        turtle.forward(300) #Forward turtle by 150 units ( width )
        turtle.left(90) #Turn turtle by 90 degree
        turtle.forward(600) #Forward turtle by 80 units ( height )
        turtle.left(90) #Turn turtle by 90 degree
        x = x + 400

    #write("mon_texte",False,align='Left',font=('Arial',16,'normal')).


    # test 
    #turtle.color('green')
    #turtle.circle(120)