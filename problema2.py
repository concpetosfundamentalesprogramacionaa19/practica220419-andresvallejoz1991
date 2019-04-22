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

print ("Ingrese la variable x")
x = input()
print ("Ingrese la variable y")
y = input()
print ("Ingrese la variable z")
z = input()
d = (float (x)-(float(y)/float(z)))
n = (float (x)+(float (y)/float (z)))
m = (float (n)/float (d))






print ("El valor de m en base a las variables:\nX =%s\n\tY =%s\n\t\tZ = %s\nDan como resultado: \n\t\t\t m =%.2f " % (x,y,z,m))