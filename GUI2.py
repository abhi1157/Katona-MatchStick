
'''

ABHINAV GUPTA
2015B4A70602P

'''

import turtle
turtle.speed(10)
def gui(state,size,path):

    turtle.bgcolor("yellow")

    #arr=[1,1,1,0,1,0,0,0,0,1,1,0,0,1,1,1,0,0,0,1,1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,1,0,0,0,1]
    arr=state
    so=size
    gu=turtle.Turtle()
    start_pos=(-50,50)

    #print(path)
    turtle.penup()
    turtle.setx(start_pos[0])
    turtle.sety(start_pos[1])
    turtle.pendown()
    for j in range(so+1):
        for i in range(so):
            if(arr[j*so+i] is 1):
                turtle.forward(30)
                turtle.dot()
            else:
                turtle.penup()
                turtle.forward(30)
                turtle.pendown()


        #end
        turtle.penup()
        turtle.setx(start_pos[0])
        turtle.sety(start_pos[1]-30*(j+1))
        turtle.pendown()



    turtle.penup()
    turtle.setx(start_pos[0])
    turtle.sety(start_pos[1])
    turtle.pendown()


    turtle.right(90)

    for j in range(0,so+1):

        for i in range(so):
            if(arr[(j+so+1)*so+i] is 1):
                turtle.forward(30)
                turtle.dot()
            else:
                turtle.penup()
                turtle.forward(30)
                turtle.pendown()


        #end
        turtle.penup()
        turtle.setx(start_pos[0]+30*(j+1))
        turtle.sety(start_pos[1])
        turtle.pendown()

    turtle.left(90)
    turtle.color("yellow")

    for i in range(len(path)):


        if(path[i]<=so*(so+1)):
            xc=(path[i]-1)%so
            yc=(int)(path[i]-1)//so
            turtle.penup()
            turtle.setx(start_pos[0]+30*xc)
            turtle.sety(start_pos[1]-30*yc)
            turtle.pendown()
            turtle.forward(30)
            #turtle.dot()


    turtle.right(90);

    for i in range(len(path)):


        if(path[i]>so*(so+1)):
            yc=((path[i]-so*(so+1))-1)%so
            xc=((path[i]-so*(so+1))-1)//so
            turtle.penup()
            turtle.setx(start_pos[0]+30*xc)
            turtle.sety(start_pos[1]-30*yc)
            turtle.pendown()
            turtle.forward(30)
            #turtle.dot()






    turtle.getscreen()._root.mainloop()
