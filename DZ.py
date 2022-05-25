# 1. Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

# numbers=[1,2,3,4,5]
# sum=0
# for i in range(0,len(numbers), 2):
#     sum=sum+numbers[i]
# print("Сумма нечётных элементов = ", sum)    

# 2. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

# numbers = [1, 2, 3, 4, 5]
# powers = []
# i = 0

# for j in range (len(numbers)-1,(len(numbers)//2)-1,-1):
#     powers.append(numbers[i]*numbers[j])
#     i+=1    
# print(powers)

# 3. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# numbers = [1.1, 1.2, 3.1, 5, 10.01]
# numbers_after_point = []
# for i in numbers:
#   if i%1 != 0:
#     numbers_after_point.append(i%1) 
# print('%.2f' % (max(numbers_after_point) - min(numbers_after_point)))

# 4.	Написать программу преобразования десятичного числа в двоичное
# x = int(input("Введите натуральное число: "))
# n = ""
 
# while x > 0:
#  y = str(x % 2)
#  n = y + n
#  x = int(x / 2)
 
# print (n)