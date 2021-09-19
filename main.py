import tkinter as tk
from menu import Menu
from testing import Testing
from colors import *


class App:
    def __init__(self, controller):
        # prepare window
        controller.geometry("500x600")
        container = tk.Frame(controller)
        container["bg"] = PRIMARY_COLOR
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Menu, Testing):
            frame_name = F.__name__
            frame = F(controller, container)
            self.frames[frame_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("Menu")

    def show_frame(self, page_name):
        """"Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
