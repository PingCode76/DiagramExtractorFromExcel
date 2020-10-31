from .diagram import * 

def drawDiagram():

    # Data in diagram
    nbRectangleInDiagram = countRectangleSection(data) #tab
    nbLabel = [1]

    x = -1000

    # foreach tab 
    for rectangle in nbRectangleInDiagram:
        #print(nbRectangleInDiagram) # 3 
        turtle.color('green')
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

        print(nbLabel)
        # for each rectangle, label
        t = -900 #x
        v = 800 #y
        for label in rectangle:
            turtle.color('black')
            turtle.up()
            turtle.goto(t,v)
            turtle.down()
            turtle.forward(150) #Forward turtle by 150 units ( width )
            turtle.left(90) #Turn turtle by 90 degree
            turtle.forward(100) #Forward turtle by 80 units ( height )
            turtle.left(90) #Turn turtle by 90 degree
            turtle.forward(150) #Forward turtle by 150 units ( width )
            turtle.left(90) #Turn turtle by 90 degree
            turtle.forward(100) #Forward turtle by 80 units ( height )
            turtle.left(90) #Turn turtle by 90 degree
            turtle.up()
            print("NbLabel")

            t = t +0 #x
            v = v - 150#y

            # Todo : add node 

            # first label 

            n = -900#x
            m = 825#y # 800 

            for nodes in rectangle:
                #node left
                turtle.goto(n,m)
                turtle.down()
                turtle.color('blue')
                turtle.circle(25) #50 good 
                #turtle.circle(50, 180)  #Trace un demi-cercle de rayon 70px
                turtle.up()

                #node right 
                turtle.goto(n+150,m) # n + width + rayon 
                turtle.down()
                turtle.color('blue')
                turtle.circle(25) #50 good 
                #turtle.circle(50, 180)  #Trace un demi-cercle de rayon 70px
                turtle.up()

                m = m - 150 #y
            

    #write("mon_texte",False,align='Left',font=('Arial',16,'normal')).


    # test 
    #turtle.color('green')
    #turtle.circle(120)