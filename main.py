import tkinter as tk
from menu import Menu
from words_generator import WordsGenerator
from colors import *


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # prepare window
        self.geometry("500x600")
        self.resizable(False,False)
        self.title("Typing speed meter")
        # prepare controller for switching windows
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Menu, WordsGenerator):
            frame_name = F.__name__
            frame = F(controller=self, parent=container)
            self.frames[frame_name] = frame
            frame["bg"]=PRIMARY_COLOR
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("Menu")

    def show_frame(self, page_name):
        """"Show a frame for the given page name"""
        frame = self.frames[page_name]
        if page_name == "WordsGenerator":
            frame.start_timer()
        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
