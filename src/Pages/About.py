from tkinter import ttk, PhotoImage


class AboutPage(ttk.Frame):
    def __init__(self: object, parent: object, props: dict) -> ttk.Frame:
        super().__init__(parent, style='dark.TFrame')
        # variables
        theme = props['theme'].get_theme()
        # icons cache
        self.icons: dict = {
            'info': PhotoImage(file=fr'Resources\Icons\\{theme}\\info.png'),
            'back': PhotoImage(file=fr'Resources\Icons\\{theme}\\back.png'),
        }
        # page layout
        content: ttk.Frame = ttk.Frame(self, style='dark.TFrame')
        ttk.Label(content, image=self.icons['info'], text='About PyHash', style='big.TLabel', compound='left').pack(
            side='top', pady=10, padx=10, fill='x')
        ttk.Label(content, text='Version: 1.0.4 Build: 140122', style='dark.small.TLabel').pack(
            side='top', padx=10, fill='x')
        ttk.Label(content, text='Icons: Icons8', style='dark.small.TLabel').pack(
            side='top', padx=10, fill='x')
        ttk.Label(content, text='Author: Mateusz Perczak', style='dark.small.TLabel').pack(
            side='top', padx=10, fill='x')
        content.place(x=0, y=0, relwidth=1, relheight=1)
        # back button
        back: ttk.Frame = ttk.Frame(self, style='dark.TFrame')

        ttk.Button(back, image=self.icons['back'], command=lambda: self.lower(
        ), style='light.TButton').pack(padx=10, pady=10)

        back.place(relx=1, rely=1, anchor='se')
