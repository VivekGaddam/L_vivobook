import tkinter as tk


"""
    # importing the qrcode library  
    import qrcode  
    # generating a QR code using the make() function  
    qr_img = qrcode.make("Welcome to Javatpoint.")  
    # saving the image file  
    qr_img.save("qr-img.jpg")  

"""
import qrcode 
new_window=tk.Tk()
def click():
    a=text_field.get()
    qr_img = qrcode.make(a)
    qr_img.save("qr-img.jpg")
 
text_field=tk.Entry(width=30,font=("Arial",20,"bold"))
button=tk.Button(text="submit",command=click)
text_field.pack()
button.pack()
new_window.mainloop()