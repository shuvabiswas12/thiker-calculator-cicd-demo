from tkinter import Tk, Button, Entry, StringVar


class Calculator:
    def __init__(self, master: Tk) -> None:
        master.title("Calculator")

        # ------- display field -------
        self.result_var = StringVar()
        Entry(
            master,
            textvariable=self.result_var,
            width=16,
            font=("Arial", 24),
            bd=10,
            insertwidth=2,
            bg="powder blue",
            justify="right",
        ).grid(row=0, column=0, columnspan=4, sticky="nsew")

        # ------- buttons -------
        self._create_buttons(master)

    # ------------------------------------------------------------------
    # helpers
    # ------------------------------------------------------------------
    def _create_buttons(self, master: Tk) -> None:
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
            ("C", 5, 0, 4),  # span 4 columns so the Clear key feels right
        ]

        for item in buttons:
            text, row, col, *opt = item
            colspan = opt[0] if opt else 1
            Button(
                master,
                text=text,
                padx=20,
                pady=20,
                font=("Arial", 18),
                command=lambda t=text: self._on_button_click(t),
            ).grid(row=row, column=col, columnspan=colspan, sticky="nsew")

        # Make the layout nicely resize‑able
        for i in range(4):
            master.columnconfigure(i, weight=1)
        for i in range(6):
            master.rowconfigure(i, weight=1)

    def _on_button_click(self, char: str) -> None:
        if char == "C":
            self.result_var.set("")
        elif char == "=":
            expr = self.result_var.get()
            try:
                # WARNING: eval is handy here but unsafe in real apps
                self.result_var.set(eval(expr))
            except Exception:
                self.result_var.set("Error")
        else:
            self.result_var.set(self.result_var.get() + char)


# ----------------------------------------------------------------------
# the function main.py wants
# ----------------------------------------------------------------------
def run_calculator() -> None:
    root = Tk()
    Calculator(root)
    root.mainloop()
