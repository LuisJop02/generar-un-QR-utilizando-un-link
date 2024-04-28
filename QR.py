import os
import tkinter
from tkinter import Label, messagebox
import qrcode
from PIL import Image, ImageTk


window = tkinter.Tk()
window.title("Link a QR")
window.geometry('400x200')
window.resizable(False, False)
window.config(bg="gray")

tkinter.Label(window, text='Link a QR', font="arial 15" ).place(x=150,y=5) 
tkinter.Label(window, text="introduzca el link") .place(x=150,y=50)

link1 = tkinter.StringVar()
linkenter= tkinter.Entry(window, textvariable=link1, width=50,  ).place(x=40,y=100)


def QR():
        link = str(link1.get())
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(link)
        link1.set("")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img = img.resize((200, 200))
        qr_name = link.replace("://", "_").replace("/", "_").replace(".", "_") + ".png"
        qr_path = os.path.join("qr_codes", qr_name)
        img.save(qr_path)
        
        
        messagebox.showinfo( "generado","generado correctamente")



tkinter.Button(window,text="generar QR", command=QR).place(x=150,y=130)

if __name__ == "__main__":
    if not os.path.exists("qr_codes"):
        os.makedirs("qr_codes")






window.mainloop()