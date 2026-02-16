# benedict musa
# 16/2/2026
#program to calculate factorial of numbers
number= int(input("Enter the number x: "))
factorial = 1
for x in range(1,number+1):
    factorial *=x
print(f"{number}!={factorial}")