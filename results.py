import tkinter as tk
from colors import *


class Results(tk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        super().__init__(parent)
        # prepare GUI