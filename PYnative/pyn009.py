def num_palindrome(num):
    print(f'original number {num}')
    num_str = str(num)
    reverse = num_str[::-1]
    if reverse == num_str:
        print('it is a palindrome number.')
    else:
        print('not a palindrome number')


num_palindrome(121)
num_palindrome(152)