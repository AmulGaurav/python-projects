import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# reps variable is to hold the total count of work and break sessions
reps = 0

timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    # This method is used to stop after function
    window.after_cancel(timer)

    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")

    # Reset reps count to 0
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    # reps increased by 1 after every session
    global reps
    reps += 1

    # Converting session time to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # check for long break session
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    # check for short break session
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    # check for work session
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count // 60
    count_sec = count % 60

    # check if seconds count is less than 10 to show like this 09, 08.... 00
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # check if minutes count is less than 10 to show like this 09, 08.... 00
    if count_min < 10:
        count_min = f"0{count_min}"

    # To modify timer count use itemconfig method in canvas where first argument is the thing which needs to be modified and the second one holds its value
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        # Storing after method in timer variable to give it a ID. So, we can cancel it at the time of reset
        global timer
        timer = window.after(1000, count_down, count - 1)
        
    else:
        # Calling start function after every session is completed
        start_timer()

        # Adding one check mark after every completed work session
        if reps % 2 == 0:
            check_label["text"] += "✔️"

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW)
# Storing img location in variable, tomato_img.
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 125, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Label
timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

# Button
start_button = tkinter.Button(text="Start", bg=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text="Reset", bg=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

check_label = tkinter.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
check_label.grid(row=3, column=1)

window.mainloop()