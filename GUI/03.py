# This program displays an empty window.
import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Display a title.
        self.main_window.title('My First GUI')

        # Display a text
        self.label1 = tkinter.Label(
            self.main_window, text="This is a Button")

        # Creat a button
        self.button1 = tkinter.Button(
            self.main_window, text='Call Me', command=self.do_something)

        # call the lable widget's pack method
        self.label1.pack(padx=20, pady=20, side='right')
        self.button1.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # define Messagebox Method
    def do_something(self):
        tkinter.messagebox.showinfo(
            'Response', 'Thanks for cliking the button')


# Create an instance of the MyGUI class.
my_gui = MyGUI()
