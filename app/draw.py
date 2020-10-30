from .diagram import * 

def drawDiagram():

    ########## drawing Diagram ###############

    # Create nb Rectangle
    nbRectangleInDiagram = countRectangleSection(data) #count la nouvelle variable 

    # boucle nbRectangleInDiagram for create Rectangle
    i = 0 
    while i < nbRectangleInDiagram:
        #print(nbRectangleInDiagram) # 3 

        if i == 0:
            turtle.up()
            turtle.goto(-1000, 400)
            turtle.down()
            turtle.forward(300) #Forward turtle by 150 units ( width )
            turtle.left(90) #Turn turtle by 90 degree
            turtle.forward(600) #Forward turtle by 80 units ( height )
            turtle.left(90) #Turn turtle by 90 degree
            turtle.forward(300) #Forward turtle by 150 units ( width )
            turtle.left(90) #Turn turtle by 90 degree
            turtle.forward(600) #Forward turtle by 80 units ( height )
            turtle.left(90) #Turn turtle by 90 degree

        if i == 1:
            turtle.up()
            turtle.goto(-600, 400)
            turtle.down()
            turtle.forward(300) #Forward turtle by 150 units ( width )
            turtle.left(90) #Turn turtle by 90 degree
            turtle.forward(600) #Forward turtle by 80 units ( height )
            turtle.left(90) #Turn turtle by 90 degree
            turtle.forward(300) #Forward turtle by 150 units ( width )
            turtle.left(90) #Turn turtle by 90 degree
            turtle.forward(600) #Forward turtle by 80 units ( height )
            turtle.left(90) #Turn turtle by 90 degree


        if i == 2:
            turtle.up()
            turtle.goto(-200, 400)
            turtle.down()
            turtle.forward(300) #Forward turtle by 150 units ( width )
            turtle.left(90) #Turn turtle by 90 degree
            turtle.forward(600) #Forward turtle by 80 units ( height )
            turtle.left(90) #Turn turtle by 90 degree
            turtle.forward(300) #Forward turtle by 150 units ( width )
            turtle.left(90) #Turn turtle by 90 degree
            turtle.forward(600) #Forward turtle by 80 units ( height )
            turtle.left(90) #Turn turtle by 90 degree

        print(i)
        i = i + 1 
        

        


    #write("mon_texte",False,align='Left',font=('Arial',16,'normal')).


    # test 
    #turtle.color('green')
    #turtle.circle(120)