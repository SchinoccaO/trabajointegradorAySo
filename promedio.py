numeros = []
#crear lista vacia

#pedir 5 numeros
for i in range(5):
    while True:
        try:
            numero = float(input(f"ingrese el numero {i + 1}: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Error. Ingrese un numero valido")

#calcular promedio

suma = 0

for numero in numeros:
    suma += numero
promedio = suma / len(numeros)

print("Lista de numeros ingresados: ")
print(numeros)

print(f"Promedio: {promedio}")