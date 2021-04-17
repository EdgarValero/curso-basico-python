def conversacion(mensaje):
  print('Hola')
  print('Como estas?')
  print(mensaje)
  print('Adios')

opcion = int(input('Elige una ioción (1, 2, 3): '))
if opcion == 1:
  conversacion('Elegiste la opción 1')
elif opcion == 2:
  conversacion('Elegiste la opción 2')
elif opcion == 3:
  conversacion('Elegiste la opción 3')
else:
  print('Escribe una opción correcta')