from USUARIO import planes_Hogar, años,telefonia
from json import*



def menu():
 print("-------------------------------------")
print("---------Movistar-------------------")
print("-------------------------------------")

print(input("QUE USARIO ERES: 1 cliente 2  Admin   "))


opcion1 = 1
opcion2 = 2
if opcion1: 
    print("BIENVENIDO AL SERVICIO MOVISTAR EN QUE PODEMOS AYUDARTE")
    print("1 PLAN HOGAR (WIFI Y TELFONIAFIJA)")
    punto1=1
    if punto1:
     print(planes_Hogar)

    
    print("2 TELEFONIA MOVIL ")
    punto2=2
    if punto2:
     print(telefonia)
     
    print("3 CONSULTAR AÑOS")
    punto3 = 3
    if punto3:
      print(años)

    print("4. SALIR")
    punto4 = 4
    if punto4:
       menu()

else:opcion2
print("Bienvenido  administrador que deseas ver")
print("1 lista de usarios registrados")

print("2. ingresar un nuevo usario")
print("3. eleminar un usario")
print("4 salir")