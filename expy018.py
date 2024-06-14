import math
a = float(input('Quantos graus tem o ângulo?'))
an = math.radians(a)
s = math.sin(an)
c = math.cos(an)
t = math.tan(an)
print(
    f"Se o ângulo tem {a}º, o seno é {s}, o cosseno é {c} e a tangente é {t}")
