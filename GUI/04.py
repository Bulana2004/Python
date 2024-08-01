import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Display a title.
        self.main_window.title('My First GUI')

        # Display a text with a specific color.
        self.label1 = tkinter.Label(
            self.main_window,
            text="This is a Button",
            fg="blue",
            font=('Helvetica', 10)
        )

        # Create a button with enhanced appearance.
        self.button1 = tkinter.Button(
            self.main_window,
            text='Call Me',
            command=self.Massage,
            bg='#4CAF50',       # Green background color
            fg='white',         # White text color
            bd=3,               # Border width
            relief='raised',    # Raised border
            font=('Helvetica', 12, 'bold'),  # Font style and Font size
            padx=10,            # Horizontal padding
            pady=5              # Vertical padding
        )

        self.button2 = tkinter.Button(
            self.main_window,
            command=self.Massage,
            text='Cancel',
            bg='#4CAF50',       # Green background color
            fg='white',         # White text color
            bd=3,               # Border width
            relief='raised',    # Raised border
            font=('Helvetica', 12, 'bold'),  # Font style and Font size
            padx=10,            # Horizontal padding
            pady=5              # Vertical padding
        )

        # Call the label widget's pack method.
        self.label1.pack(padx=20, pady=20)
        self.button1.pack(padx=100, pady=20, side='left')
        self.button2.pack(padx=100, pady=20, side='right')

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # Define Messagebox Method.
    def Massage(self):
        tkinter.messagebox.showinfo(
            'Response', 'Thanks for clicking the button')


# Create an instance of the MyGUI class.
my_gui = MyGUI()
