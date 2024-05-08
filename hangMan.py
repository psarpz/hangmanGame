import random
import tkinter as tk
from tkinter import messagebox
import hangManWords

# Import word list
wordList = hangManWords.hangManWordList

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")

        self.randomChosenWord = ""
        self.stages = ['''
          +---+
          |   |
              |
              |
              |
              |
        =========''','''
          +---+
          |   |
          O   |
              |
              |
              |
        =========''','''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========''','''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========''','''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========''','''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========''','''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========''']

        self.display = []
        self.lives = len(self.stages) - 1

        self.setup_ui()

    def setup_ui(self):
        self.word_label = tk.Label(self.master, text="Word: ")
        self.word_label.grid(row=0, column=0, padx=10, pady=10)

        self.word_display = tk.Label(self.master, text="")
        self.word_display.grid(row=0, column=1, padx=10, pady=10)

        self.guess_label = tk.Label(self.master, text="Guess a letter:")
        self.guess_label.grid(row=1, column=0, padx=10, pady=10)

        self.guess_entry = tk.Entry(self.master)
        self.guess_entry.grid(row=1, column=1, padx=10, pady=10)

        self.guess_button = tk.Button(self.master, text="Guess", command=self.check_guess)
        self.guess_button.grid(row=2, columnspan=2, padx=10, pady=10)

        self.play_hangman()

    def play_hangman(self):
        self.randomChosenWord = random.choice(wordList)
        self.display = ["_"] * len(self.randomChosenWord)
        self.update_word_display()

    def update_word_display(self):
        self.word_display.config(text=" ".join(self.display))

    def check_guess(self):
        user_guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if user_guess in self.randomChosenWord:
            messagebox.showinfo("Correct guess!", "You guessed correctly!")
            for index, letter in enumerate(self.randomChosenWord):
                if letter == user_guess:
                    self.display[index] = user_guess
            self.update_word_display()
        else:
            messagebox.showinfo("Incorrect guess!", "Incorrect guess! Try again.")
            self.update_lives()

        if "_" not in self.display:
            messagebox.showinfo("Congratulations!", "Congratulations! You won!")
            self.reset_game()
        elif self.lives == 0:
            messagebox.showinfo("Game Over", f"Sorry, you lost. The word was: {self.randomChosenWord}")
            self.reset_game()

    def update_lives(self):
        self.lives -= 1
        if self.lives < 0:
            self.lives = 0
        self.word_display.config(text=self.stages[self.lives])

    def reset_game(self):
        self.lives = len(self.stages) - 1
        self.word_display.config(text="")
        self.play_hangman()

def main():
    root = tk.Tk()
    app = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
