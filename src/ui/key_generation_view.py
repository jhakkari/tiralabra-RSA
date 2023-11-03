from tkinter import ttk, constants

class KeyGenerationView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Nothing in here, yet!")

        label.grid(row=0, column=0, columnspan=2)
        self._frame.rowconfigure(0, minsize=200, weight=1)
        self._frame.columnconfigure(0, minsize=200, weight=1)