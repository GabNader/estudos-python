# Write a program to accept a string from the user and display characters that are present at an even index number.
texto = str(input('digite uma frase'))
print(f'Original String is {texto}')
print('Printing only even index chars')
for letra in range(0, len(texto), 2):
    print(texto[letra])
