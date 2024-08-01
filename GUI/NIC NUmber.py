import tkinter as tk
import tkinter.messagebox


class NIC:

    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()
        root = self.main_window

        # Window name
        root.title("Ckeck birthday and Gender using NIC")

        # Making the title
        self.title = tkinter.Label(
            root,
            text="Enter NIC Number to check the Birthday and Gender",
            padx=100
        )

        # Create the input
        self.data_entry = tk.Entry(
            root,
            width=20,
            justify='center'
        )

        # Create button frame
        self.button_frame = tk.Frame(root)
        button_frame = self.button_frame

        # creat buttons
        self.bd_button = tk.Button(
            button_frame,
            text='Get Birthday',
            width=10,
            command=self.birthday
        )
        self.gd_button = tk.Button(
            button_frame,
            text='Get Gender',
            width=10,
            command=self.gender
        )

        self.quit = tk.Button(
            root,
            text='Quit',
            command=root.destroy,
            width=10,
            bg='#a40000',
            fg='white'
        )

        # Pack the widgets
        self.title.pack(pady=5)
        self.data_entry.pack(pady=10)
        self.button_frame.pack(pady=5)
        self.bd_button.pack(padx=5, side='left')
        self.gd_button.pack(padx=5)
        self.quit.pack(pady=5)

        # Enter the tkinter to mainloop
        tkinter.mainloop()

    def birthday(self):
        nic = self.data_entry.get().strip()

        if not nic:
            tk.messagebox.showwarning('Input Error', 'Input entry is empty')
        else:
            try:
                if not nic.isdigit():
                    tk.messagebox.showwarning(
                        'Result', 'Check the NIC number and try again')
                else:
                    if len(nic) == 12:
                        tk.messagebox.showinfo('Result', 'NIC is valid')
                    else:
                        tk.messagebox.showwarning(
                            'Result', 'NIC must be exactly 12 digits long')
            except ValueError:
                tk.messagebox.showinfo('Result', 'Value Error')

    def gender(self):
        nic = self.data_entry.get().strip()
        if not nic:
            tk.messagebox.showwarning('Input Error', 'Input entry is empty')
        else:
            try:
                nic_number = self.data_entry.get()
                if not nic_number.isdigit():
                    tk.messagebox.showwarning(
                        'Result', f'Check the nic number and try again')
                else:
                    tk.messagebox.showinfo('Result', f'{nic_number}')
            except:
                tk.messagebox.showinfo('Result', f'Value Error')


Tst = NIC()
