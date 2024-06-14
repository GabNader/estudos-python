from random import randint
guesses = 0
com_number = randint(1, 9)
user_number = 0
while user_number != 'exit':
    user_number = int(input('Number: '))
    guesses += 1
    if user_number == com_number and guesses > 1:
        print(f'You got it! I thought of the number {com_number}, and you guessed it in {guesses} tries! ')
        break
    if user_number == com_number and guesses == 1:
        print(f'You got it! I thought of the number {com_number}, and you guessed it in a single try!! ')
        break
    elif user_number > com_number:
        print(f'Lower than {user_number}...')
    elif user_number < com_number:
        print(f'Higher than {user_number}...')




