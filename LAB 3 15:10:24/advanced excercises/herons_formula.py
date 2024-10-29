def herons_formula(a, b, c):
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

print(herons_formula(3, 4, 5))  # Output: 6.0