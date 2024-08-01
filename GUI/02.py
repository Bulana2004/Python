import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("Thisis my first GUI Project")

        self.label1 = tkinter.Label(
            self.main_window, text="Flat!", borderwidth=4, relief='flat')
        self.label2 = tkinter.Label(
            self.main_window, text="Raised!", borderwidth=4, relief='raised')
        self.label1.pack(padx=20, pady=20, side='left')
        self.label2.pack()

        tkinter.mainloop()


mygui = MyGUI()
