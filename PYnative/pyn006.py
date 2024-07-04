# Iterate the given list of numbers and print only those numbers which are divisible by 5
list_x = [10, 20, 33, 46, 55]
print(f'Given list is {list_x}')
print('Divisible by 5')
for n in list_x:
    if n % 5 == 0:
        print(n)
