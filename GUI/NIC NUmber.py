import tkinter as tk
import tkinter.messagebox


class NIC:

    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()
        root = self.main_window

        # Disaleb maximize button
        root.resizable(False, False)

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

                        day_of_year = int(nic[4:7])
                        year = int(nic[:4])

                        # Leap year check
                        is_leap_year = (year % 4 == 0 and year %
                                        100 != 0) or (year % 400 == 0)
                        day_of_year -= 1

                        if day_of_year >= 500:
                            day_of_year -= 500

                        if day_of_year <= 31:
                            month = 'January'
                            day = day_of_year
                        elif is_leap_year and day_of_year <= 60:
                            month = 'February'
                            day = day_of_year - 31
                        elif not is_leap_year and day_of_year <= 59:
                            month = 'February'
                            day = day_of_year - 31
                        elif day_of_year <= 90:
                            month = 'March'
                            day = day_of_year - 59
                        elif day_of_year <= 120:
                            month = 'April'
                            day = day_of_year - 90
                        elif day_of_year <= 151:
                            month = 'May'
                            day = day_of_year - 120
                        elif day_of_year <= 181:
                            month = 'June'
                            day = day_of_year - 151
                        elif day_of_year <= 212:
                            month = 'July'
                            day = day_of_year - 181
                        elif day_of_year <= 243:
                            month = 'August'
                            day = day_of_year - 212
                        elif day_of_year <= 274:
                            month = 'September'
                            day = day_of_year - 243
                        elif day_of_year <= 304:
                            month = 'October'
                            day = day_of_year - 274
                        elif day_of_year <= 335:
                            month = 'November'
                            day = day_of_year - 304
                        elif day_of_year <= 365:
                            if is_leap_year:
                                day_of_year += 1
                            month = 'December'
                            day = day_of_year - 335
                        else:
                            # Handle cases where day_of_year exceeds expected ranges
                            month = 'Unknown'
                            day = 'Unknown'

                        tk.messagebox.showinfo(
                            'Birthday', f'{year} / {month} / {day}')

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
