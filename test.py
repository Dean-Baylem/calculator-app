from tkinter import *
from tkinter import ttk

class Calculator:
    """A scientific calculator GUI App"""

    def __init__(self):


        # ----------------- Variables ------------------

        self.x = "0"
        self.y = ""
        self.z = ""
        self.operator = ""
        self.result = 0

        # ----------- GUI Initialization --------------

        self.window = Tk()
        self.window.title("Calculator")
        self.window.config(height=600, width=800)

        # ------------------ Canvas --------------------

        self.canvas = Canvas(height=50, width=500)
        self.result = self.canvas.create_text(450, 35, text=self.x, fill="black", font=("Birch std", 12, 'italic'))
        self.canvas.grid(column=0, row=0, columnspan=4)


        # ------------------ Buttons ------------------

        self.button1 = Button()
        self.button1.config(width=20, text='1', command=lambda: self.update_x("1"))
        self.button1.grid(column=1, row=5)

        self.button2 = Button()
        self.button2.config(width=20, text='2', command=lambda: self.update_x("2"))
        self.button2.grid(column=2, row=5)

        self.button3 = Button()
        self.button3.config(width=20, text='3', command=lambda: self.update_x("3"))
        self.button3.grid(column=3, row=5)

        self.button4 = Button()
        self.button4.config(width=20, text='4', command=lambda: self.update_x("4"))
        self.button4.grid(column=1, row=4)

        self.button5 = Button()
        self.button5.config(width=20, text='5', command=lambda: self.update_x("5"))
        self.button5.grid(column=2, row=4)

        self.button6 = Button()
        self.button6.config(width=20, text='6', command=lambda: self.update_x("6"))
        self.button6.grid(column=3, row=4)

        self.button7 = Button()
        self.button7.config(width=20, text='7', command=lambda: self.update_x("7"))
        self.button7.grid(column=1, row=3)

        self.button8 = Button()
        self.button8.config(width=20, text='8', command=lambda: self.update_x("8"))
        self.button8.grid(column=2, row=3)

        self.button9 = Button()
        self.button9.config(width=20, text='9', command=lambda: self.update_x("9"))
        self.button9.grid(column=3, row=3)

        self.button0 = Button()
        self.button0.config(width=20, text='0', command=lambda: self.update_x("0"))
        self.button0.grid(column=2, row=6)

        self.addition = Button()
        self.addition.config(width=20, text='+', fg="Green", command=lambda: self.setup("+"))
        self.addition.grid(column=4, row=5)

        self.subtraction = Button()
        self.subtraction.config(width=20, text="-", fg="Green", command=lambda: self.setup("-"))
        self.subtraction.grid(column=4, row=4)

        self.multiplication = Button()
        self.multiplication.config(width=20, text="*", fg="Green", command=lambda: self.setup("*"))
        self.multiplication.grid(column=4, row=3)

        self.division = Button()
        self.division.config(width=20, text="/", fg="Green", command=lambda: self.setup("/"))
        self.division.grid(column=4, row=2)

        self.squared = Button()
        self.squared.config(width=20, text="x\u00b2", command=self.square_number)
        self.squared.grid(column=0, row=2)

        self.equals = Button()
        self.equals.config(width=20, text="=", fg="Green", command=self.equal)
        self.equals.grid(column=4, row=6)

        self.clear = Button()
        self.clear.config(width=20, text="C", fg="Red", command=self.clear_values)
        self.clear.grid(column=4, row=1)


        # --------------- Main Loop ---------------

        self.window.mainloop()


        # --------------- Methods ----------------


    def setup(self, operator):
        self.y = self.x
        self.x = "0"
        self.operator = operator

    def update_x(self, button):
        if self.x == "0":
            self.x = ""
        self.x += button
        self.canvas.itemconfig(self.result, text=self.x)

    def add_num(self):
        if self.z == "":
            num = float(self.x) + float(self.y)
            self.z = str(num)
            self.x = "0"
            self.y = "0"
            self.canvas.itemconfig(self.result, text=num)
        else:
            num = float(self.z) + float(self.x)
            self.z = str(num)
            self.x = "0"
            self.y = "0"
            self.canvas.itemconfig(self.result, text=num)

    def subtract_num(self):
        if self.z == "":
            num = float(self.x) - float(self.y)
            self.z = str(num)
            self.x = "0"
            self.y = "0"
            self.canvas.itemconfig(self.result, text=num)
        else:
            num = float(self.z) - float(self.x)
            self.z = str(num)
            self.x = "0"
            self.y = "0"
            self.canvas.itemconfig(self.result, text=num)

    def multiply_num(self):
        if self.z == "":
            num = float(self.x) * float(self.y)
            self.z = str(num)
            self.x = "0"
            self.y = "0"
            self.canvas.itemconfig(self.result, text=num)
        else:
            num = float(self.z) * float(self.x)
            self.z = str(num)
            self.x = "0"
            self.y = "0"
            self.canvas.itemconfig(self.result, text=num)

    def divide_num(self):
        if self.z == "":
            num = float(self.y) / float(self.x)
            self.z = str(num)
            self.x = "0"
            self.y = "0"
            self.canvas.itemconfig(self.result, text=num)
        else:
            num = float(self.z) / float(self.x)
            self.z = str(num)
            self.x = "0"
            self.y = "0"
            self.canvas.itemconfig(self.result, text=num)

    def square_number(self):
        if self.z == "":
            ans = float(self.x) * float(self.x)
            self.x = ans
            self.canvas.itemconfig(self.result, text=self.x)
        else:
            ans = float(self.z) * float(self.z)
            self.z = ans
            self.canvas.itemconfig(self.result, text=self.z)

    def equal(self):
        if self.operator == "+":
            self.add_num()
        if self.operator == "-":
            self.subtract_num()
        if self.operator == "*":
            self.multiply_num()
        if self.operator == "/":
            self.divide_num()

    def clear_values(self):
        self.x = "0"
        self.y = ""
        self.z = ""
        self.canvas.itemconfig(self.result, text=self.x)

Calculator()
