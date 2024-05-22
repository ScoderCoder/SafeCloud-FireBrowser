# Sougato, Yuvaansh, Alessio
# Innovation Project

# Import + Define lib
import tkinter as tk
from tkinter import ttk 

import os
import json

# banfile
banfile = "banned.json"

# Load the JSON data from the file
with open(banfile, 'r') as file:
    data = file.read()

# Convert the JSON data into a Python list
blist = json.loads(data)

# print(blist)

def refresh():
    with open(banfile, "w") as file:
        file.truncate()

    with open(banfile, 'a') as file:
      json.dump(blist, file, indent=1)

class App():
    def __init__(self):
        self.root = tk.Tk()

        # size
        self.root.geometry("400x400")

        #title
        self.root.title("SafeCloud FireBrowser")

        self.mainframe = tk.Frame(self.root, background="gray") # put everything in frame

        for widgets in self.mainframe.winfo_children():
            widgets.destroy()

        self.mainpage()

        self.root.mainloop()

        return

    def mainpage(self):
        for widgets in self.mainframe.winfo_children():
            widgets.destroy()
        
        # specify location of mainframe
        self.mainframe.pack(fill="both", expand=True) # both means both x and y

        # create text in mainframe
        self.text = ttk.Label(self.mainframe, text="SafeCloud FireBrowser", background="gray", font=("Ubuntu", 20))
        # specify where on the mainframe the text box will go
        self.text.grid(row=0, column=0, padx=10)

        self.text = ttk.Label(self.mainframe, text="Enter URL address", background="gray", font=("Ubuntu", 12))
        self.text.grid(row=1, column=0, padx=10)

        self.settextfield = ttk.Entry(self.mainframe)
        self.settextfield.grid(row=2, column=0, pady=10, padx=10, sticky="NWES") # pady = add padding y, sticky="NWES" makes box scale to fit entire cell

        set_text_button = ttk.Button(self.mainframe, text="Submit", command=self.open_website)
        set_text_button.grid(row=2, column=2, pady=10)

        set_text_button = ttk.Button(self.mainframe, text="Filter Settings", command=self.filter_settings)
        set_text_button.grid(row=3, column=0, pady=10)

    def open_website(self):
        websitetoopen = self.settextfield.get()

    def add_site(self):
        appe = self.settextfield.get()

        blist.append(appe)

        refresh()

        self.filter_settings()

    def remove_site(self):
        appe = self.unban.get()

        if appe in blist:
            blist.remove(appe)
        else:
            print("Error: Custom value enserted to dropdown.")

        refresh()

        self.filter_settings()

    def filter_settings(self):
        for widgets in self.mainframe.winfo_children():
            widgets.destroy()

        self.text = ttk.Label(self.mainframe, text="SafeCloud FireBrowser", background="gray", font=("Ubuntu", 20))
        # specify where on the mainframe the text box will go
        self.text.grid(row=0, column=0, padx=10)

        self.text = ttk.Label(self.mainframe, text="Filter Settings", background="gray", font=("Ubuntu", 12))
        self.text.grid(row=1, column=0, padx=10)

        self.text = ttk.Label(self.mainframe, text="Add website: ", background="gray", font=("Ubuntu", 12))
        self.text.grid(row=2, column=0, padx=10)

        self.settextfield = ttk.Entry(self.mainframe)
        self.settextfield.grid(row=3, column=0, pady=10, padx=10, sticky="NWES")

        set_text_button = ttk.Button(self.mainframe, text="Add", command=self.add_site)
        set_text_button.grid(row=3, column=1, pady=10)

        self.unban = ttk.Combobox(self.mainframe, value=blist)
        self.unban.grid(row=4, column=0, pady=10, padx=10, sticky="NWES")

        set_text_button = ttk.Button(self.mainframe, text="Remove", command=self.remove_site)
        set_text_button.grid(row=4, column=1, pady=10)

        set_text_button = ttk.Button(self.mainframe, text="Homepage", command=self.mainpage)
        set_text_button.grid(row=5, column=0, pady=10)

        self.text = ttk.Label(self.mainframe, text="FILTER LIST", background="gray", font=("Ubuntu", 12))
        self.text.grid(row=6, column=0, padx=10)

        roo=7

        for i in blist:
            roo+=1

            self.text = ttk.Label(self.mainframe, text=i, background="gray", font=("Ubuntu", 12))
            self.text.grid(row=roo, column=0, padx=10)



if __name__ == "__main__":
    App()