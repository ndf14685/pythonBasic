from tkinter import * 
from tkinter import scrolledtext
from tkinter import messagebox


ventana = Tk()

ventana.title("Hola Buen Mundo ")

ventana.geometry("600x400")

titulo = Label(ventana, text="GUI 1.0", font=("Arial Bold",24))

titulo.grid(row=0, column=0)

def clicked():
	messagebox.showinfo('Message Tittle', 'Message Content')
	#messagebox.showerror('Message Tittle', 'Message Content')
	pass

btn = Button(ventana, text="Buscar", command=clicked)

btn.grid(column=0, row=2)




txt = scrolledtext.ScrolledText(ventana, width=40, height=10)
txt.grid(column=1, row=1)



ventana.mainloop()