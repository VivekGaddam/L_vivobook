from tkinter import *

app = Tk()
app.title("Number Pad")
app.geometry("600x600")
app.config(background="#ffff99")

entered_number = StringVar()

def button_clicked(number):
    entered_number.set(entered_number.get() + str(number))

def operation_clicked(operation):
    entered_number.set(entered_number.get() + operation)

def evaluate_expression():
    try:
        result = str(eval(entered_number.get()))
        entered_number.set(result)
    except Exception as e:
        entered_number.set("Error")

entry = Entry(app, textvariable=entered_number, width=20, font=("Arial", 30, "bold"),
              background="black", fg="white")
entry.pack(padx=20, pady=20) 

button_grid = []
frame = Frame(app)
frame.pack() 

for row in range(3):
    for col in range(3):
        number = row * 3 + col + 1
        button = Button(frame, text=number, font=("Arial", 30, "bold"), command=lambda n=number: button_clicked(n)) 
        button_grid.append(button)
        button.grid(row=row, column=col, padx=10, pady=10)
        button.config(bg='blue', fg='white', width=5, height=2) 


button_zero = Button(frame, text='0', font=("Arial", 30, "bold"), command=lambda: button_clicked(0))
button_zero.grid(row=3, column=1, padx=10, pady=10)
button_zero.config(bg='blue', fg='white', width=5, height=2)


operations = ['+', '-', '*', '/', '=']
for i, op in enumerate(operations):
    if op == '=':
        button = Button(frame, text=op, font=("Arial", 30, "bold"), command=evaluate_expression)
    else:
        button = Button(frame, text=op, font=("Arial", 30, "bold"), command=lambda o=op: operation_clicked(o))
    button.grid(row=3 + (i // 2), column=(i % 2) * 2, padx=10, pady=10)
    button.config(bg='blue', fg='white', width=5, height=2)

app.mainloop()
