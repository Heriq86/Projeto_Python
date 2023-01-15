print("Informar vetores e localizar posição")
print("=" * 20)
num = []
for cont in range(0, 8):
    num.append(int(input('Digite um valor: ')))
print(num)
print("=" * 20)
for cont in range(1):
    n1 = int(input('Digite um valor: '))
    if n1 not in num:
        print('Não existe esse valor dentro do vetor')
    else:
        print(f"O valor digitado se encontra na posição {num.index(n1)} do vetor.")