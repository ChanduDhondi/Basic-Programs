import turtle

""""Setting Screen"""
bg = turtle.Screen()
bg = turtle.bgcolor("light yellow")
bg = turtle.title("Drawing Shapes")

pen = turtle.Turtle()
pen.hideturtle()

pen.teleport(0,200)
pen.write("Drawing Shapes",False,"center")
pen.up()
pen.home()
pen.down()
pen.speed(6)

class Shapes():
    def __init__(self,pen_clr,fl_clr):
         self.pen_clr = pen_clr
         self.fl_clr = fl_clr
    
    def draw(self,sides):
         self.sides = sides
         pen.color(self.pen_clr)
         pen.fillcolor(self.fl_clr)
         
         for _ in range(self.sides):  
            pen.forward(50)
            pen.right(360/self.sides)
    def semi_circle(self):
        pen.up()
        pen.setpos(-100,100)
        pen.down()
        pen.color(self.pen_clr)
        pen.begin_fill()
        pen.fillcolor(self.fl_clr)
        pen.circle(50,90)
        pen.left(90)
        pen.forward(100)
        pen.setheading(270)
        pen.circle(50,90)
        pen.end_fill()
          
shape = Shapes('green','purple')
shape.draw(4)
shape.semi_circle()


turtle.done()




        

        


        


