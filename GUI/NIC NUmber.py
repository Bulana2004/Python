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
            command=self.birthday,
            bg='#231d4d',
            fg='white'
        )
        self.gd_button = tk.Button(
            button_frame,
            text='Get Gender',
            width=10,
            command=self.gender,
            bg='#231d4d',
            fg='white'
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
        # Get NIC number input
        nic = self.data_entry.get().strip()
        # Check input is empty or not
        if not nic:
            tk.messagebox.showwarning('Input Error', 'Input entry is empty')
        else:
            try:
                # Check enter NIC number is digit
                if not nic.isdigit():
                    tk.messagebox.showwarning(
                        'Input Error', 'Check the NIC number and try again')
                else:
                    # Check NIC number lenght is == 12
                    if len(nic) == 12:  # Example NIC number 200418501010

                        # Asign the variables
                        year = int(nic[:4])
                        date_in_year = int(nic[4:7])
                        is_leap_year = (year % 4 == 0 and year %
                                        100 != 0) or (year % 400 == 0)
                        month = None
                        date = None

                        # Female date change rewrite
                        if date_in_year > 365:
                            if is_leap_year:
                                if date_in_year > 366:
                                    date_in_year -= 500
                        else:
                            date_in_year = date_in_year

                        # Calculate birthday
                        if date_in_year <= 31:
                            month = 'January'
                            date = date_in_year
                        elif date_in_year <= 60:
                            month = 'February'
                            date = date_in_year - 31
                            if is_leap_year:
                                if date_in_year == 60:
                                    month = 'February'
                                    date = 29
                        else:
                            if not is_leap_year:
                                date_in_year -= 1
                            if date_in_year <= 90:
                                month = 'March'
                                date = date_in_year - 60
                            elif date_in_year <= 120:
                                month = 'April'
                                date = date_in_year - 91
                            elif date_in_year <= 151:
                                month = 'May'
                                date = date_in_year - 121
                            elif date_in_year <= 181:
                                month = 'June'
                                date = date_in_year - 152
                            elif date_in_year <= 212:
                                month = 'July'
                                date = date_in_year - 182
                            elif date_in_year <= 243:
                                month = 'August'
                                date = date_in_year - 213
                            elif date_in_year <= 273:
                                month = 'September'
                                date = date_in_year - 244
                            elif date_in_year <= 304:
                                month = 'October'
                                date = date_in_year - 274
                            elif date_in_year <= 334:
                                month = 'November'
                                date = date_in_year - 305
                            elif date_in_year <= 365:
                                month = 'December'
                                date = date_in_year - 335

                        tk.messagebox.showinfo(
                            'Birthday', f"{year} / {month} / {date}")

                    else:
                        tk.messagebox.showwarning(
                            'Input Error', 'NIC must be exactly 12 digits long')
            except ValueError:
                tk.messagebox.showinfo('Input Error', 'Value Error')

    def gender(self):
        # Get NIC number input
        nic = self.data_entry.get().strip()
        # Check input is empty or not
        if not nic:
            tk.messagebox.showwarning('Input Error', 'Input entry is empty')
        else:
            try:
                # Check enter NIC number is digit
                if not nic.isdigit():
                    tk.messagebox.showwarning(
                        'Result', 'Check the NIC number and try again')
                else:
                    # Check NIC number lenght is == 12
                    if len(nic) == 12:  # Example NIC number 200418501010
                        date_in_year = int(nic[4:7])
                        # Make femail date
                        if date_in_year > 400:
                            tk.messagebox.showinfo('Gender', 'Female')
                        else:
                            tk.messagebox.showinfo('Gender', 'Male')
                    else:
                        tk.messagebox.showwarning(
                            'Result', 'NIC must be exactly 12 digits long')
            except ValueError:
                tk.messagebox.showinfo('Result', 'Value Error')


Tst = NIC()
