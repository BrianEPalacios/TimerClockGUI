import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------------------------------- TIMER RESET -------------------------------------------------- #

# ------------------------------------------------------ TIMER MECHANISM -------------------------------------------- #
def start_timer():
    count_down(302)


# ------------------------------------------------- COUNTDOWN MECHANISM ---------------------------------------------- #
def count_down(count):
    # gives us the number of minutes
    count_minutes = count // 60
    # getting the number of seconds
    count_seconds = count % 60

    if count_seconds == 0:
        count_seconds = "00"
    elif count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    # This is changing the text in the tomato, the 00:00
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# -------------------------------------------------------- UI SETUP ------------------------------------------------- #
# Creating Window
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Creating canvas
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# Creating photo image for canvas.create_image
tomato_img = tk.PhotoImage(file="tomato.png")

# Add image to canvas | Coordinates required | image required
canvas.create_image(100, 112, image=tomato_img)
# Adding text
timer_text = canvas.create_text(100, 130, text=f"00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(row=1, column=1)

# ----------- Create Timer Label ------------ #
timer_label = tk.Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)

# ---------- Create start and reset buttons ------#
start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", highlightthickness=0)
reset_button.grid(row=2, column=2)

# ------- Create Checkmark -------#
checkmark_label = tk.Label(text="🍙", font=30, bg=YELLOW)
checkmark_label.grid(row=3, column=1)

# Keeps window open
window.mainloop()
