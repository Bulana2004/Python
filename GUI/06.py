import tkinter as tk
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        # Create the main window widget
        self.main_window = tkinter.Tk()
        root = self.main_window

        # Create the title
        root.title("Convert")

        # Create the content
        self.title = tk.Label(
            root,
            text="Meter to kilometer Convert",
            padx=10
        )
        self.title.pack(pady=10)

        # Make text frame
        self.text_frame = tk.Frame(root)
        self.text_frame.pack(padx=5)

        # Make the input
        self.data_enty = tk.Entry(
            self.text_frame,
            width=10
        )
        self.data_enty.pack(pady=5, side='left')

        self.label1 = tk.Label(
            self.text_frame,
            text="Km"
        )
        self.label1.pack(pady=5, side='left')
        # # Display output
        # self.display_label = tk.Label(
        #     root,
        #     text=''
        # )
        # self.display_label.pack(pady=5)

        # Make a button frame
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        # Create buttons
        self.convert_button = tk.Button(
            self.button_frame,
            text="Convert",
            command=self.convert,
            width=10
        )
        self.convert_button.pack(padx=5, side='left')

        self.quit_button = tk.Button(
            self.button_frame,
            text='Quit',
            command=root.destroy,
            width=10
        )
        self.quit_button.pack(padx=5)

        # Call tkinter to mainloop
        tkinter.mainloop()

    def convert(self):
        try:
            km = float(self.data_enty.get())
            miles = km * 0.621371
            tk.messagebox.showinfo("Result", f"{km} is equal to {miles} miles")
        except:
            tk.messagebox.showwarning("Result", "Invalid input")


mygui = MyGUI()
