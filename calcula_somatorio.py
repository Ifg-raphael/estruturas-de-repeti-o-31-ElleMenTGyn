n = int(input())   # lê n(limite somatório)
s = 0              # acumula a soma

if n >= 2:
    # somatório de i = 2 até n(inclusive)
    for i in range(2, n + 1):
        s += 1 / (i - 1)
else:
    # se n < 2, retorna 0.00
    s = 0.00

# imprime o resultado
print(f"{s:.2f}")
