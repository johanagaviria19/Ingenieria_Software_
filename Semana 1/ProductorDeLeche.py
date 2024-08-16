litros_producidos = float(input("Digite la cantidad de litros producidos: "))

precio_por_galon = float(input("Digite el precio por galón: "))

galones = litros_producidos / 3.785

monto_a_recibir = galones * precio_por_galon
print(f'El monto a recibir es: {monto_a_recibir}')

