"""
Part 1:

Arithmetic and logical operations

Calculate income tax

"""

# flow control
# if else
# if <condition>:
#     ...
#     ...
#     ...
#     ...
# else:
#     ...
#     ...
#     ..
# ..

# nested if else
# if <conditions>:
#     if <another set of conditions>:
#         <i am inside the nested if>
#     else:
#     <iam inside the main if>
# else:

# if elif ladder

# if <conds1>:
#     ...
# elif <conds2>:
#     ...
# elif <conds3>:
#     ...
# else:

"""
Mutually exclusive items: 
A and B are mutually exclusive, then A and B cannot happen together

Indepdent items:

"""

# if <cond>:

# if <cond>:

# if <cond>:

# if <cond>:

# check if a number is even

# num = int(input("Enter a integer value: "))

# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")

# num = int(input("Enter a integer value: "))

# if num % 2 == 0:
#     print(f"{num} is divisible by 2")
#     if num % 4 == 0:
#         print(f"{num} is divisible by 4")
#     elif num % 8 == 0:
#         print(f"{num} is divisible by 8")
# else:
#     if num % 3 == 0:
#         print(f"{num} is divisible by 3")
#     if num % 5 == 0:
#         print(f"{num} is divisible by 5")

# num = int(input("Enter a integer value: "))

# if num % 2 == 0 and num % 5 == 0:
#     print(f"{num} is divisible by 2 and 5")
# elif num % 2 == 0:
#     print(f"{num} is divisible by 2")
# elif num % 5 == 0:
#     print(f"{num} is divisible by 5")
# else:
#     print(f"{num} is not divisible by 2 and 5")


# if num % 2 == 0:
#     print(f"{num} is divisible by 2")
# if num % 5 == 0:
#     print(f"{num} is divisible by 5")
# if num % 2 != 0 and num % 5 != 0:
#     print(f"{num} is not divisible by 2 or 5")

# tax calculator
"""
1. 0-20k - 0% tax
2. 20-50k - 10% tax
2. 50-100k - 15% tax
2. 100-200k - 25% tax
2. 200K+ 35% tax

35k
15k -> 10%

115k
15k - 25% 
50k - 15%
30k - 10%
20k - 0%
"""

salary = float(input("Please enter your salary: "))

amounts = []

if salary >= 200000:
    bracket_amount = (salary - 2000000)
    salary -= bracket_amount
    amounts.append(bracket_amount * 0.35)
if salary >= 100000:
    bracket_amount = (salary - 100000)
    salary -= bracket_amounts
    amounts.append(bracket_amount * 0.25)
if salary >= 50000:
    bracket_amount = (salary - 50000)
    salary -= bracket_amount
    amounts.append(bracket_amount * 0.25)