## this is my etch a sketch 

from turtle import Turtle, Screen 

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.back(10)

def move_clockwise():
    tim.right(10)

def move_counter():
    tim.left(10)    

def clear():
    tim.reset()


screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=move_counter)
screen.onkey(key='d', fun=move_clockwise)
screen.onkey(key='c', fun=clear)


screen.exitonclick()

## we don't immeditley add the () otherwise it will trigger asap 