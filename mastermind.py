import tkinter as tk
import random

def generate_secret_code(length=4):
    return [random.randint(1, 6) for _ in range(length)]

def get_feedback(guess, secret_code):
    correct_position = 0
    correct_color = 0
    secret_code_copy = secret_code[:]
    guess_copy = guess[:]

    for i in range(len(guess)):
        if guess[i] == secret_code[i]:
            correct_position += 1
            secret_code_copy[i] = None
            guess_copy[i] = None

    for i in range(len(guess)):
        if guess_copy[i] is not None and guess_copy[i] in secret_code_copy:
            correct_color += 1
            secret_code_copy[secret_code_copy.index(guess_copy[i])] = None

    return correct_position, correct_color

class MastermindGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Mastermind Game")

        self.secret_code = generate_secret_code()
        #print("Secret code for testing:", self.secret_code)  # This line prints the secret code to the console

        self.attempts = 0
        self.max_attempts = 10
        self.guess_history = []  # List to store guesses and their feedback

        self.label = tk.Label(master, text="Guess the 4-digit code (numbers 1-6):")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.feedback_label = tk.Label(master, text="")
        self.feedback_label.pack()

        self.history_label = tk.Label(master, text="Previous Guesses:")
        self.history_label.pack()

        self.history_list = tk.Listbox(master, height=10, width=50)
        self.history_list.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.make_guess)
        self.guess_button.pack()

        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game)
        self.reset_button.pack()

    def make_guess(self):
        guess = self.entry.get().strip()
        if not guess.isdigit() or len(guess) != 4 or any(char not in '123456' for char in guess):
            self.feedback_label.config(text="Invalid input. Use numbers 1-6.")
            return

        guess = [int(char) for char in guess]
        correct_position, correct_color = get_feedback(guess, self.secret_code)
        feedback_text = f"{correct_position} exact; {correct_color} correct color but wrong position."
        self.feedback_label.config(text=feedback_text)
        self.guess_history.append((guess, feedback_text))
        self.update_history_list()
        self.attempts += 1

        if correct_position == 4:
            self.feedback_label.config(text="Correct! You've guessed the code!")
            self.guess_button.config(state='disabled')
        elif self.attempts >= self.max_attempts:
            self.feedback_label.config(text=f"Game Over! The code was: {''.join(map(str, self.secret_code))}")
            self.guess_button.config(state='disabled')

    def update_history_list(self):
        self.history_list.delete(0, tk.END)
        for guess, feedback in self.guess_history:
            self.history_list.insert(tk.END, f"{''.join(map(str, guess))}: {feedback}")

    def reset_game(self):
        self.secret_code = generate_secret_code()
        self.attempts = 0
        self.guess_history.clear()
        self.update_history_list()
        self.guess_button.config(state='normal')
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    gui = MastermindGUI(root)
    root.mainloop()
