# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

num = int(input())
sum_dig = 1
num_list = []

for i in range(num):
    sum_dig *= i + 1
    num_list.append(sum_dig)

print(num_list)