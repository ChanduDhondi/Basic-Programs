import turtle

""""Setting Screen"""
bg = turtle.Screen()
bg = turtle.bgcolor("light yellow")
bg = turtle.title("Drawing Shapes")

pen = turtle.Turtle()


class Shape():

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

square = Shape('black','green')
square.draw(8)
square.draw(7)
square.draw(6)
square.draw(5)
square.draw(4)
square.draw(3)
square.draw(2)

turtle.done()




        

        


        


