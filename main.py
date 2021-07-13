from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    pass


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start():
    pass


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 134, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

title_label = Label(text="Timer", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=2, row=1)

check_mark = Label(text="✔", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
check_mark.grid(column=2, row=4)

start_button = Button(text="Start", command=start)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=3, row=3)

window.mainloop()
