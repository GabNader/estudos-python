#pergunta palavra do player1
p1points = 0
p2points = 0
onepoint_letters = 'aeilnorst'
twopoint_letters = 'dg'
threepoint_letters = 'bcmp'
fourpoint_letters = 'fhvwy'
fivepoint_letter = 'k'
eightpoint_letters = 'jx'
tenpoint_letters = 'qz'
palavra1 = str(input('Player 1: ')).lower().strip()
palavra2 = str(input('Player 2: ')).lower().strip()
for letra in palavra1:
    if letra in onepoint_letters:
        p1points += 1
    if letra in twopoint_letters:
        p1points += 2
    if letra in threepoint_letters:
        p1points += 3
    if letra in fourpoint_letters:
        p1points += 4
    if letra in fivepoint_letter:
        p1points += 5
    if letra in eightpoint_letters:
        p1points += 8
    if letra in tenpoint_letters:
        p1points += 10
for letra in palavra2:
    if letra in onepoint_letters:
        p2points += 1
    if letra in twopoint_letters:
        p2points += 2
    if letra in threepoint_letters:
        p2points += 3
    if letra in fourpoint_letters:
        p2points += 4
    if letra in fivepoint_letter:
        p2points += 5
    if letra in eightpoint_letters:
        p2points += 8
    if letra in tenpoint_letters:
        p2points += 10
if p1points > p2points:
    print('Player 1 wins!')
elif p2points > p1points:
    print('Player 2 wins!')
else:
    print('Tie!')
