def is_golden_number(n):
#     # function implementation ...
    boolean = False
    if n >= 1000 or n <= 0:
        return "Number not valid, needs to be between 0 and 1000"

    for a in range(1, n):
        b = n - a
        if a * b % 1000 == 0:
            boolean = True
            break
    return boolean

print(is_golden_number(70))