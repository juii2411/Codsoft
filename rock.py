import tkinter as tk
import random

# Game logic
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    # Update the GUI labels
    user_choice_label.config(text=f"You chose: {user_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)
    score_label.config(text=f"Score -> You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="You chose: ")
    computer_choice_label.config(text="Computer chose: ")
    result_label.config(text="Let's play!")
    score_label.config(text="Score -> You: 0 | Computer: 0")

# Initialize scores
user_score = 0
computer_score = 0

# Create main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

# Fonts and padding
font_big = ("Arial", 16)
pad = 10

# Widgets
title_label = tk.Label(window, text="Rock-Paper-Scissors", font=("Arial", 20, "bold"))
title_label.pack(pady=pad)

instruction_label = tk.Label(window, text="Choose rock, paper, or scissors:", font=font_big)
instruction_label.pack(pady=pad)

# Buttons for choices
button_frame = tk.Frame(window)
button_frame.pack(pady=pad)

rock_button = tk.Button(button_frame, text="Rock", width=10, font=font_big, command=lambda: play("rock"))
paper_button = tk.Button(button_frame, text="Paper", width=10, font=font_big, command=lambda: play("paper"))
scissors_button = tk.Button(button_frame, text="Scissors", width=10, font=font_big, command=lambda: play("scissors"))

rock_button.grid(row=0, column=0, padx=5)
paper_button.grid(row=0, column=1, padx=5)
scissors_button.grid(row=0, column=2, padx=5)

# Game result display
user_choice_label = tk.Label(window, text="You chose: ", font=font_big)
user_choice_label.pack()

computer_choice_label = tk.Label(window, text="Computer chose: ", font=font_big)
computer_choice_label.pack()

result_label = tk.Label(window, text="Let's play!", font=font_big)
result_label.pack(pady=pad)

score_label = tk.Label(window, text="Score -> You: 0 | Computer: 0", font=font_big)
score_label.pack(pady=pad)

# Reset and exit
control_frame = tk.Frame(window)
control_frame.pack(pady=pad)

reset_button = tk.Button(control_frame, text="Play Again", font=font_big, command=reset_game)
reset_button.grid(row=0, column=0, padx=10)

exit_button = tk.Button(control_frame, text="Exit", font=font_big, command=window.destroy)
exit_button.grid(row=0, column=1, padx=10)

# Start GUI event loop
window.mainloop()
