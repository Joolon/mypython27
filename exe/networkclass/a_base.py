__authon__ = 'Jolon'

from Tkinter import *

class App:
    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(frame,text='Exit',fg='red',command=frame.quit)
        self.button.pack()

        self.HiButton = Button(frame,text='Say Hi',fg='green',command=self.say_hi)
        self.HiButton.pack()

    def say_hi(self):
        print 'Hi Sundy,Thanks!'


root = Tk()
app = App(root)
root.mainloop()


