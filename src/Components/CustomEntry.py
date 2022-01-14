from tkinter import ttk, PhotoImage
from pyperclip import copy
from os.path import join


class CustomEntry(ttk.Frame):
    def __init__(self: ttk.Frame, parent: object, text: str = '', theme: str = 'Light') -> ttk.Frame:
        super().__init__(parent)
        # icon cahce
        self.icons: dict = {
            'copy': PhotoImage(file=join('Resources', 'Icons', theme, 'copy.png')),
        }
        # layout
        ttk.Label(self, text=text, style='small.TLabel', width=6).pack(
            side='left', padx=(0, 10))
        self.entry: ttk.Entry = ttk.Entry(
            self, style='dark.TEntry', font=('catamaran 11 bold'))
        self.entry.pack(side='left', fill='x', expand=True)
        ttk.Button(self, image=self.icons['copy'], style='light.TButton', command=lambda: copy(self.entry.get())).pack(
            side='left', padx=10)

    def set(self: object, text: str) -> None:
        self.entry.delete(0, 'end')
        if text:
            self.entry.insert(0, text)
