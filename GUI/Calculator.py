import tkinter as tk
import tkinter.messagebox


class Calculator:

    def __init__(self):
        self.main_window = tkinter.Tk()
        root = self.main_window

        # Disable rezible window
        root.resizable(False, False)

        # The title
        root.title("Calculator")

        # title
        self.title = tk.Label(
            root,
            text="Calculator GUI Project test",
            padx=100
        )

        # Making a frame
        self.input_frame = tk.Frame(root)
        input_frame = self.input_frame

        self.label = tk.Label(
            input_frame,
            text="Enter number to calculate :",
            padx=5,
        )

        self.input = tk.Entry(
            input_frame,
            width=20,
            justify='center'
        )

        # First row
        self.row1 = tk.Frame(root)
        row1 = self.row1

        self.empty = tk.Button(
            row1,
            bg="#d9d9d9",
            width=2,
        )
        self.empty.pack(padx=2, side="left")

        self.division = tk.Button(
            row1,
            text="/",
            width=2,
            bg='#d9d9d9'
        )
        self.division.pack(padx=2, side='left')

        self.multiply = tk.Button(
            row1,
            text="*",
            width=2,
            bg="#d9d9d9"
        )
        self.multiply.pack(padx=2)

        # Second row
        self.row2 = tk.Frame(root)
        row2 = self.row2

        # row 1 buttons
        self.no7 = tk.Button(
            row2,
            text=7,
            width=2,
            bg="#d9d9d9"
        )

        self.no8 = tk.Button(
            row2,
            text=8,
            width=2,
            bg="#d9d9d9"
        )

        self.no9 = tk.Button(
            row2,
            text=9,
            width=2,
            bg='#d9d9d9'
        )

        # Pack the widjets
        self.title.pack()
        self.input_frame.pack(pady=18, padx=8)
        self.label.pack(side='left')
        self.input.pack(padx=5)
        self.row1.pack(pady=0)
        self.row2.pack(pady=5)
        self.no7.pack(padx=2, side='left')
        self.no8.pack(padx=2, side='left')
        self.no9.pack(padx=2)

        # Third Row
        self.row3 = tk.Frame(root)
        row3 = self.row3
        self.row3.pack(pady=0)

        self.no4 = tk.Button(
            row3,
            text="4",
            width=2,
            bg="#d9d9d9"
        )
        self.no4.pack(padx=2, side='left')

        self.no5 = tk.Button(
            row3,
            text="5",
            width=2,
            bg="#d9d9d9"
        )
        self.no5.pack(padx=2, side='left')

        self.no6 = tk.Button(
            row3,
            text='6',
            width=2,
            bg="#d9d9d9"
        )
        self.no6.pack(padx=2)

        # Forth Row
        self.row4 = tk.Frame(root)
        row4 = self.row4
        self.row4.pack(pady=5)

        self.no1 = tk.Button(
            row4,
            text="1",
            width=2,
            bg="#d9d9d9"
        )
        self.no1.pack(padx=2, side='left')

        self.no2 = tk.Button(
            row4,
            text="2",
            width=2,
            bg="#d9d9d9"
        )
        self.no2.pack(padx=2, side='left')

        self.no3 = tk.Button(
            row4,
            text='3',
            width=2,
            bg="#d9d9d9"
        )
        self.no3.pack(padx=2)

        tkinter.mainloop()


mygui = Calculator()
