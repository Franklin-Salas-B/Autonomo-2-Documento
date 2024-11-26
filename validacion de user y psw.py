# validacion de user y psw
import hashlib
# Base de datos de usuarios (En la practica se utilizaria una base de datos real)
ususarios = {"admin": hashlib.sha256("password123".encode()).hexdigest(),"usuario1": hashlib.sha256("contraseña123".encode()), "usuario2": hashlib.sha256("clave123".encode().hexdigest())}
             def validar_usuario(usuario, contraseña):
             usuario(str) : El nombre de ususario
             Args:
             contraseña(str) : La contraseña de ususario.
returns:
bool: True si el ususarios y la contraseña son validos, False caso contrario
# verificar si el susuario existe en la base de datos
if ususario in ususarios:
# verificar si la contraseña coincide con la almacenada en la base de datos
contraseña_hash = hashlib.sha256(contraseña.encode()).hexdigest()
if contraseña_hash == ususarios[ususario] :
      return True return False
# Ejemplo de uso
usuario = input("Ingrese su usuario: ")
contraseña = input("Ingrese su contraseña: ")
if validar_usuario(usuario , contraeña ): 
print ("usuario y contraseña validos")
else:
print ("Ususario o contraseña invalidos" )
