"""
Descripcion: Programa que solicta nombre de vendedor
y valor de ventas de ese vendedor, luego con esa información
se calcula la comisión por ventas en base al 13% del
valor de ventas
Desarrollado por: Sebastian Ponce Vidal
Fecha: 5/02/2025
"""
nombre=input("Suministre el nombre de un vendedor ")
ventas=input("Suministre el valor de ventas de ese vendedor ")
comision_venta = round((float(ventas)*0.13),2)
print(f"El vendedor {nombre} obtuvo una comisión por {comision_venta}")