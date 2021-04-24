#!\Users\kolok\anaconda3\envs\py38\python3.8

# import tkinter
# from tkinter import *
import string
from nltk.corpus import stopwords
import pandas as pd
import tkinter as tk
import time
from  nlpFunction import nlpFunction


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.toSummarize = ""
        self.entry = tk.Entry(self)  # options = []

        self.entry['textvariable'] = self.toSummarize
        self.entry.pack(side="top", pady=0)

        self.var = int()
        self.scale = tk.Scale(self)
        self.scale['variable'] = self.var # root, variable=var)
        self.scale["orient"] = "horizontal"
        self.scale["from"] = 1
        self.scale["to"] = 8
        self.scale.pack(side="top") # , position="horizontal")


        self.summarizeButton = tk.Button(self)
        self.summarizeButton["text"] = "Summarize"
        self.summarizeButton["command"] = self.summarize
        self.summarizeButton.pack(side="top", pady=4)

        #self.summary = ""
        self.summaryMessage = tk.Message(self)
        #self.summaryLabel["text"] = self.summary
        # self.summaryLabel["height"] = 10
        # self.summaryLabel["width"] = 20
        self.summaryMessage.pack(expand=True)

        #self.quit = tk.Button(self, text="QUIT", fg="red",
                              #command=self.master.destroy)
        #self.quit.pack(side="bottom")

    def _summarize(self):
        #self.summary = self.toSummarize
        print("hw")
        print(self.summary)
        print(self.entry['textvariable'])

    def summarize(self):
        inp = self.entry.get()  # get(1.0, "end-1c")
        temp = self.scale.get()
        inp = nlpFunction(inp,temp)
        # self.summaryLabel.config(text="one moment...")
        # time.sleep(1)
        self.summaryMessage.config(text=inp)


root = tk.Tk()
root.title("Summarizer GUI")
root.geometry("600x400")
app = Application(master=root)
app.mainloop()


