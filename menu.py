import tkinter as tk
from colors import *


class Menu(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)
        # prepare GUI
        self.title_label = tk.Label(self, text="Typing Speed Meter", bg=PRIMARY_COLOR, fg="white", font=("Myanmar Text"
                                                                                                         , 26, "bold"))
        self.start_button = tk.Button(self, text="Start", fg="white", bg=SECONDARY_COLOR, width=15,
                                      font=("Myanmar Text",
                                            15, "bold"), command=lambda: controller.show_frame("WordsGenerator"))
        self.title_label.place(relx=0.5, y=120, anchor=tk.CENTER)
        self.start_button.place(relx=0.5, y=270, anchor=tk.CENTER)
