import tkinter as tk
import tkinter.messagebox


class SIS:

    def __init__(self):

        self.main_window = tkinter.Tk()
        root = self.main_window

        root.geometry("400x300")
        root.resizable(False, False)
        root.title("SIS")

        self.title = tkinter.Label(
            root,
            text="Student Imformation System",
            font=("Helvetica", 10)
        )

        self.row1 = tk.Frame(root)
        row1 = self.row1
        self.label1 = tk.Label(
            row1,
            text="STNO",
            padx=17
        )
        self.input1 = tk.Entry(
            row1,
            width=15,
            justify='center'
        )

        self.row2 = tk.Frame(root)
        row2 = self.row2
        self.label2 = tk.Label(
            row2,
            text="STName",
            padx=10
        )
        self.input2 = tk.Entry(
            row2,
            width=15,
            justify='center'
        )

        self.title.pack(pady=10)
        self.row1.pack()
        self.label1.pack(side='left', pady=5)
        self.input1.pack(pady=5)
        self.row2.pack()
        self.label2.pack(side='left', pady=5)
        self.input2.pack(pady=5)

        tkinter.mainloop()


tst = SIS()
