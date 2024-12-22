import tkinter  as tk



your_name = "KENNETH_CORBILLA"
your_section = "BSIT_2ABC"
window = tk.Tk()
window.title("OOP")
window.geometry("500x350")


frame = tk.Frame(window)
frame.pack(pady=20)

label = tk.Label(frame, text = (f"OOP {your_name } {your_section}"))
label.grid(row=0, column=0, padx=10, pady=10)

window.mainloop()
