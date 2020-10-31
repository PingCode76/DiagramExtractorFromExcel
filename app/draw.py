from .diagram import * 

def drawDiagram():

    # Data in diagram
    nbRectangleInDiagram = countRectangleSection(data) #tab
    nbLabelInRectangle = [3] #count for nb label in Rectangle
    

    x = -1000
    # foreach tab 
    for rectangle in nbRectangleInDiagram:
        #print(nbRectangleInDiagram) # 3 
        turtle.color('green')
        turtle.up()
        turtle.goto(x, 400)
        turtle.down()

        turtle.fillcolor('grey') # background color 
        turtle.begin_fill() # begin color 

        turtle.forward(300) #Forward turtle by 150 units ( width )
        turtle.left(90) #Turn turtle by 90 degree
        turtle.forward(600) #Forward turtle by 80 units ( height )
        turtle.left(90) #Turn turtle by 90 degree
        turtle.forward(300) #Forward turtle by 150 units ( width )
        turtle.left(90) #Turn turtle by 90 degree
        turtle.forward(600) #Forward turtle by 80 units ( height )
        turtle.left(90) #Turn turtle by 90 degree

        turtle.end_fill() # end color 

        x = x + 400

        # for each rectangle, label
        t = -900 #x
        v = 800 #y

        for label in rectangle:
            turtle.color('green') #color 
            turtle.up()
            turtle.goto(t,v) # pos
            turtle.down()

            turtle.fillcolor('white') # background color 
            turtle.begin_fill() # begin color 

            turtle.forward(150) #Forward turtle by 150 units ( width )
            turtle.left(90) #Turn turtle by 90 degree
            turtle.forward(100) #Forward turtle by 80 units ( height )
            turtle.left(90) #Turn turtle by 90 degree
            turtle.forward(150) #Forward turtle by 150 units ( width )
            turtle.left(90) #Turn turtle by 90 degree
            turtle.forward(100) #Forward turtle by 80 units ( height )
            turtle.left(90) #Turn turtle by 90 degree

            turtle.end_fill() # end color 
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

                turtle.color('blue') # color 
                turtle.fillcolor('blue')
                
                turtle.begin_fill()
                turtle.circle(25) #50 good 
                turtle.end_fill() 
                
                turtle.up()

                #node right 
                turtle.goto(n+150,m) # n + width + rayon 
                turtle.down()

                turtle.color('blue')
                turtle.fillcolor('blue')

                turtle.begin_fill()
                turtle.circle(25) #50 good 
                turtle.end_fill() 

                turtle.up()

                m = m - 150 #y
            

    #write("mon_texte",False,align='Left',font=('Arial',16,'normal')).


    # test 
    #turtle.color('green')
    #turtle.circle(120)