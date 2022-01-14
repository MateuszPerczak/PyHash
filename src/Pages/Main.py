from re import S
from tkinter import ttk, PhotoImage
from Components.CustomEntry import CustomEntry
from os.path import basename
from threading import Thread


class MainPage(ttk.Frame):
    def __init__(self: object, parent: object, props: dict) -> ttk.Frame:
        super().__init__(parent)
        # variables
        theme: str = props['theme'].get_theme()
        self.hash_manager: object = props['hash_manager']
        self.about_page: object = props['about_page']
        # icons cache
        self.icons: dict = {
            'add': PhotoImage(file=fr'Resources\\Icons\\{theme}\\add.png'),
            'info': PhotoImage(file=fr'Resources\Icons\\{theme}\\info.png')
        }
        # page layout
        # left frame
        self.left_frame: ttk.Frame = ttk.Frame(self, style='dark.TFrame')
        ttk.Button(self.left_frame, image=self.icons['add'], text='Add file', compound='left', command=self.__open_file).pack(
            side='top', anchor='c', padx=10, pady=10)
        ttk.Button(self.left_frame, image=self.icons['info'], text='About', compound='left', command=self.__open_about).pack(
            side='bottom', anchor='c', padx=10, pady=(0, 10))
        self.left_frame.pack(side='left', fill='y')
        # right frame
        self.right_frame: ttk.Frame = ttk.Frame(self)
        # entry
        # sha 256 entry
        self.sha256_entry: CustomEntry = CustomEntry(
            self.right_frame, text='Sha256', theme=theme)
        self.sha256_entry.pack(side='top', pady=10, fill='x', padx=10)
        # sha1 entry
        self.sha1_entry: CustomEntry = CustomEntry(
            self.right_frame, text='Sha1', theme=theme)
        self.sha1_entry.pack(side='top', pady=(0, 10), fill='x', padx=10)
        # md5 entry
        self.md5_entry: CustomEntry = CustomEntry(
            self.right_frame, text='Md5', theme=theme)
        self.md5_entry.pack(side='top', pady=(0, 10), fill='x', padx=10)
        # pack right frame
        self.right_frame.pack(side='right', fill='both', expand=True)

    def __open_file(self: object) -> None:
        if self.hash_manager.open_file():
            self.master.title(f'PyHash -> {basename(self.hash_manager.file)}')
            self.sha256_entry.set('Calculating ...')
            self.sha1_entry.set('Calculating ...')
            self.md5_entry.set('Calculating ...')
            self.__get_hashes()
        else:
            self.master.title('PyHash')
            self.sha256_entry.set('')
            self.sha1_entry.set('')
            self.md5_entry.set('')

    def __get_hashes(self: object) -> None:
        Thread(target=lambda: self.sha256_entry.set(
            self.hash_manager.get_sha256()), daemon=True).start()
        Thread(target=lambda: self.sha1_entry.set(
            self.hash_manager.get_sha1()), daemon=True).start()
        Thread(target=lambda: self.md5_entry.set(
            self.hash_manager.get_md5()), daemon=True).start()

    def __open_about(self: object) -> None:
        self.about_page.tkraise()
