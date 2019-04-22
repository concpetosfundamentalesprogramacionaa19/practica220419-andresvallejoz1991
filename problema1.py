"""
Problema 1
Descuento mensual y Pago
Andrés Vallejo Z
"""
Horas = 100 #Numeros de horas establecidas
print ("Ingrese costo de horas") #Ingreso del costo por hora
costo = input()
SMensual =int (Horas)*int(costo) #Sueldo mensual de empleado
Descuento = int (SMensual)*(0.10) #Calculo del descuento del seguro Social
Total = int (SMensual)-(Descuento) # Total a pagar ya con descuento

print ("El descuento del Seguro social es :  %d\tEl sueldo Mensual es : %d"  % (Descuento,Total)) 
