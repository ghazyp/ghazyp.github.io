import tkinter as tk
import random

# The Mastermind game

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
        self.current_guess = []
        self.attempts = 0
        self.max_attempts = 10

        # Game Frame
        game_frame = tk.Frame(master)
        game_frame.pack(pady=20)

        # History Frame
        history_frame = tk.Frame(master)
        history_frame.pack(pady=20)

        # Number buttons
        button_frame = tk.Frame(game_frame)
        button_frame.pack()

        for i in range(1, 7):
            btn = tk.Button(button_frame, text=str(i), command=lambda num=i: self.append_number(num))
            btn.pack(side="left", padx=5)

        # Entry and Feedback
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(game_frame, textvariable=self.entry_var, width=50)
        self.entry.pack()

        self.feedback_label = tk.Label(game_frame, text="")
        self.feedback_label.pack()

        # Guess and Reset buttons
        self.guess_button = tk.Button(game_frame, text="Guess", command=self.make_guess)
        self.guess_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(game_frame, text="Reset Game", command=self.reset_game)
        self.reset_button.pack(side="right", padx=10)

        # History List
        self.history_label = tk.Label(history_frame, text="Previous Guesses:")
        self.history_label.pack()

        self.history_list = tk.Listbox(history_frame, height=10, width=50)
        self.history_list.pack()

    def append_number(self, num):
        if len(self.current_guess) < 4:
            self.current_guess.append(num)
            self.entry_var.set(''.join(map(str, self.current_guess)))

    def make_guess(self):
        if len(self.current_guess) != 4:
            self.feedback_label.config(text="Please enter exactly 4 numbers.")
            return

        correct_position, correct_color = get_feedback(self.current_guess, self.secret_code)
        feedback_text = f"{correct_position} exact; {correct_color} correct color but wrong position."
        self.feedback_label.config(text=feedback_text)
        self.history_list.insert(tk.END, f"{''.join(map(str, self.current_guess))}: {feedback_text}")
        self.current_guess = []
        self.entry_var.set('')

        self.attempts += 1
        if correct_position == 4:
            self.feedback_label.config(text="Correct! You've guessed the code!")
            self.guess_button.config(state='disabled')
        elif self.attempts >= self.max_attempts:
            self.feedback_label.config(text=f"Game Over! The code was: {''.join(map(str, self.secret_code))}")
            self.guess_button.config(state='disabled')

    def reset_game(self):
        self.secret_code = generate_secret_code()
        self.current_guess = []
        self.entry_var.set('')
        self.attempts = 0
        self.history_list.delete(0, tk.END)
        self.guess_button.config(state='normal')
        self.feedback_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    gui = MastermindGUI(root)
    root.mainloop()
