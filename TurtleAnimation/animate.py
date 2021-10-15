from turtle import *
t = Turtle()

screen = Turtle().screen
screen.bgcolor("black")
screen.setup(width=1200, height=800)
t.speed(0)
t.width(4)
t.hideturtle()
t.color("white")
t.penup()
t.backward(325)
t.right(90)
t.pendown()
t.circle(325)
t.penup()
t.left(90)
t.forward(325)
t.pendown()

def draw():
  for i in range(7):
    t.circle(160)
    t.right(60)
    t.color(colors[i])

colors = ["pink", "purple", "cyan", "green", "yellow", "orange", "red"]

def erase():
  for i in range(6):
    t.width(5)
    t.circle(160)
    t.right(60)
    t.color("black")

while True:
  draw()
  erase()
  
  
