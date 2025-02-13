import json
def abrirJSon():
  dicfinal={}
  with open("./servicios.json","r") as openFile:
      dicfinal= json.load()

def guardarJSon(dic):
  with open("./servicios.json","w") as outFile:
    json.dump(dic,outFile)



def planes_Hogar():
 
 opcion1 = 1 
 if opcion1:
  print("CONSULTANDO PLANES HOGAR")
  print("1. PLAN HOGAR CON 600 MEGAS CON FIBRA OPTICA, TELEVISION Y TELEFONIA POR 120.000 EL PRIMER MES DESPUES 150.000       ")
  print("2 PLAN HOGAR CON 2000 MEGAS CON FIBRA OPTICA, TELEVISION Y TELEFONIA POR 150.000 EL PRIMER MES DESPUES 200.000 + HBOMAX  ")
 plan1=1
 plan2=2
 if plan1:
     print("Dentro de unos dias vendra los tecnicos para instalar el plan hota en tu casa")
 if plan2:
   print("Dentro de unos dias vendra los tecnicos para instalar el plan hota en tu casa ")
def telefonia():
  print(input("r","ingrese el numero celular"))
 
  print("los planes de telefonia que tenemos son")
  print("1.por solamente 14.000 en los primeros 3 meses te llevas 22GB de internet gratis los servicios como whatsapp facebook y sms luego de los tres meses pagas 35.000")
opcionn1=1
if opcionn1:
  print("ya  estas con el nuevo plan muchas gracias")

  print("2 por solamente 35.000 en los primeros 3 meses te llevas 40GB de internet gratis los servicios como whatsapp facebook y sms luego de los tres meses pagas 55.000 + spotify includio")
opcionn2=2
if opcionn2:
  print("ya  estas con el nuevo plan muchas gracias")


def años():
  años= abrirJSon()
  print (input("ingrese la ide o usario (Adriana Quintero diaz) "))
  if años >= 10:
    print("muy bien tienes:" [años])
  elif años <= 9:
    print("ya casi llegas a  los 10 años")
  else:
     print ("muchas gracias por escoger nuestro servicio")
     





    

