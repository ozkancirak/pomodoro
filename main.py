import tkinter
from tkinter import *
import pygame
import math


# ----------------------------MP3 Function------------------------------ #
def play_mp3(file_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


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
program_value = 0
timer = None
Padoru = r"Z:\MY PYTHON JOURNEY\pomodoroprogram\padorupadoru.mp3"

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    if timer is not None:
        window.after_cancel(str(timer))
    Label_Timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(Timer_text, text="00:00")
    Label_Checkmark.config(text="")
    global reps
    reps = 0
    global program_value
    program_value = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global program_value
    if program_value == 0:
        global reps
        reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            count_down(long_break_sec)
            Label_Timer.config(text="Long Break", fg="white")
        elif reps % 2 == 0:
            count_down(short_break_sec)
            Label_Timer.config(text="Short Break", fg="pink")
        else:
            count_down(work_sec)
            Label_Timer.config(text="Work", fg="red")
    program_value = 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    global program_value
    global Padoru

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(Timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        program_value = 0
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        Label_Checkmark.config(text=marks)
        window.attributes('-topmost', True)
        play_mp3(r"Z:\MY PYTHON JOURNEY\pomodoroprogram\padorupadoru.mp3")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Work&Break")
window.config(padx=100, pady=50, bg=YELLOW)

Label_Timer = tkinter.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), highlightthickness=0, bg=YELLOW)
Label_Timer.grid(row=2, column=2)
Label_Checkmark = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
Label_Checkmark.grid(row=5, column=2)
button_start = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(row=4, column=1)
button_reset = tkinter.Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(row=4, column=3)

canvas = Canvas(width=189, height=224, bg=YELLOW, highlightthickness=0)
Tomato_Img = PhotoImage(file="zc.png")
canvas.create_image(100, 112, image=Tomato_Img)
Timer_text = canvas.create_text(100, 130, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=3, column=2)


window.mainloop()
