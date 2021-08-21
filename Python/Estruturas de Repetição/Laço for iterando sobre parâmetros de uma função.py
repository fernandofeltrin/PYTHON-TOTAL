def cadastra(**kwargs):
  for key, value in kwargs.items():
    print(f'Parâmetro {key}, Dado/Valor: {value}')

gerente = cadastra(Nome = 'Fernando',
                   Credencial = 3509,
                   Email = 'fernando2rad@gmail.com')
