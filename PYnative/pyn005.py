# Write a function to return True if the first and last number of a given list is same.
# If numbers are different then return False.
def last_number(num):
    if num[0] == num[len(num)-1]:
        print('True')
    else:
        print('False')


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
last_number(numbers_x)
last_number(numbers_y)
