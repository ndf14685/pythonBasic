import requests 


respuesta = requests.get("https://cat-fact.herokuapp.com/facts/random")

print(respuesta);


if respuesta:
	print("TODO OK")
else:
	print("TODO ERROR")


print("-----------------------------------------------------")
print(respuesta.text)
print("-----------------------------------------------------")
print(respuesta.headers)
print("-----------------------------------------------------")
print(respuesta.json())
#print(respuesta.json(), type=(respuesta.json()))

print("-----------------------------------------------------")




print(respuesta.json())[text]
print(respuesta.json())[id]
