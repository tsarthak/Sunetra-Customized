# """
# line 1
# line 2
# ...
# """
# # for ...
# # while

# """
# while <condition>:
#     statements...
# """

# # num = 0

# # while num < 10:
# #     # print(f"Inside loop num = {num}")
# #     num = num + 1
# #     print(f"Inside loop num = {num}")

# # print("---------")

# # num = 20

# # while num > 0:
# #     num = num - 1
# #     print(f"Inside loop num = {num}")

# # print(num)

# num = 5

# while True:
#     num -= 1 # num = num - 1
#     if num <= 0:
#         break

# print(num)

# num = 5

# while True:
#     if num >= 0:
#         num -= 1 # num = num - 1
#         continue
#     else:
#         break

# print(num)


"""
*
**
***
****
*****

Think of this exercise as typing a * and then moving on to the next line
One observation - the number of stars in a row is equal to the row number

We can use this fact, and design our loop in such a way that for each row,
we print a fixed number of stars = the row number.

We can control this using two loops.
1. one loop goes from top to bottom
2. the second loop goes from left to right

the top loop is the row loop and the nested loop is the left to
right loop

in each row, we print stars equal to the row number and move
one position to the right. then at the end, we just move to the
next line and bring back the horizontal position marker to
the start to start printing all over again.
"""
rows = 0
columns = 0

while rows <= 4:
    columns = 0
    while columns <= rows:
        # print(f"Row: {rows}, Column: {columns} ")
        print('*', end='')
        columns += 1
    print()
    rows += 1

"""
*****
****
***
**
*
"""
