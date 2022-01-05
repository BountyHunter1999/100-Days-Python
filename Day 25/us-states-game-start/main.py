import pandas as pd
import turtle

FONT = ("Courier", 8, "normal")

df = pd.read_csv("50_states.csv")
df["state"] = df["state"].str.lower().str.replace(" ", "_")

screen = turtle.Screen()

image = "blank_states_img.gif"
screen.addshape(image)
screen.title("Name the States")

turtle.shape(image)

text = turtle.Turtle()
text.penup()
text.hideturtle()


def get_cor(data, answer):
    cleaned_answer = answer.lower().replace(" ", "_")
    row = data[data.state == cleaned_answer]
    if not row.empty:
        return int(row.x), int(row.y)
    else:
        return False


def write_text(state, x_y):
    text.goto(x_y)
    text.write(f"{state}", align="center", font=FONT)


states_found = []
while len(states_found) <= 50:
    answer_state = screen.textinput(title=f"{len(states_found)}/50 States Correct",
                                    prompt="What's another state's name?")

    cor = get_cor(df, answer_state)
    if cor:
        if answer_state not in states_found:
            write_text(answer_state, cor)
            states_found.append(answer_state)
        else:
            print("Already Found")
    elif answer_state == "exit":
        states_found_series = pd.Series(states_found)
        states_missed = df.state[~df.state.isin(states_found)]
        break
    else:
        print("Get ur GK checked bitch!")

print(states_missed, len(states_missed))
df_missed = pd.DataFrame(states_missed)
df_missed.to_csv("states_missed.csv")
