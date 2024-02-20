from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps = 0
timer = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
    timer_label.config(text="Timer")
    tick_label.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN*60
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        countdown(work_sec)
        timer_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfigure(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        checks = ""
        work_sessions = math.floor(reps/2)
        for n in range(work_sessions):
            checks += "✔️"
        tick_label.config(text=checks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=150, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN,bg=YELLOW, font=(FONT_NAME,45, "bold"))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_image)
timer_text = canvas.create_text(100,130, text="00:00",fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button= Button(text="Start",fg="black", bg=GREEN, command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",fg="black", bg=GREEN, command=reset_timer)
reset_button.grid(row=2,column=2)

tick_label = Label(bg=YELLOW,fg="green")
tick_label.grid(row=3, column=1)

window.mainloop()