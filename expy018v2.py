from math import sin, cos, tan, radians
a = float(input('Digite o ângulo em graus:'))
sin = sin(radians(a))
cos = cos((radians(a)))
tan = (tan(radians(a)))
print(f'ângulo de {a}º tem seno {sin:.4f}, cosseno {cos:.4f} e tangente {tan:.4f}')

