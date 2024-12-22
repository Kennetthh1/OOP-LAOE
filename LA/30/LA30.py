import tkinter as tk

root = tk.Tk()
root.title("Basic Tkinter Widgets")
root.geometry("300x200")
favorite_anime = ("Naruto Shippuden")
frame = tk.Frame(root)
frame.pack(pady=20)


def display_text():
    print(f"My Favorite anime is {favorite_anime}")
    

button = tk.Button(root, text="Pindutin moko beybe", command=display_text)
button.pack(pady=10)

root.mainloop()
