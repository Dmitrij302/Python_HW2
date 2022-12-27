# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

n = int(input('Введите число: '))
total = 0
num_list = []
for i in range(1, n + 1):
    num = (1 + 1 / i) ** i
    if num - int(num) == 0: 
        num = int(num)
    else:
        num = round(num, 2)
    num_list.append(num)
    total += num
print(f'n = {n} -> {num_list}\nСумма {total}')