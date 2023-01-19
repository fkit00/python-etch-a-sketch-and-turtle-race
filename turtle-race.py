from turtle import Turtle, Screen 
import random 

is_race_on= False

screen = Screen()
screen.setup(width = 500, height= 400)
user_bet = screen.textinput("Welcome to  Turtle racing","Please make a bet on which turtle you think will win the race - please enter a colour")
colours= ["red", "orange","yellow","green","blue","purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
print(user_bet)

if user_bet:
    is_race_on = True

for n in range(0,6):
   
    turtle = Turtle(shape="turtle")
    turtle.color(colours[n])
    turtle.penup() 
    turtle.goto(x=-230,y=y_positions[n])


while is_race_on:
    random.randint(0,10)





screen.exitonclick()