import tkinter

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km:.2f}")

window = tkinter.Tk()
window.minsize(width=150, height=150)
window.title("Mile to Km Converter")
window.config(padx=10, pady=10)

# Entry
miles_input = tkinter.Entry(width=15)
miles_input.insert(index=0, string=0)
miles_input.grid(row=0, column=1)

# Label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)
miles_label.config(padx=10, pady=10)

is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(row=1, column=0)
is_equal_label.config(padx=10, pady=10)

km_result_label = tkinter.Label(text="0")
km_result_label.grid(row=1, column=1)
km_result_label.config(padx=10, pady=10)

km_label = tkinter.Label(text="Km")
km_label.grid(row=1, column=2)
km_label.config(padx=10, pady=10)

# Button
calculate_button = tkinter.Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=2, column=1)
calculate_button.config(padx=10, pady=10)

window.mainloop()