from tkinter import ttk, PhotoImage
from os.path import join


class InitPage(ttk.Frame):
    def __init__(self: object, parent: object) -> ttk.Frame:
        super().__init__(parent, style='dark.TFrame')
        # page layout
        self.icon: PhotoImage = PhotoImage(
            file=join('Resources', 'Icons', 'Static', 'icon.png'))
        ttk.Label(self, image=self.icon, anchor='c').pack(
            side='top', fill='both', expand=True)
