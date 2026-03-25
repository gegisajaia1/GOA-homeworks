from turtle import *

#i want to paint a house 
speed(5) 
width(7) 
color("blue")
forward(200) 
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90) 
#end of square

#drawing a door

forward(70)
color("brown") 
begin_fill()
left(90) 
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120) 
end_fill()

penup()
goto(200, 200)
pendown() 

color("red") 
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
 
penup()
color("blue")
left(30)
forward(30)
left(90)
forward(30)
pendown() 
color("cyan")
begin_fill()
forward(30)
right(90)
forward(30) 
right(90) 
forward(30) 
right(90)
forward(30)
end_fill()
 
penup() 
begin_fill()
right(90)
forward(110)
pendown()
forward(30)
right(90) 
forward(30) 
right(90) 
forward(30) 
right(90) 
forward(30) 
end_fill()

exitonclick() 