import tkinter as tk
from tkinter import messagebox

from calculator import calculate, square_root, square


class Calculator:

    def __init__(self, root):

        self.root = root
        self.root.title("Professional Calculator")
        self.root.geometry("350x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.expression = ""
        self.first_number = None
        self.operator = None
        self.reset_display = False

        self.create_display()
        self.create_buttons()

    def create_display(self):

        self.display = tk.Entry(
            self.root,
            font=("Arial", 25),
            bg="#313244",
            fg="white",
            justify="right",
            bd=0
        )

        self.display.pack(
            padx=15,
            pady=25,
            ipady=20,
            fill="x"
        )

        self.display.insert(0, "0")

    def create_buttons(self):

        button_frame = tk.Frame(
            self.root,
            bg="#1e1e2e"
        )

        button_frame.pack(expand=True, fill="both", padx=10, pady=10)

        buttons = [
            ["C", "⌫", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["+/-", "0", ".", "="],
            ["√", "x²", "**", ""]
        ]

        for row_index, row in enumerate(buttons):

            for col_index, value in enumerate(row):

                if value == "":
                    continue

                button = tk.Button(
                    button_frame,
                    text=value,
                    font=("Arial", 16, "bold"),
                    bg="#45475a" if value not in ["=", "C"] else "#89b4fa",
                    fg="white",
                    activebackground="#585b70",
                    bd=0,
                    command=lambda v=value: self.button_click(v)
                )

                button.grid(
                    row=row_index,
                    column=col_index,
                    padx=4,
                    pady=4,
                    sticky="nsew"
                )

        for i in range(4):
            button_frame.columnconfigure(i, weight=1)

        for i in range(6):
            button_frame.rowconfigure(i, weight=1)

    def update_display(self, value):

        self.display.delete(0, tk.END)
        self.display.insert(0, str(value))

    def button_click(self, value):

        current = self.display.get()

        if value.isdigit():

            if self.reset_display or current == "0":
                current = value
                self.reset_display = False

            else:
                current += value

            self.update_display(current)

        elif value == ".":

            if self.reset_display:
                current = "0"
                self.reset_display = False

            if "." not in current:
                self.update_display(current + ".")

        elif value in ["+", "-", "*", "/", "%", "**"]:

            try:
                self.first_number = float(current)
                self.operator = value
                self.reset_display = True

            except ValueError:
                messagebox.showerror("Error", "Invalid Number")

        elif value == "=":

            if self.operator is not None:

                try:
                    second_number = float(current)

                    result = calculate(
                        self.first_number,
                        second_number,
                        self.operator
                    )

                    self.update_display(self.format_result(result))

                    self.first_number = None
                    self.operator = None
                    self.reset_display = True

                except (ValueError, ZeroDivisionError, OverflowError) as error:
                    messagebox.showerror("Error", str(error))
                    self.clear()

        elif value == "C":

            self.clear()

        elif value == "⌫":

            if not self.reset_display:
                current = current[:-1]

                if current in ["", "-"]:
                    current = "0"

                self.update_display(current)

        elif value == "+/-":

            try:
                result = -float(current)
                self.update_display(self.format_result(result))

            except ValueError:
                pass

        elif value == "√":

            try:
                result = square_root(float(current))
                self.update_display(self.format_result(result))
                self.reset_display = True

            except ValueError as error:
                messagebox.showerror("Error", str(error))

        elif value == "x²":

            try:
                result = square(float(current))
                self.update_display(self.format_result(result))
                self.reset_display = True

            except ValueError:
                messagebox.showerror("Error", "Invalid Number")

    def format_result(self, result):

        if isinstance(result, float) and result.is_integer():
            return str(int(result))

        return str(result)

    def clear(self):

        self.expression = ""
        self.first_number = None
        self.operator = None
        self.reset_display = False

        self.update_display("0")


if __name__ == "__main__":

    root = tk.Tk()

    calculator = Calculator(root)

    root.mainloop()