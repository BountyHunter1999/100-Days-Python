from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.01
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(text_count, text="00:00")
    check.config(text="")
    text.config(text="Timer", fg=GREEN)
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    count_sec = 0

    if reps % 2 == 1:
        count_sec = work_sec
        text.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        count_sec = long_break_sec
        checks = "✔" * math.floor(reps / 2)
        check.config(text=checks)
        text.config(text="Break", fg=RED)
    else:
        count_sec = short_break_sec
        text.config(text="Break", fg=PINK)
        checks = "✔" * math.floor(reps / 2)
        check.config(text=checks)
        print(f"checks: {len(checks)}: {checks}")

    count_down(count_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    minute = math.floor(count / 60)
    sec = count % 60

    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(text_count, text=f"{minute}:{sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
# window.minsize(width=300, height=300)
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
text_count = canvas.create_text(101, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"), )
canvas.grid(row=1, column=1)

text = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 50))
text.grid(row=0, column=1)


start = Button(text="start", bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 10, "bold"), command=start_timer)
start.grid(row=2, column=0)

check = Label(fg=GREEN, bg=YELLOW)
check.grid(row=3, column=1)

reset = Button(text="reset",  bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 10, "bold"), command=reset_timer)
reset.grid(row=2, column=2)


window.mainloop()
