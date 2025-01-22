import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data["state"]
states_list = states.to_list()
guessed_list = []
x_list = []
y_list = []
def create_csv():
    learn_state = [state for state in states_list if state not in guessed_list]
    for state in learn_state:
        r_data = data[data.state == state]
        x = r_data.x.item()
        x_list.append(x)
        y = r_data.y.item()
        y_list.append(y)

    learn_dic = {
        "state": learn_state,
        "x": x_list,
        "y": y_list
    }
    learn_data_frame = pandas.DataFrame(learn_dic)
    learn_data_frame.to_csv("learn_state")
    print(learn_data_frame)
while len(guessed_list) < 50:
    answer = screen.textinput(f"{len(guessed_list)}/50 Guess the name of state", "What is the name of the state?").title()

    if answer == "Exit":
       create_csv()
       break

    if answer in states_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row_data = data[data.state == answer]
        t.goto(row_data.x.item(), row_data.y.item())
        t.write(answer)
        guessed_list.append(answer)

if len(guessed_list) >= 50:
    create_csv()






