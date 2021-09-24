import tkinter as tk
import requests
from colors import *


class WordsGenerator(tk.Frame):
    def __init__(self, controller, parent):
        self.controller = controller
        super().__init__(parent)
        # generate new words
        self.generated_words = self.generate_words()
        self.correct_words = 0
        self.wrong_words = 0
        self.time_left = 60
        # prepare GUI
        self.active_word = self.next_word()
        self.word_label = tk.Label(self, text=self.active_word, bg=PRIMARY_COLOR, fg="white", font=("Myanmar Text"
                                                                                                    , 26, "bold"))
        self.correct_words_label = tk.Label(self, text=f"Correct: {self.correct_words}", bg=PRIMARY_COLOR,
                                            fg=CORRECT_COLOR, font=("Myanmar Text"
                                                                    , 20, "bold"))
        self.wrong_words_label = tk.Label(self, text=f"Wrong: {self.wrong_words}", bg=PRIMARY_COLOR, fg=WRONG_COLLOR,
                                          font=("Myanmar Text"
                                                , 20, "bold"))
        self.word_entry = tk.Entry(self, font=("Myanmar Text", 20, "bold"), bg=SECONDARY_COLOR, fg=ENTRY_COLOR, border=0,
                                   justify="center", width=15)
        self.word_entry.focus()
        self.time_label = tk.Label(self, text=f"Time left: {self.time_left}", bg=PRIMARY_COLOR, fg="white", font=("Myanmar Text"
                                                                                                    , 22))
        # place widgets
        self.word_label.place(relx=0.5, y=210, anchor=tk.CENTER)
        self.correct_words_label.place(relx=0.25, y=120, anchor=tk.CENTER)
        self.wrong_words_label.place(relx=0.75, y=120, anchor=tk.CENTER)
        self.word_entry.place(relx=0.5, y=300, anchor=tk.CENTER)
        self.time_label.place(relx=0.5, y=50, anchor=tk.CENTER)
        self.timer()

    @staticmethod
    def generate_words():
        response = requests.get(url="https://random-word-api.herokuapp.com/word", params={"number": 500})
        words_data = response.json()
        return words_data

    def next_word(self):
        return self.generated_words.pop(0)

    def timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label['text'] = self.time_left
            self.controller.after(1000, self.timer)
        else:
            self.time_left = 60
            self.controller.show_frame("Menu")
