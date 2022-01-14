from hashlib import sha256, md5, sha1
from tkinter.filedialog import askopenfilename
from os.path import join, expanduser
from typing import Callable


class HashManager:
    """
    Class that manages the hash values of the files.
    """

    def __init__(self: object) -> object:
        # get user desktop fodler path
        self.user_desktop: str = join(expanduser("~"), "Desktop")
        # file
        self.file: str = ''

    def open_file(self: object) -> bool:
        self.file: str = askopenfilename(initialdir=self.user_desktop, filetypes=(
            ('All Files', '*.*'), ), title='Choose a file')
        if self.file:
            return True
        return False

    def get_sha1(self: object) -> str:
        sha1sum: Callable = sha1()
        with open(self.file, 'rb') as source:
            block: bytes = source.read(2 ** 16)
            while len(block) != 0:
                sha1sum.update(block)
                block: bytes = source.read(2 ** 16)
        return sha1sum.hexdigest()

    def get_sha256(self: object) -> str:
        with open(self.file, 'rb') as source:
            contents: bytes = source.read()
        return sha256(contents).hexdigest()

    def get_md5(self: object) -> str:
        md5_func: Callable = md5()
        with open(self.file, 'rb') as source:
            while True:
                data: bytes = source.read(65536)
                if not data:
                    break
                md5_func.update(data)
        return md5_func.hexdigest()
