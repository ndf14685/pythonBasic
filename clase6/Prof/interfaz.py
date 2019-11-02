import requests

respuesta = requests.get('https://cat-fact.herokuapp.com/facts/random')

if respuesta:
	print("Todo OK", respuesta.status_code)
else:
	print("Error", respuesta.status_code)



