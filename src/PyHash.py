from tkinter import Tk
from Components import View
from Pages.Init import InitPage
from Pages.Main import MainPage
from Components.HashManager import HashManager
from Pages.About import AboutPage


class PyHash(Tk):
    def __init__(self: Tk) -> Tk:
        super().__init__()
        # window properties
        self.title('PyHash')
        self.geometry(
            f'150x150+{int(self.winfo_x() + ((self.winfo_screenwidth() / 2) - 75))}+{int(self.winfo_y() + ((self.winfo_screenheight() / 2) - 75))}')
        self.minsize(150, 150)
        self.iconbitmap(join('Resources', 'Icons', 'Static', 'icon.ico'))
        # apply custom layout
        View.Layout(self)
        # init theme
        self.theme: object = View.Theme(self)
        self.theme.apply('System')
        # load init window
        self.init_page: InitPage = InitPage(self)
        self.init_page.place(x=0, y=0, relwidth=1, relheight=1)
        # initialize hash manager
        self.hash_manager = HashManager()
        # init ui after initialization
        self.after(1000, self.__init_ui)
        self.mainloop()

    def __init_ui(self: object) -> None:
        # load about page
        self.about_page = AboutPage(self, props={'theme': self.theme})
        self.about_page.place(x=0, y=0, relwidth=1, relheight=1)
        # load main page
        self.main_page: MainPage = MainPage(
            self, props={'theme': self.theme, 'hash_manager': self.hash_manager, 'about_page': self.about_page})
        self.main_page.place(x=0, y=0, relwidth=1, relheight=1)
        # unload init window
        self.init_page.place_forget()
        del self.init_page
        # restore properties
        self.geometry(
            f'500x150+{int(self.winfo_x() - 175)}+{int(self.winfo_y())}')
        self.minsize(500, 150)


if __name__ == "__main__":
    PyHash()
