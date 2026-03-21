#algoritmo

#Pedir el nombre 
#guardar el nombre
#solicitar la edad
#guardar edad

#Pseudocidigo 
#Inicio
#leer el nombre
#leer la edad 
#Comparar si la edad es mayor o igual a 0 y SI es menor o igual  a 11
#Si la edad esta entre 12 y 17 muestra el nombre, 
#Comparar si la edad si la edad es mayor o igual a 0 y SI es menor o igual  a 17 
#Si la edad esta entre 18 y 30 muestra el nombre, la categoria: y el mensaje:
#Comparar si la edad  es mayor a 30
#Si la edad es mayor a 30


nombre=input("ingrese su nombre: ")
print("Hola",nombre)
edad=int(input("ingrese su edad(numero entero)"))

if edad >= 0 and edad <= 11:
    print(nombre,"niño","corresponde atencion pediatrica")
elif edad > 12 and edad <= 17:
    print(nombre,"joven","Corresponde a atención para adolescentes")
elif edad > 18 and edad <= 59:
    print(nombre,"adulto","Corresponde a atención para adultos")
elif edad > 60 and edad <=100:
    print(nombre,"adulto","Corresponde a atención para adultos")
else:
    print("Dato inválido, Error: la edad debe ser menor a 100")
