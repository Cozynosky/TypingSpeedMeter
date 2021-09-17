from tkinter import *

# --- CONSTANTS ---
PRIMARY_COLOR = "#077187"


class App:
    def __init__(self, window):
        # prepare window
        self.window = window
        window.title("Typing speed meter")
        window.geometry("500x600")
        window["bg"] = PRIMARY_COLOR
        # prepare widgets
        self.title_label = Label(window, text="Typing Speed Meter", bg=PRIMARY_COLOR, fg="white", font=("Comic Sans MS", 20, "bold"))

        self.menu()


    def menu(self):
        self.title_label.pack()


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()