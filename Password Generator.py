# TODO Change BitMap Icon

from tkinter import Tk, StringVar
from tkinter.ttk import Label, Button
from pyperclip import copy
from secrets import choice
from string import ascii_letters, digits, punctuation

AVL = ascii_letters + digits + punctuation
FONT = "JetBrains Mono", 40
BG, FG = "#59A958", "#F9D888"
PASS_LEN = KEY_LBL_LEN = 20

window = Tk()
window.title("Password Generator")
window.resizable(width=False, height=False)

key = StringVar(master=window, value="".join([choice(AVL) for _ in range(PASS_LEN)]))


def generate(pass_len=PASS_LEN):
    key.set("".join([choice(AVL) for _ in range(pass_len)]))


key_lbl = Label(
    master=window,
    textvariable=key,
    font=FONT,
    background=BG,
    foreground=FG,
    justify="center",
    width=KEY_LBL_LEN
)
gen_btn = Button(master=window, text="Generate", command=generate)
cpy_btn = Button(master=window, text="Copy", command=lambda: copy(key.get()))

key_lbl.grid(row=0, column=0, rowspan=2, padx=10, pady=10, ipadx=5, ipady=5)
gen_btn.grid(row=0, column=1, padx=10, pady=10, ipadx=5, ipady=5)
cpy_btn.grid(row=1, column=1, padx=10, pady=10, ipadx=5, ipady=5)

window.mainloop()
