import tkinter as tk
import requests
from menu import Menu
from test import Test
from results import Results
from colors import *


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # prepare window
        self.geometry("500x600")
        self.resizable(False, False)
        self.title("Typing speed meter")
        # prepare controller for switching windows
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # start new test
        self.new_test()

        self.frames = {}
        for F in (Menu, Test, Results):
            frame_name = F.__name__
            frame = F(controller=self, parent=container)
            self.frames[frame_name] = frame
            frame["bg"] = PRIMARY_COLOR
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("Menu")

    def next_word(self):
        return self.generated_words.pop(0)

    def new_test(self):
        self.generated_words = self.generate_words()
        self.current_word = self.next_word()
        self.correct_words = []
        self.wrong_words = []
        self.time_left = 5

    @staticmethod
    def generate_words():
        response = requests.get(url="https://random-word-api.herokuapp.com/word", params={"number": 500})
        words_data = response.json()
        return words_data

    def show_frame(self, page_name):
        """"Show a frame for the given page name"""
        frame = self.frames[page_name]
        if page_name == "Test":
            frame.start_timer()
            frame.generate_gui()
            frame.word_entry.focus()
        elif page_name == "Results":
            frame.generate_results()
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
