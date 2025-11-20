from tkinter import Tk, filedialog
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "resources"))
import d

def choose_files(multiple=True):
    root = Tk()
    root.withdraw()                 
    root.attributes("-topmost", True) 
    filetypes = [("TOML or CSV", ("*.toml", "*.csv"))]
    if multiple:
        paths = filedialog.askopenfilenames(title="Select .toml or .csv file(s)", filetypes=filetypes)
    else:
        p = filedialog.askopenfilename(title="Select a .toml or .csv file", filetypes=filetypes)
        paths = (p,) if p else ()
    root.destroy()
    return list(paths)

a = 1
if a == 1:
    files_to_process = choose_files()
    for file_path in files_to_process:
        d.process_file(file_path)
