#
# Calcular numeros primos e colocar numa lista
#
count_module = 0
numbers = [];
for i in range(2, 10001):
    for j in range(2, i):
        # print(f'{i}', end=' ')
        # print(f'{j}')
        # print(f'{i} mod {j}:{i%j}')
        if j > 2 and i % 2 == 0:
            break
        if j > 5 and i % 5 == 0:
            break
        if i % j == 0:
            count_module += 1
    # print(f'{i} module counter: {count_module}')
    if count_module == 0:
        numbers.append(i)
    count_module = 0
print(f'\n{numbers}')
print(len(numbers))
