import turtle as t
import random as r
class Piton:
    def __init__(self):
        self.body=[]
        self.create_snake()
        self.head=self.body[0]
        self.n=3
    def create_snake(self):
        self.body = [t.Turtle(shape="square"), t.Turtle(shape="square"), t.Turtle(shape="square")]
        self.head=self.body[0]
        self.head.color("DarkOliveGreen")
        self.body[1].color("DarkOliveGreen")
        self.body[2].color("DarkOliveGreen")
        self.body[0].penup()
        self.body[1].penup()
        self.body[2].penup()
        x, y = self.head.position()
        self.body[1].goto(x - 10, y)
        self.body[2].goto(x - 20, y)
    def add_head(self):
        self.n += 1
        self.body.append(t.Turtle(shape="square"))
        self.body[self.n - 1].color("DarkOliveGreen")
        self.body[self.n - 1].penup()
        self.body[self.n-1].goto(self.body[self.n-2].pos())
    def move(self):
        x, y=self.head.position()
        self.head.forward(20)
        for i in range(1, self.n):
            x1, y1 = self.body[i].pos()
            self.body[i].goto(x, y)
            x = x1
            y = y1
    def right(self):
        if self.head.heading()!=180:
            self.head.seth(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

class Fruit:
    def __init__(self):
        self.fruit = t.Turtle(shape="circle")
        self.fruit.color("purple")
        self.fruit.penup()
        xf = r.choice(range(-380, 381, 20))
        yf = r.choice(range(-340, 341, 20))
        self.fruit.goto(xf, yf)
    def move(self):
        xf = r.choice(range(-380, 381, 20))
        yf = r.choice(range(-340, 341, 20))
        self.fruit.goto(xf, yf)
class Score:
    def __init__(self):
        self.scor=0
        self.text=t.Turtle()
        self.text.penup()
        self.text.hideturtle()
        self.text.color("white")
        self.text.goto(0,371)
        self.text.write(f"Score: {self.scor}", False, "center", font=("Arial", 16, "normal"))

    def grow(self):
        self.text.clear()
        self.scor+=1
        self.text.goto(0, 371)
        self.text.write(f"Score: {self.scor}", False, "center", font=("Arial", 16, "normal"))