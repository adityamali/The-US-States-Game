import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
t = turtle.Turtle()
states = pandas.read_csv('50_states.csv')
correct = []

allstates = states.state.tolist()
while len(correct) <= 50:
    state_input = screen.textinput(title= f"{len(correct)}/50 States Correct" , prompt="Enter the name of a US state").title()
    for name in allstates:
        if state_input == name:
            x = int(states.loc[states['state'] == state_input].x)
            y = int(states.loc[states['state'] == state_input].y)
            correct.append(name)
            t.penup()
            t.hideturtle()
            t.goto(x, y)
            t.pendown()
            t.write(name)
        else:
            pass
    print(len(correct))


turtle.mainloop()
