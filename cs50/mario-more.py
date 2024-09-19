height = int(input('height: '))
space = height - 1
for coluna in range(height+1):
    print('' * (height - coluna), end='')
    for linha in range(coluna):
        print('#', end='')
        print('#', end='')
    print('\n')
    space -= 1