from tkinter import Tk
from ui.ui import UI

window = Tk()
window.title("Tiralabra-RSA")
window.geometry('780x560')
window.minsize(370, 220)

ui_view = UI(window)
ui_view.start()

window.mainloop()
