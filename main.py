from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    timer_label.config(text="Timer")
    check.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # work seconds for odd number reps
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK, bg=YELLOW)
    else:
        count_down(work_sec)
        timer_label.config(text="WORK", fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    # Counting the minutes and seconds in correct format to visualize
    count_min = math.floor(count / 60)
    count_sec = (count % 60)
    # To format the second timer in '00:00' format in seconds place
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for x in range(work_sessions):
            mark += "✔"
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

# Setting up the window
window = Tk()
window.title("POMODORO")
window.config(padx=110, pady=60, bg=YELLOW)

# Setting up the canvas on the window
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Making the start button
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

# Making the Timer Label
timer_label = Label(text="Timer", font=(FONT_NAME, 40, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# Making the check mark label
check = Label(fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)

# Making the Reset button
reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()
