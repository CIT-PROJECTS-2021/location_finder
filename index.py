from html.parser import HTMLParser
from pydoc import HTMLDoc
from tkinter import *   
from tkhtmlview import RenderHTML,HTMLLabel# pip install tkthmlview
import tk_html_widgets

main_window = Tk()

html_label = HTMLLabel(main_window,html=RenderHTML('.index.html'))
html_label.pack(fill='both',expand=True)
html_label.fit_height()

main_window.mainloop()