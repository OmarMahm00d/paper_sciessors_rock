import tkinter as tk
from tkinter import messagebox
import random

def play_with_friend_window():
    print("hello world")
    pass
def play_with_computer_window():
    def play_with_computer_logic(player_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = ""
        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or \
             (player_choice == "Paper" and computer_choice == "Rock") or \
             (player_choice == "Scissors" and computer_choice == "Paper"):
            result = "You win!"
        else:
            result = "Computer wins!"

        messagebox.showinfo("Result", "Computer chose: " + computer_choice + "\n" + result)

    play_window = tk.Toplevel(root)
    play_window.title("Play with Computer")

    rock_button = tk.Button(play_window, text="Rock", width=10, command=lambda: play_with_computer_logic("Rock"))
    rock_button.grid(row=0, column=0, padx=10, pady=5)

    paper_button = tk.Button(play_window, text="Paper", width=10, command=lambda: play_with_computer_logic("Paper"))
    paper_button.grid(row=0, column=1, padx=10, pady=5)

    scissors_button = tk.Button(play_window, text="Scissors", width=10, command=lambda: play_with_computer_logic("Scissors"))
    scissors_button.grid(row=0, column=2, padx=10, pady=5)

def play_alone_window():
    def play_alone_logic(player1_choice, player2_choice):
        result = ""
        if player1_choice == player2_choice:
            result = "It's a tie!"
        elif (player1_choice == "Rock" and player2_choice == "Scissors") or \
             (player1_choice == "Paper" and player2_choice == "Rock") or \
             (player1_choice == "Scissors" and player2_choice == "Paper"):
            result = "Player 1 wins!"
        else:
            result = "Player 2 wins!"

        messagebox.showinfo("Result", "Player 1 chose: " + player1_choice + "\n" +
                            "Player 2 chose: " + player2_choice + "\n" + result)

    play_window = tk.Toplevel(root)
    play_window.title("Play Alone")

    def player1_choice_logic(choice):
        player1_choice = choice
        player2_choice = random.choice(["Rock", "Paper", "Scissors"])
        play_alone_logic(player1_choice, player2_choice)

    rock_button_p1 = tk.Button(play_window, text="Rock", width=10, command=lambda: player1_choice_logic("Rock"))
    rock_button_p1.grid(row=0, column=0, padx=10, pady=5)

    paper_button_p1 = tk.Button(play_window, text="Paper", width=10, command=lambda: player1_choice_logic("Paper"))
    paper_button_p1.grid(row=0, column=1, padx=10, pady=5)

    scissors_button_p1 = tk.Button(play_window, text="Scissors", width=10, command=lambda: player1_choice_logic("Scissors"))
    scissors_button_p1.grid(row=0, column=2, padx=10, pady=5)

    def player2_choice_logic(choice):
        player1_choice = random.choice(["Rock", "Paper", "Scissors"])
        player2_choice = choice
        play_alone_logic(player1_choice, player2_choice)

    rock_button_p2 = tk.Button(play_window, text="Rock", width=10, command=lambda: player2_choice_logic("Rock"))
    rock_button_p2.grid(row=1, column=0, padx=10, pady=5)

    paper_button_p2 = tk.Button(play_window, text="Paper", width=10, command=lambda: player2_choice_logic("Paper"))
    paper_button_p2.grid(row=1, column=1, padx=10, pady=5)

    scissors_button_p2 = tk.Button(play_window, text="Scissors", width=10, command=lambda: player2_choice_logic("Scissors"))
    scissors_button_p2.grid(row=1, column=2, padx=10, pady=5)

root = tk.Tk()
root.title("An Explosive Rock Paper Scissors Game")

friend_button = tk.Button(root, text="Play with Friend", width=20, command=play_with_friend_window)
friend_button.pack(pady=10)

computer_button = tk.Button(root, text="Play with Computer", width=20, command=play_with_computer_window)
computer_button.pack(pady=10)

alone_button = tk.Button(root, text="Play Alone", width=20, command=play_alone_window)
alone_button.pack(pady=10)

root.mainloop()
