import tkinter as tk
from tkinter import ttk

from constants import (AMOUNT_ERROR, BACKGROUND_COLOR, BUTTON_COLOR,
                       CURRENCIES, CURRENCY_ERROR, RATES)


def entry_clicked(event: tk.Event) -> None:
    event.widget.delete(0, tk.END)


def clear() -> None:
    combo_1.set("From Currency")
    combo_2.set("To Currency")
    entry.delete(0, tk.END)
    result.delete(0, tk.END)
    error_label.config(text="")
    entry.insert(0, "Amount")
    result.insert(0, "Result")


def convert() -> None:
    error_label.config(text="")
    from_currency = combo_1.get()
    to_currency = combo_2.get()
    if from_currency not in CURRENCIES or to_currency not in CURRENCIES:
        error_label.config(text=CURRENCY_ERROR)
        return
    try:
        amount = float(entry.get())
    except ValueError:
        error_label.config(text=AMOUNT_ERROR)
        return
    rate = RATES[(from_currency, to_currency)]
    ans = amount * rate
    result.delete(0, tk.END)
    result.insert(0, str(ans))


# window configuration
window = tk.Tk()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{x}x{y}")
window.config(bg=BACKGROUND_COLOR)
window.title("Currency Converter")

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# labels
label_1 = tk.Label(window, text="Convert From:", bg=BACKGROUND_COLOR)
label_1.grid(row=0, column=0, padx=10, pady=10)
label_2 = tk.Label(window, text="Convert To:", bg=BACKGROUND_COLOR)
label_2.grid(row=0, column=1, padx=10, pady=10)

# combo boxes
combo_1 = ttk.Combobox(window, values=CURRENCIES)
combo_1.set("From Currency")
combo_1.grid(row=1, column=0, padx=10, pady=10)

combo_2 = ttk.Combobox(window, values=CURRENCIES)
combo_2.set("To Currency")
combo_2.grid(row=1, column=1, padx=10, pady=10)

# entries
entry = tk.Entry(window)
entry.insert(0, "Amount")
entry.grid(row=2, column=0, padx=10, pady=10)
entry.bind("<Button-1>", entry_clicked)

result = tk.Entry(window)
result.insert(0, "Result")
result.grid(row=2, column=1, padx=10, pady=10)
result.bind("<Button-1>", entry_clicked)

# buttons
clear_button = tk.Button(window, text="Clear", command=clear, bg=BUTTON_COLOR)
clear_button.grid(row=3, column=0, padx=10, pady=10)

convert_button = tk.Button(window, text="Convert", command=convert, bg=BUTTON_COLOR)
convert_button.grid(row=3, column=1, padx=10, pady=10)

# error_label for error handling
error_label = tk.Label(window, bg=BACKGROUND_COLOR)
error_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the application
window.mainloop()
