import tkinter as tk
from tkinter import filedialog
import requests

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

def download_images():
    file_path = f1.get()
    folder_path = f2.get()
    url_list, names_list = [], []

    with open(file_path, "r") as f:
        lines  = f.readlines()
        for line in lines:
            url,name = line.split("|")
            url_list.append(url)
            names_list.append(name.strip())
    
    count = 0
    
    for i,link in enumerate(url_list):
        try:
            page = requests.get(link).content

            with open(f"{folder_path}/{names_list[i]}.jpg", "wb+") as f:
                f.write(page)
            
            count += 1
        except Exception as e:
            continue


heading = tk.Label(window, text="Bulk Image Downloader", font=("Comic Sans MS",20,"bold"))
heading.pack(padx=20, pady=15)

inp_frame = tk.Frame(window)
inp_frame.pack()

f_text = tk.Label(inp_frame, text="Input File :", font=("Comic Sans MS",15))
f_text.grid(row=0, column=0, sticky="E", padx=10, pady=10)

f1 = tk.StringVar()
f_ent = tk.Entry(inp_frame, textvariable=f1, font=("Comic Sans MS",13))
f_ent.grid(row=0, column=1, padx=(10,20),  pady=10)

f_btn = tk.Button(inp_frame, text="Browse", font=("Comic Sans MS",15), command=browse_file)
f_btn.grid(row=0, column=2, padx=(0,20), pady=10, ipadx=5)

fold_text = tk.Label(inp_frame, text="Output Folder :", font=("Comic Sans MS",15))
fold_text.grid(row=1, column=0, sticky="E", padx=10, pady=10)

f2 = tk.StringVar()
fold_ent = tk.Entry(inp_frame, textvariable=f2, font=("Comic Sans MS",13))
fold_ent.grid(row=1, column=1, padx=(10,20),  pady=10)

fold_btn = tk.Button(inp_frame, text="Browse", font=("Comic Sans MS",15), command=browse_folder)
fold_btn.grid(row=1,column=2, padx=(0,20), pady=10, ipadx=5)

download_btn = tk.Button(inp_frame, text="Download", font=("Comic Sans MS",15), command=download_images)
download_btn.grid(row=2, columnspan=3, pady=(10,20))

window.mainloop()