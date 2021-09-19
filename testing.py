import tkinter as tk
from colors import *


class Testing(tk.Frame):
    def __init__(self, controller, parent):
        self.controller = controller
        super().__init__(parent)
        controller.title("Typing speed test")
        self["bg"] = PRIMARY_COLOR
        # prepare GUI
        self.title_label = tk.Label(self, text="Typing", bg=PRIMARY_COLOR, fg="white", font=("Myanmar Text"
                                                                                                         , 26, "bold"))
        self.start_button = tk.Button(self, text="Start", fg="white", bg=SECONDARY_COLOR, width=15, font=("Myanmar Text"
                                                                                                         , 15, "bold"))
        self.title_label.grid(row=0, pady=60)
        self.start_button.grid(row=1)
