import turtle
from turtle import *
import random as r
import time
from clase import Piton, Fruit, Score
scr=Screen()
scr.title("Snake")
def joc(turt, scor):
    scor.text.clear()
    scr.onkey(None, "space")
    sarpe = Piton()
    turt.clear()
    scr.onkey(fun=sarpe.up,key="w")
    scr.onkey(fun=sarpe.right,key="d")
    scr.onkey(fun=sarpe.down,key="s")
    scr.onkey(fun=sarpe.left,key="a")
    fruit=Fruit()
    scr.tracer(0)
    broks=1
    scor=Score()
    while broks:
        scr.update()
        time.sleep(0.04)
        sarpe.move()

        xi, yi = round(sarpe.head.xcor()), round(sarpe.head.ycor())
        xf, yf = round(fruit.fruit.xcor()), round(fruit.fruit.ycor())
        if xi>420 or yi > 360 or xi<-420 or yi<-360:
            broks=0
            break
        for f in range(1,sarpe.n):
            xp, yp = round(sarpe.body[f].xcor()), round(sarpe.body[f].ycor())
            if xi==xp and yi==yp:
                broks=0
                break




        if xi==xf and yi==yf:
            scor.grow()
            fruit.move()
            sarpe.add_head()
    if broks==0:
        fruit.fruit.hideturtle()
        scor.text.clear()
        for i in sarpe.body:
            i.hideturtle()
        del fruit
        del sarpe
        gameover=turtle.Turtle()
        gameover.hideturtle()
        gameover.color("black")
        gameover.penup()
        gameover.write("GAME OVER",align="center", font=("Impact",160, "bold"))
        scor.text.color("purple")
        scor.text.goto(0,-40)
        scor.text.write(f"SCOR FINAL: {scor.scor}", font=("Impact", 50, "normal"), align="center")
        scr.onkey(key="space", fun=lambda:joc(gameover, scor))
        scr.onkey(key="Escape", fun=turtle.bye)

scr.screensize(400,400)
scr.bgcolor("DarkGreen")
filler = turtle.Turtle()
filler.hideturtle()
filler.speed(0)
filler.color("OliveDrab1")       # Fill color

# Fill the large rectangle
filler.penup()
filler.goto(-430, 370)     # Top-left corner
filler.pendown()
filler.begin_fill()
filler.goto(430, 370)      # Top-right
filler.goto(430, -370)     # Bottom-right
filler.goto(-430, -370)    # Bottom-left
filler.goto(-430, 370)     # Back to start
filler.end_fill()

scr.listen()
title=turtle.Turtle()
title.color("black")
title.penup()
title.hideturtle()
scor= Score()
title.write("SNAKE",align="center", font=("Impact",140, "bold"))
scr.onkey(key="space", fun=lambda:joc(title,scor ))
scr.exitonclick()









