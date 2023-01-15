print("Calculo de abono salarial")
print("=" * 20)
print('Digite os Salarios para realizar o calculo de abono salarial dos seus colaboradores')
print("Para execultar o Calculo digite 0")
salarios = [] 
while True:
    salario = float(input('Salário: '))
    if salario == 0:
        break
    salarios.append(salario)

print('Detalhamento de Gastos e Abono')
print("=" * 20)

print('Salário - Abono')
abono = 0
minimo = 0
abonototal = 0
for s in salarios:
    abono = (s * 20) / 100
    if abono < 100:
       abono = 100
       minimo += 1
       abonototal += abono
    else:
       abonototal += abono
   
    print('R$ {:.2f} - R$ {:.2f}'.format(s, abono))

print('Foram processados {} colaboradores'.format(salarios))
print('Total gasto com abonos: R$ {:.2f}'.format(abonototal))
print('Valor mínimo pago a {} colaboradores'.format(minimo))
print('Maior valor de abono pago: R$ {:.2f} '.format(abono))
