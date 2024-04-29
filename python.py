import tkinter as tk

def button_click():
    # This function will be executed when the button is clicked
    print("Button clicked!")

# Create the main window
root = tk.Tk()
root.title("My Python App")

# Create a label
label = tk.Label(root, text="Welcome to my Python App!")
label.pack()

# Create a button
button = tk.Button(root, text="Click me!", command=button_click)
button.pack()

# Run the Tkinter event loop
root.mainloop()
