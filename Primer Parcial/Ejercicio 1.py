#algoritmo

#Pedir el nombre 
#guardar el nombre
#solicitar el consumo de agua mensual en metros cubicos
#guardar consumo

#Pseudocidigo 
#Inicio
#leer el nombre
#leer el consumo de agua mensual
#Comparar el consumo si es mayor o igual a 1 y SI es menor o igual  a 15
#Si el consumo esta entre 1 y 15 muestra el nombre, la categoria: Bajo consumo y el mensaje :¡Excelente! Eres un usuario responsable del agua
#Comparar el consumo si es mayor o igual a 15 y SI es menor o igual  a 30
#Si el consumo esta entre 16 y 30 muestra el nombre, la categoria: Consumo normal y el mensaje: Tu consumo está dentro del promedio del hogar
#Comparar el consumo si es mayor a 30
#Si el consumo es mayor a 30 muestra el nombre, la categoria: Alto consumo y el mensaje: Atención: tu consumo es alto, revisa posibles fugas
#Clasificar el consumo mensual del agua


nombre=input("ingrese su nombre: ")
print("Hola",nombre)
consumo=int(input("ingrese su consumo mensual de agua en metros cubicos(numero entero)"))

if consumo >= 1 and consumo <= 15:
    print(nombre,"tienes Bajo consumo","¡Excelente! Eres un usuario responsable del agua")
elif consumo > 15 and consumo <= 30:
    print(nombre,"tienes Consumo normal","Tu consumo está dentro del promedio del hogar")
elif consumo > 30:
    print(nombre,"tienes Alto consumo","Atención: tu consumo es alto, revisa posibles fugas")
else:
    print("Dato inválido, Error: el consumo debe ser mayor a 0")
  
