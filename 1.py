from tkinterhtml import HtmlFrame
import tkinter as tk

root = tk.Tk()
frame = HtmlFrame(root,horizontal_scrollbar='auto',vertical_scrollbar='auto')
frame.set_content('.index.html')
#frame.set_content(urllib.request.urlopen)
root.mainloop()