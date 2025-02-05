import tkinter as tk

# Create main window
window = tk.Tk()
window.geometry('500x200')
window.configure(bg='lightblue')
window.title("My First GUI")

# Create a label
label = tk.Label(window,
                 text="What is your name?",
                 font=('Arial',24)
                 )
label.pack(padx=10,pady=10)

# Removes placeholder text when user clicks
def on_entry_click(event):
    if name.get() == placeholder:
        name.delete(0, tk.END)
        name.config(fg="black")  # Change text color

# Restores placeholder if entry is empty
def on_focus_out(event):
    if not name.get():
        name.insert(0, placeholder)
        name.config(fg="gray")

# Placeholder text
placeholder = "Enter your name..."

# Create Entry widget
name = tk.Entry(window, font=("Arial", 14), fg="gray")
name.insert(0, placeholder)  # Insert placeholder text
name.bind("<FocusIn>", on_entry_click)  # Remove text on focus
name.bind("<FocusOut>", on_focus_out)  # Restore if empty
name.pack(padx=20, pady=15)

# Function to get text from the text box
def show_intro():
    intro = name.get()
    if intro.strip():
        label_output.config(text=f"Nice to meet you, {intro}!", fg="black")
    else:
        label_output.config(text="Invalid", fg="red")

# Create a button
submit = tk.Button(window, text="Submit", command=show_intro, font=("Arial", 12))
submit.pack()

# Label to show output
label_output = tk.Label(window, text="", font=("Arial", 14))
label_output.pack(pady=10)


# Start the GUI
window.mainloop()