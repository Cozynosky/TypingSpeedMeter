import tkinter as tk
from colors import *


class Results(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)
        # prepare GUI
        self.results_label = tk.Label(self, text="Results", bg=PRIMARY_COLOR, fg="white", font=("Myanmar Text"
                                                                                                , 45, "bold"))
        self.words_per_minute_label = tk.Label(self, bg=PRIMARY_COLOR, fg="white", font=("Myanmar Text"
                                                                                   , 26, "bold"))
        self.chars_per_minute_label = tk.Label(self, bg=PRIMARY_COLOR, fg="white", font=("Myanmar Text"
                                                                                   , 26, "bold"))
        self.reset_button = tk.Button(self, text="Reset", command=self.reset_test, fg="white", bg=SECONDARY_COLOR,
                                      width=10,
                                      font=("Myanmar Text", 15, "bold"))
        self.results_label.place(relx=0.5, y=70, anchor=tk.CENTER)
        self.words_per_minute_label.place(relx=0.5, y=150, anchor=tk.CENTER)
        self.chars_per_minute_label.place(relx=0.5, y=200, anchor=tk.CENTER)
        self.reset_button.place(relx=0.5, y=500, anchor=tk.CENTER)

    def generate_results(self):
        self.words_per_minute_label['text'] = f"WPM: {len(self.controller.correct_words)}"
        self.chars_per_minute_label['text'] = f"CHPM: {sum(map(len,self.controller.correct_words))}"

    def reset_test(self):
        self.controller.new_test()
        self.controller.show_frame("Menu")
