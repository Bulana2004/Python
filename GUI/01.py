import tkinter


class MyGUI(object):
    def __init__(self):

        # Create the main window widget
        self.main_window = tkinter.Tk()

        # Display the titile
        self.main_window.title("My first GUI Project")

        # Display a text
        self.label = tkinter.Label(self.main_window, text="Hello World!")
        self.label2 = tkinter.Label(
            self.main_window, text="This is my GUI programme")
        self.label.pack(side='left')
        self.label2.pack(side='left')

        # Enter Tkinter to main loop
        tkinter.mainloop()


# Create an instance of the MyGui class
mygui = MyGUI()
