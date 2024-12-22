import tkinter as tk

root = tk.Tk()
root.title("OOP")
root.geometry("500x500")
root.configure(bg="Green")

pangalan = tk.Entry(root)
pangalan.grid(row=0, column=0, padx=0, pady=100)

counter = 0
def display_text():
    global counter
    #print(f"{counter}. ", end="")
    #print(pangalan.get())
    
    print(f"{counter}. {pangalan.get()}")
    counter += 1

button = tk.Button(root, text="TAKBOOOOOOOOOOOOOOOO", command=display_text)

button.grid(row=1, column=0, padx=250, pady =20)

root.mainloop()
