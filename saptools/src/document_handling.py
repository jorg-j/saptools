"""
Handles Write and append to outfile, read file and document selector
"""
from tkinter import *
from tkinter import filedialog


# -----------------------------------------------------------------------

######################### Write/Append to File #########################


def writer(line, Mode="a+", OutName="outfile.py"):
    with open(OutName, Mode) as f:
        f.write(line)
        f.write("\n")


# -----------------------------------------------------------------------


########################## Document Selector ###########################


def document_select():
    root = Tk()
    root.filename = filedialog.askopenfilename()
    filepath = root.filename
    root.destroy()
    data = read_data(filepath=filepath)
    return data


# -----------------------------------------------------------------------

############################## Read File ##############################


def read_data(filepath):
    with open(filepath, "r") as f:
        data = f.read()
    data = data.split("\n")
    return data


# -----------------------------------------------------------------------
