import random

result = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for i in range(100):
    resultado = random.randint(1, 6)
    result[resultado] += 1

for valor, cont in result.items():
    print(f"O valor {valor} foi sorteado {cont} vezes.")
