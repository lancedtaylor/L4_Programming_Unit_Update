def annual_net_income(gross_salary):
    # complete your function implementation here...
    gross_salary = float(gross_salary)
    # Assuming some tax rate for calculation
    tax_rate = 0
    if gross_salary >= 45000:
        tax_rate = 0.5
    elif gross_salary >= 30000 and gross_salary < 45000:
        tax_rate = 0.3
    else:
        tax_rate = 0.15
    net_salary = gross_salary * (1 - tax_rate)
    return net_salary
        
print(annual_net_income(60000))
print(annual_net_income(30000))
print(annual_net_income(20000))