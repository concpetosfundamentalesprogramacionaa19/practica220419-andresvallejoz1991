"""
Problema 2
Ingresar por teclado la variables: x,y,z
En base a las mismas realizar la siguiente operación:
y finalmente presentar en pantalla el siguiente reporte:
El valor de m, en base a las variables:
da como resultado:
m = ?
Andrés Vallejo Z
"""

print ("Ingrese la variable x")#Ingreso de la varriable x
x = input()
print ("Ingrese la variable y")#Ingreso de la varriable y
y = input()
print ("Ingrese la variable z")#Ingreso de la varriable z
z = input()
d = (float (x)-(float(y)/float(z))) #Numerador de la operacion
n = (float (x)+(float (y)/float (z))) #Denominador de la operacion
m = (float (n)/float (d)) #Operacion resultante



print ("El valor de m en base a las variables:\nX =%s\n\tY =%s\n\t\tZ = %s\nDan como resultado: \n\t\t\t m =%.2f " % (x,y,z,m))