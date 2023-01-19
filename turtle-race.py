from turtle import Turtle, Screen 
import random 

is_race_on= False

screen = Screen()
screen.setup(width = 500, height= 400)
user_bet = screen.textinput("Welcome to  Turtle racing","Please make a bet on which turtle you think will win the race - please enter a colour")
colours= ["red", "orange","yellow","green","blue","purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles=[]
print(user_bet)


for n in range(0,6):
   
    turtle = Turtle(shape="turtle")
    turtle.color(colours[n])
    turtle.penup() 
    turtle.goto(x=-230,y=y_positions[n])
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_colour=turtle.pencolor()
            if winning_colour== user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner")
            else:
                print(f"you've lost! {winning_colour} won!")
        random_distance= random.randint(0,10)
        turtle.forward(random_distance)





screen.exitonclick()