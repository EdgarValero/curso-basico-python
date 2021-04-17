# Conversor 2.0
def conversor(tipo_pesos, valor_dolar):
  pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
  pesos = float(pesos)
  dolares = pesos / valor_dolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
  conversor("colombianos", 3875)
elif opcion == 2:
  conversor("argentinos", 65)
elif opcion == 3:
  conversor("mexicanos", 24)
else:
  print("Ingresa una opción correcta por favor")

# Conversor 1.0
# # Conversion de Pesos a Dolares
# pesos = input("¿Cuántos pesos colombianos tienes?: ")
# pesos = float(pesos)
# valor_dolar = 3875
# dolares = pesos / valor_dolar
# dolares = round(dolares, 2)
# dolares = str(dolares)
# print("Tienes $" + dolares + " dolares")

# # Conversion de Bolivares a Dolares
# pesos = input("¿Cuántos bolivares venezolanos tienes?: ")
# pesos = float(pesos)
# valor_dolar = 1900000
# dolares = pesos / valor_dolar
# dolares = round(dolares, 2)
# dolares = str(dolares)
# print("Tienes $" + dolares + " dolares")