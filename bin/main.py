

import tkinter as tk
from nlpFunction import nlpFunction


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Input Widget
        self.toSummarize = ""
        self.entry = tk.Entry(self)
        self.entry['textvariable'] = self.toSummarize
        self.entry.pack(side="top", pady=0)

        # Num Sentences (of output) Widget
        self.var = int()
        self.scale = tk.Scale(self)
        self.scale['variable'] = self.var
        self.scale["orient"] = "horizontal"
        self.scale["from"] = 1
        self.scale["to"] = 8
        self.scale.pack(side="top")

        # Button Widget
        self.summarizeButton = tk.Button(self)
        self.summarizeButton["text"] = "Summarize"
        self.summarizeButton["command"] = self.summarize
        self.summarizeButton.pack(side="top", pady=4)

        # Output Widget
        self.summaryMessage = tk.Message(self)
        self.summaryMessage.pack(expand=True)

    def summarize(self):
        input = self.entry.get()  # get(1.0, "end-1c")
        numSentences = self.scale.get()
        print("log: main.py: line 43: number of SENTENCES requested for SUMMARY: " + str(numSentences))
        input = nlpFunction(input, numSentences)
        self.summaryMessage.config(text=input)


# -------------------------------------------------------------
# Mainloop
# -------------------------------------------------------------
root = tk.Tk()
root.title("Summarizer GUI")
root.geometry("600x400")
app = Application(master=root)
app.mainloop()


