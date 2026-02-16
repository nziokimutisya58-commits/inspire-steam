



int(input("Enter your gross salary :"))

if salary < 50000:
    Tax = (2.5 * salary) / 100
    net_salary = salary - tax
    
print(f"Gross salary = {salary}")
print(f"Net salary = {net_salary}")
print(f"Tax = {tax}")
