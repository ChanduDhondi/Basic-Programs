import turtle
import random as r

""""Setting Screen"""
bg = turtle.Screen()
bg = turtle.bgcolor("light yellow")
bg = turtle.title("Drawing Shapes")

pen = turtle.Turtle()
pen.hideturtle()

pen.teleport(0,250)
pen.write("Drawing Shapes",False,"center")
pen.up()
pen.home()
pen.down()
pen.speed(0)

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
         pen.end_fill()

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
    
    def mapping_lines(self):
          pen.clear()
          pen.color("orange")
          for y1 in range(200,-200,-40):
               for y2 in range(200,-200,-40):
                    pen.up()
                    pen.goto(-200,y1)
                    pen.down()
                    pen.dot("green")
                    pen.goto(200,y2)
                    pen.dot("green")

    def rotating_circles(self):
         pen.clear()
         bg = turtle.bgcolor("black")
         pen.home()
         color = ['violet','indigo','blue','green','yellow','orange','red']
         for x in range(85):
               pen.color(r.choice(color))
               pen.left(x/10)
               pen.circle(100)
     
    def rotating_squres(self):
         pen.clear()
         bg = turtle.bgcolor("black")
         pen.home()
         color = ['violet','indigo','blue','green','yellow','orange','red']
         for x in range(88):
              for _ in range(4):
                   pen.color(r.choice(color))
                   pen.forward(100)
                   pen.left(90)
              pen.left(x)               
shape = Shapes('green','purple')
# shape.draw(5)
# shape.semi_circle() 
# shape.mapping_lines()
shape.rotating_circles()
shape.rotating_squres()


turtle.done()




        

        


        


