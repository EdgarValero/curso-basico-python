def run():
  poblacion_paises = {
    'Argentina': 426654411,
    'Brasil': 54796547854,
    'Colombia': 36745218
  }

  print(poblacion_paises['Argentina'])

  for pais in poblacion_paises.keys():
    print(pais)

  for pais in poblacion_paises.values():
    print(pais)

  for pais, poblacion in poblacion_paises.items():
    print(pais + ' tiene ' + str(poblacion) + ' habitantes')

if __name__ == '__main__':
  run()