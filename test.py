import tkinter as tk
from colors import *


class Test(tk.Frame):
    def __init__(self, controller, parent):
        self.controller = controller
        super().__init__(parent)
        # prepare GUI
        self.word_label = tk.Label(self, bg=PRIMARY_COLOR, fg="white", font=("Myanmar Text", 26, "bold"))
        self.correct_words_label = tk.Label(self, bg=PRIMARY_COLOR, fg=CORRECT_COLOR, font=("Myanmar Text", 20, "bold"))
        self.wrong_words_label = tk.Label(self, bg=PRIMARY_COLOR, fg=WRONG_COLOR, font=("Myanmar Text", 20, "bold"))
        self.word_entry = tk.Entry(self, font=("Myanmar Text", 20, "bold"), bg=SECONDARY_COLOR, fg=ENTRY_COLOR, border=0,
                                   justify="center", width=15)
        self.time_label = tk.Label(self, bg=PRIMARY_COLOR, fg="white", font=("Myanmar Text", 22))
        # place widgets
        self.word_label.place(relx=0.5, y=210, anchor=tk.CENTER)
        self.correct_words_label.place(relx=0.25, y=120, anchor=tk.CENTER)
        self.wrong_words_label.place(relx=0.75, y=120, anchor=tk.CENTER)
        self.word_entry.place(relx=0.5, y=300, anchor=tk.CENTER)
        self.time_label.place(relx=0.5, y=50, anchor=tk.CENTER)
        # bind spacebar
        self.word_entry.bind("<space>", lambda event: self.check_word())

    def generate_gui(self):
        self.word_label['text'] = self.controller.current_word
        self.correct_words_label['text'] = f"Correct: {len(self.controller.correct_words)}"
        self.wrong_words_label['text'] = f"Wrong: {len(self.controller.wrong_words)}"
        self.time_label['text'] = f"Time left: {self.controller.time_left}"

    def check_word(self):
        passed_word = self.word_entry.get().strip()
        if passed_word == self.controller.current_word:
            self.controller.correct_words.append(passed_word)
            self.correct_words_label["text"] = f"Correct: {len(self.controller.correct_words)}"
        else:
            self.controller.wrong_words.append(passed_word)
            self.wrong_words_label["text"] = f"Wrong: {len(self.controller.wrong_words)}"
        self.word_entry.delete(0, 'end')
        self.controller.current_word = self.controller.next_word()
        self.word_label['text'] = self.controller.current_word

    def start_timer(self):
        if self.controller.time_left > 0:
            self.controller.time_left -= 1
            self.time_label['text'] = f"Time left: {self.controller.time_left}"
            self.controller.after(1000, self.start_timer)
        else:
            self.word_entry.delete(0, 'end')
            self.controller.focus_set()
            self.controller.show_frame("Results")
