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

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state in states_list:
        answer_row = data[data.state == answer_state]
        answer_xcor = int(answer_row.x)
        answer_ycor = int(answer_row.y)
        state_turtle.goto(answer_xcor, answer_ycor)
        state_turtle.write(answer_state, align="center", font=("Arial", 8, "bold"))
        correct_guesses.append(answer_state)
    else:
        pass

    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in correct_guesses]
        # for state in states_list:
        #     if state not in correct_guesses:
        #         missing_states.append(state)

        states_to_learn = {
            "states": missing_states
        }

        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("States_to_learn.csv")
        break


