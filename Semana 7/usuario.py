#ALGORITMO
#PEDIR USUARIO 
#ESCRIBIR USUARIO
#PEDIR CONTRASEÑA
#ESCRIBIR CONTRASEÑA

#PSEUDOCODIGO
#LEER USUARIO 
#LEER CONTRASEÑA 
#SI USUARIO ES JOSEE Y CONTRASEÑA ES JOSE2854, DECIR ACCESO CONCECIDO 
#SI USUARIO Y CONTRASEÑA NO COINCIDE, ESCRIBIR ACCESO DENEGADO 

usuario=input("escriba su usuario: ")
contrasena=input("escribir contrasena: ")

if usuario == "josee" and contrasena == "jose2854":
    print("acceso concedido, bienvenido!")

else:
    print("acceso denegado, datos incorrectos ")
