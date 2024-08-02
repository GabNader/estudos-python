# Given two list of numbers, write a program to create a new list such that the new list
# should contain odd numbers from the first list and even numbers from the second list.

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
result_list = []
for n in list1:
    if n % 2 != 0:
        result_list.append(n)
for n in list2:
    if n % 2 == 0:
        result_list.append(n)
print(result_list)
