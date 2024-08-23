
alto = float(input("Escribe la altura de la alberca: "))
largo = float(input("Escribe el largo de la alberca: "))
precio = float(input("Escribe el precio del metro cúbico: "))

volumen = alto * largo

pago = volumen * precio

print(f"El pago por {volumen} litros de agua es: ${pago:.2f}")
