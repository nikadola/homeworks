from turtle import *

#we want to paint a house 

#step1: draw a square

speed(30)

width(7)
color("red")

begin_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

end_fill()

#end of square

#draw a door

forward(70)

color("blue")

begin_fill()

left(90)
forward(100)

right(90)
forward(60)

right(90)
forward(100)

end_fill()

#end of door

penup()

goto(200, 200)
pendown()

color("yellow")

begin_fill()

right(150)
forward(200)

left(120)
forward(200)

end_fill()

#drow a window
color("green")

begin_fill()

penup()

goto(20, 120)

pendown()

left(120)
forward(30)

left(90)
forward(30)

left(90)
forward(30)

left(90)
forward(30)

end_fill()

penup()

goto(180, 120)

pendown()

begin_fill()

right(90)
forward(30)

right(90)
forward(30)

right(90)
forward(30)

right(90)
forward(30)

end_fill()


exitonclick()


