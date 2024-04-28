import tkinter
from tkinter import messagebox
import qrcode


window = tkinter.Tk()
window.title("Link a QR")
window.geometry('500x400')
window.resizable(False, False)
window.config(bg="gray")

tkinter.Label(window, text='Link a QR', font="arial 15" ).place(x=200,y=5) 
tkinter.Label(window, text="introduzca el link") .place(x=200,y=50)

link = tkinter.StringVar()
linkenter= tkinter.Entry(window, textvariable=link, width=50,  ).place(x=105,y=100)


def QR():
    texto = str(link.get())
    img = qrcode.make(texto)
    img.save("codigo_qr.png")
    link.set("")
    messagebox.showinfo( "generado","generado correctamente")



tkinter.Button(window,text="generar QR", command=QR).place(x=210,y=130)






window.mainloop()