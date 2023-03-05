import tkinter as tk
from tkinter import messagebox

import db as db

root = tk.Tk()


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        db.close_db()
        root.destroy()


def start():
    db.open_db()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()


if __name__ == '__main__':
    start()
