import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.title('Bulk Image Downloader')

def browse_file():
    file = filedialog.askopenfilename()
    if file:
        f1.set(file)

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        f2.set(folder)

heading = tk.Label(window, text="Bulk Image Downloader")
heading.pack()

inp_frame = tk.Frame(window)
inp_frame.pack()

f_text = tk.Label(inp_frame, text="Input File :")
f_text.grid(row=0, column=0)

f1 = tk.StringVar()
f_ent = tk.Entry(inp_frame, textvariable=f1)
f_ent.grid(row=0, column=1)

f_btn = tk.Button(inp_frame, text="Browse")
f_btn.grid(row=0, column=2)

fold_text = tk.Label(inp_frame, text="Output Folder :")
fold_text.grid(row=1, column=0)

f2 = tk.StringVar()
fold_ent = tk.Entry(inp_frame, textvariable=f2)
fold_ent.grid(row=1, column=1)

fold_btn = tk.Button(inp_frame, text="Browse")
fold_btn.grid(row=1,column=2)

download_btn = tk.Button(inp_frame, text="Download")
download_btn.grid(row=2, columnspan=3)

window.mainloop()