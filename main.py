import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command = self.master.destroy)

        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


root = tk.Tk()
app = Application(master=root)
app.mainloop()


'''
Learning TKinter by making Tic Tac Toe

first, I'm going to create the logic for tic tac toe in
the console. Then we'll port this over into a GUI Application
using Tkinter. Shouldn't be anything complicated.

Then, once the MVP is ported into TKinter, we'll make extra
"features" for the game. Different game modes if you will.
'''