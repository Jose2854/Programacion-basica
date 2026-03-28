#ALGORITMO 
#PEDIR LA EDAD
#ESCRIBIR EDAD
#PREGUNTAR SI TIENE LA LICENCIA VIGENTE 
#ESCRIBIR SI TIENE O NO LICENCIA 

#PSEUDOCODIGO
#LEER LA EDAD
#LEER SI TIENE LICENCIA VIGENTE 
#SI TIENE 18 AÑOS O MAS Y SI TIENE LICENCIA PUEDE CONDUCIR 
#SI NO TIENE LICENCIA Y NO TIENE 18 AÑOS NO PUEDE CONDUCIR


edad=int(input("ingrese su edad: "))
licencia=input("¿tienes licencia de conducir? (si/no): ")

if edad >=18 and licencia== "si":
    print("puedes conducir legalmente!")

else:
    print("no puedes conducir, necesitas tener 18 añor y tener licencia" )
