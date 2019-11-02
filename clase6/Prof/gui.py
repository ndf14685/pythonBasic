import requests

from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

ventana = Tk()

ventana.title("Hello Gui World")
ventana.geometry('800x400')

title = Label(ventana, text="GUI 1.0", font=("Arial Bold", 24))
title.grid(column=0, row=0)

def clicked():
	respuesta = requests.get('https://cat-fact.herokuapp.com/facts/random')
	
	if respuesta:
		mensaje = respuesta.json()['text']
		id = respuesta.json()['_id']

		texto = id + ": " + mensaje + "\n\n"
		
		txt.insert(END,texto)
		
		with open("output.txt", "a") as file:
			file.write(texto)
		
	else:
		messagebox.showerror('Ocurrio un error', 'Ocurrio un error ' + str(respuesta.status_code))
	

btn = Button(ventana, text="Buscar", command= clicked)
btn.grid(column=0, row=1)

txt = scrolledtext.ScrolledText(ventana, width=80, height=10)
txt.grid(column=1, row=0)


ventana.mainloop()

		
		