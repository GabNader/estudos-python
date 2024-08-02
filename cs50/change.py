change = int(input('change owed: '))
while True:
    if change < 0:
        print('Negative number? nonsense, try again.')
        change = int(input('change owed: '))
    if change == 0:
        print('zero?!')
        break
    if change > 0:
        break
twenty_five = 0
ten = 0
five = 0
cent = 0
while change >= 25:
    change -= 25
    twenty_five += 1
while change >= 10:
    change -= 10
    ten += 1
while change >= 5:
    change -= 5
    five += 1
while change > 0:
    change -= 1
    cent += 1
if twenty_five > 0:
    print(f'Quarter(s) = {twenty_five}')
if ten > 0:
    print(f'Dimes = {ten}')
if five > 0:
    print(f'Nickels = {five}')
if cent > 0:
    print(f'Penny = {cent}')
