## Collections discussion

# str, list, dict, set
# str - immutable
# list, dict, set - mutable

# example of a char - 'a' '1' '\t'
# example of string - 'a1\t'
# languages - C++, JAVA chars usually represented by single quotes, and strings are represented by double quotes
# 'a' - char, "a" - string
# python - strings are
# 'a' - string, "a" - string
# "This is a special 'string'"

print("Hello World") # example of a string
print('H')

# linear collections
# arrays, lists
# homogeneous and heterogeneous collections
# int arr[] - homogeneous collection/ array
# arr[]     - heterogeneous array

hetero_arr = [1, 1.23423423, "Hello Sunetra", [1,2,3]]

print(f"my_str: {my_str}, {id(my_str)}")
my_str = 'Jello'
print(f"my_str: {my_str}, {id(my_str)}")

print(f"Char at index 0 {my_str[0]}")
print(f"Char at index 1 {my_str[1]}")

# splice operation
# str[start_idx: stop_idx]
print(f"Variation1: First 3 characters of my_str = {my_str[0:3]}")
# no start index
print(f"Variation2: First 3 characters of my_str = {my_str[:3]}")
# no end index
print(f"Variation3: characters of my_str = {my_str[2:]}")
# no index
print(f"Variation3: n characters of my_str = {my_str[:]}")
# negative index examples
print(f"Variation3: last char of my_str = {my_str[len(my_str) - 1]}")
print(f"Variation3: last char of my_str = {my_str[-1]}")
print(f"Variation3: second last char of my_str = {my_str[-2]}")

print(f"Variation3: last char of my_str = {my_str[-5: -3]}")
print(f"Variation3: last char of my_str = {my_str[-5: 2]}")


my_list = [1,2,3,4,5]

print(f"Splice example with a list: {my_list[0: 3]}")

# special functions with strings

print(f"String to Uppercase {my_str}, {my_str.upper()}")
print(f"String to lowercase {my_str}, {my_str.lower()}")
my_string_with_spaces = "    hello. there are some spaces at the start of this string and at the end          "
print(f"lstrip: remove spaces from the lhs: '{my_string_with_spaces.lstrip()}'")
print(f"rstrip: remove spaces from the rhs: '{my_string_with_spaces.rstrip()}'")
print(f"strip: remove spaces from both ends: '{my_string_with_spaces.strip()}'")


blank_string = "{} {} {}"
print(blank_string.format("Hello", 1, "World"))
print(blank_string.format("Goodbye", 2, "World"))