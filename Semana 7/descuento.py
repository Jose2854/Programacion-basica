#ALGORITMO 
#PREGUNTAR SI ES ESTUDIANTE (SI/NO)
#ESCRIBIR SI ES ESTUDIANTE O NO
#PREGUNTAR EL VALOR DE LA COMPRA
#ESCRIBIR EL VALOR DE LA COMPRA

#PSEUDOCODIGO 
#LEER SI ES ESTUDIANTE 
#LEER VALOR TOTAL DE LA COMPRA 
#SI ES ESTUDIANTE O LA COMPRA ES MAYOR O IGUAL A 200000, APLICA EL DESCEUNTO DEL 15%
#SI NO ES ESTUDIANTE O LA COMPRA ES MENOR QUE 200000, NO APLICA DESCUENTO 

estudiante=input("¿eres estudiante? (si/no)")
total=int(input("escriba el valor de su compra en pesos: "))
descuento= total*0.15

if estudiante == "si" or total >= 200000:
    print("el descuento es:", descuento)

else:
    print("no tienes descuento")
