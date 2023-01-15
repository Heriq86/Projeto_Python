print("=" * 20)
print("Encontre o Vetor")
print("=" * 20)
vet = []

for c in range(0,8):
    n = int(input('Digite o valor do vetor:'))
    vet.append(n)
print("=" * 20)
for c in range(1):
  num = int(input('Informe o vetor que deseja pesquisar:'))
if num in vet:
     print('o valor {} está dentro do vetor e na posição {}'.format(num, vet.index(num)))
else:
 print('O valor não está no vetor:'.format(num))




 
