import requests
from tkinter import * 
from tkinter import scrolledtext
from tkinter import messagebox


ventana = Tk()

ventana.title("Hola Buen Mundo ")

ventana.geometry("600x400")

titulo = Label(ventana, text="GUI 1.0", font=("Arial Bold",24))

titulo.grid(row=0, column=0)

def clicked():
	#messagebox.showinfo('Message Tittle', 'Message Content')
	#messagebox.showerror('Message Tittle', 'Message Content')
	respuesta = requests.get("https://cat-fact.herokuapp.com/facts/random")
	if respuesta:
		#texto = 

		mensaje=respuesta.json()['text']
		id=respuesta.json()['id']
		texto=(id + ": " + mensaje + "\n\n")
		txt.insert(END, texto)

		#--------------- Aca podriamos cambiar para escribir en una base de datos con SQL Lite ------------------------#
		with open("output.txt", "a") as file:
			file.write(txt)	

		#--------------------------------------------------------------------------------------------------------------#
		
	else:
		messagebox.showerror('Message Tittle', 'UPS ERROR: '+ str(respuesta.status_code))
	pass

btn = Button(ventana, text="Buscar", command=clicked)

btn.grid(column=0, row=2)




txt = scrolledtext.ScrolledText(ventana, width=40, height=10)
txt.grid(column=1, row=1)



ventana.mainloop()