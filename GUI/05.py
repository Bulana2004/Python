import tkinter as tk
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Display a title.
        self.main_window.title('User Input GUI')

        # Create a label to prompt the user.
        self.prompt_label = tk.Label(
            self.main_window, text="Enter your name:", font=('Helvetica', 12))

        # Create an entry widget for user input.
        self.name_entry = tk.Entry(
            self.main_window, width=20, font=('Helvetica', 12))

        # Create a button to submit the input.
        self.submit_button = tk.Button(
            self.main_window,
            text='Submit',
            command=self.show_name,
            bg='#4CAF50',       # Green background color
            fg='white',         # White text color
            bd=3,               # Border width
            relief='raised',    # Raised border
            font=('Helvetica', 12, 'bold'),
            padx=10,            # Horizontal padding
            pady=5              # Vertical padding
        )

        # Creat Quit button
        self.quit_button = tk.Button(
            self.main_window,
            text="Quit",
            command=self.main_window.destroy,
            bg='#4CAF50',       # Green background color
            fg='white',         # White text color
            bd=3,               # Border width
            relief='raised',    # Raised border
            font=('Helvetica', 12, 'bold'),
            padx=10,            # Horizontal padding
            pady=5              # Vertical padding
        )

        # Create a label to display the input.
        self.display_label = tk.Label(
            self.main_window, text="", font=('Helvetica', 12))

        # Pack the widgets.
        self.prompt_label.pack(padx=20, pady=10)
        self.name_entry.pack(padx=20, pady=10)
        self.submit_button.pack(padx=20, pady=10)
        self.quit_button.pack(padx=20, pady=10)
        self.display_label.pack(padx=20, pady=10)

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # Define method to show the entered name.
    def show_name(self):
        # Get the input from the entry widget.
        name = self.name_entry.get()

        # Display the input in the display label.
        self.display_label.config(text=f"Hello, {name}!")

        # Optionally, show a message box.
        # tkinter.messagebox.showinfo('Responce Massage', f'You entered: {name}')


# Create an instance of the MyGUI class.
my_gui = MyGUI()
