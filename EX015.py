D = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
diaspreco = 60*D
kmpreco = 0.15*km
precofinal = diaspreco + kmpreco
print('Deve ser pago:  {}R$'.format(precofinal))

