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
LONG_BREAK_MIN = 35
reps = 0
rep_string = ""
flag = 1


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global rep_string, reps, flag
    rep_string = ""
    reps = 0
    flag = 0
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text=rep_string)
    title_label.config(text="Timer", fg=GREEN)
    # instead of using flags to stop our timer
    # use window.after_cancel(timer), where timer = window.after() in count_down function


# ---------------------------- TIMER MECHANISM ------------------------------- #
# rep 1 : work 25 min
# rep 2 : break 5 min
# rep 3 : work 25 min
# rep 4 : break 5 min
# rep 5 : work 25 min
# rep 6 : break 5 min
# rep 7 : work 25 min
# rep 8 : break 35 min
# 2hrs 30 min, repeat rep 9, 10....

def start_timer():
    global reps, rep_string, flag
    flag = 1
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    rep_checks = "✔"
    rep_pause = "⏸️"

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
        rep_string = rep_string+rep_pause+rep_pause
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
        rep_string = rep_string + rep_pause
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
        rep_string = rep_string + rep_checks


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global flag
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if flag:
        if count_sec < 10:
            canvas.itemconfig(timer_text, text=f"{count_min}:0{count_sec}")
        else:
            canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

        if count > 0:
            window.after(1000, count_down, count - 1)
        else:
            check_marks.config(text=rep_string)
            start_timer()
    else:
        return


# ---------------------------- UI SETUP ------------------------------- #
# window setup
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_label.grid(column=1, row=0)

# canvas setup
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=canvas_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=2)
window.mainloop()
