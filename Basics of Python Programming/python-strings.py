# collections

# collections - arrays
# in python - array is called a list.
# more specifically, python lists are dynamic arrays


'''
immutable types - int, float, string
'''

# id
x = 14
y = 14
print(f"Integer example (initial case): id of x = {id(x)}, id of y = {id(y)}")


y += 1
print(f"Integer example (after update): id of x = {id(x)}, id of y = {id(y)}")

str1 = "This is a string"
str2 = str1
print(f"String example (initial case): id of str1 = {id(str1)}, id of str2 = {id(str2)}")
str2 += " and something more"
print(f"String example (after update): id of str1 = {id(str1)}, id of str2 = {id(str2)}")

'''
mutable types - list, dictionaries, sets
'''
print("---------------------------------------------")
l1 = [1,2,3]
print(id(l1), l1)

l1[0] = 21
print(id(l1), l1)

l2 = l1
print(id(l2), l2)

l2[1] = 22
print(id(l2), l2)
print("---------------------------------------------")
print(f"List example (initial case): id of l1 = {id(l1)}, id of l2 = {id(l2)}")

print("---------------------------------------------")
print(id(l1[0]))
l1[0] = 45
print(id(l1[0]))
print("---------------------------------------------")
