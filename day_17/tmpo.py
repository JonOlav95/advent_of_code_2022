from fractions import Fraction


a = Fraction(53/35)*Fraction(1000000000000 - 12)
a += 28
print(int(a))
