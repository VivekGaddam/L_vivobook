import tkinter as tk
new_window=tk.Tk()
new_window.title("WINDOW")
new_window.wm_title("Window")
new_window.geometry("600x400+500+0")
a=new_window.winfo_screenmmwidth()
new_window.state("zoomed")
new_window.attributes("-fullscreen",True)
new_window.minsize(600,400)
new_window.maxsize(600,400)
new_window.resizable(0,0)
my_lable=tk.Label(text='Vivek Chandra Reddy',background='red',foreground='blue',font=("Arial" ,30, "bold"),relief="groove")
my_lable.pack()
print(a)
new_window.mainloop()


import tkinter as tk

def button_clicked():
    print("Button clicked!")

root = tk.Tk()

# Creating a button with specified options
button = tk.Button(root, 
                   text="Click Me", 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)

button.pack(padx=20, pady=20)

root.mainloop()


from tkinter import *

# Create a GUI app
app = Tk()

# Create a function with one parameter, i.e., of 
# the text you want to show when button is clicked
def which_button(button_press):
	# Printing the text when a button is clicked
	print(button_press)


# Creating and displaying of button b1
b1 = Button(app, text="Apple",
			command=lambda m="It is an apple": which_button(m))

b1.grid(padx=10, pady=10)

# Creating and displaying of button b2
b2 = Button(app, text="Banana",
			command=lambda m="It is a banana": which_button(m))
b2.grid(padx=10, pady=10)

# Make the infinite loop for displaying the app
app.mainloop()

from tkinter import *
app=Tk()
app.geometry("500x500")
app.title("Home Page")
def clicked():
    print(text.get())
    
text=Entry(app,text="enter your name ",width=30)
button=Button(text='submit',command=clicked)
text.pack()
button.pack()
app.mainloop()