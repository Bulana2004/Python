import tkinter


class Mygui:

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title('Gui Test 2')

        self.label1 = tkinter.Label(
            self.main_window, text="Hellow!", borderwidth=1, relief='solid')
        self.label1.pack()

        tkinter.mainloop()


# call the gui
mygui = Mygui()
