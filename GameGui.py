import tkinter as tk
from tkinter import messagebox
import random

# Word to guess
words = [ 'phishing', 'malware', 'firewall', 'trojan', 'ransomware', 'spyware', 'rootkit', 'exploit', 'backdoor', 'botnet', 'hashing', 'encryption', 'keylogger', 'bruteforce', 'spoofing', 'dns', 'penetration', 'zero-day', 'patch', 'ddos', 'vpn', 'darkweb', 'trojanhorse', 'adware', 'socialengineering']
WORD = random.choice(words)

hidden_word = ["_"] * len(WORD)
attempts = 12  # Number of allowed incorrect guesses

# Function to check the guessed letter
def check_guess():
    global attempts
    guess = entry.get()  # Get user input
    entry.delete(0, tk.END)  # Clear input field

    if len(guess) != 1 or not guess.isalpha():
        messagebox.showwarning("Invalid Input", "Please enter a single letter.")
        return

    if guess in WORD:
        for i, letter in enumerate(WORD):
            if letter == guess:
                hidden_word[i] = guess
    else:
        attempts -= 1

    update_display()

    if "_" not in hidden_word:
        messagebox.showinfo("Congratulations!", "You guessed the word!")
        window.quit()
    elif attempts == 0:
        messagebox.showinfo("Game Over", f"You lost! The word was {WORD}")
        window.quit()

# Function to update the word display
def update_display():
    word_label.config(text=" ".join(hidden_word))
    attempts_label.config(text=f"Attempts left: {attempts}")

# Create main window
window = tk.Tk()
window.geometry('500x200')
window.title("Word Guessing Game")

# UI Elements
word_label = tk.Label(window, text=" ".join(hidden_word), font=("Arial", 20))
word_label.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=5)

guess_button = tk.Button(window, text="Guess", command=check_guess)
guess_button.pack(pady=5)

window.bind("<Return>", lambda event: check_guess())

attempts_label = tk.Label(window, text=f"Attempts left: {attempts}", font=("Arial", 14))
attempts_label.pack(pady=10)

# Run the application
window.mainloop() 
