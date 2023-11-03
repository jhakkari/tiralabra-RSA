from tkinter import Tk
from ui.ui import UI

window = Tk()
ui_view = UI(window)
ui_view.start()

window.mainloop()