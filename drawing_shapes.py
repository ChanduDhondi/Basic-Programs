import turtle


#setting background

wn = turtle.Screen()
wn.bgcolor("light yellow")
wn.title("Drawing Shapes")

#using turtle function

pen = turtle.Turtle()
pen.color("yellow")
pen.begin_fill()
pen.fillcolor("purple")
pen.down()

# drawing Square

for i in range(4):
    pen.forward(50)
    pen.right(90)

turtle.done()

# drawing circle 
pen.setpos(-100,+100)

pen.circle(100)

    
pen.end_fill()



turtle.done()





