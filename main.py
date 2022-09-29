from turtle import Turtle, Screen
import pandas

turtle = Turtle()
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_turtle = Turtle()
state_turtle.penup()
state_turtle.hideturtle()

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()

correct_guesses = []

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/{len(states_list)} States Correct",
                                    prompt="What's another state's name?")
    if answer_state.title() in states_list:
        answer_row = data[data.state == answer_state.title()]
        answer_xcor = int(answer_row.x)
        answer_ycor = int(answer_row.y)
        state_turtle.goto(answer_xcor, answer_ycor)
        state_turtle.write(answer_state.title(), align="center", font=("Arial", 8, "bold"))
        correct_guesses.append(answer_state.title())
    else:
        pass

    if len(correct_guesses) == len(states_list):
        game_is_on = False

screen.exitonclick()
