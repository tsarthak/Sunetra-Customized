"""
String formatting - a few ways
"""

# string interpolation
# I can form a string

"""
%s - placeholder
int main()
{
printf("Hello, %s. How is your %s doing?", "Sunetra.", "Cat")
}
"""
# tuple

print("Old way 1: ", "Hello %s. How is your %s doing? Is she %d years old" % ("Sunetra" , "Cat", 3))

# %s - format specifier
# %d - integer format specifier
# %f - floating point ....
# %c - char

print("Old way 2: ",
    "Hello %(name)s. How is your %(pet)s doing? Is she %(age)d years old" % 
    {
        "pet": "Cat",
        "name": "Sunetra",
        "age": 3
    }
)

print("New way 1: ",
    "Hello {}. How is your {} doing? Is she {} years old".format(
        "Sunetra" , "Cat", 3
    )
)

print("New way 2: ",
    "Hello {name1}. How is your {pet} doing? Is she {age} years old".format(
        name1="Sunetra" , pet="Cat", age=3
    )
)

# string interpolation or f-strings
person_name = "Sunetra"
person_pet = "Cat"
person_pet_age = 3
print("New way 3: ",
    f"Hello {person_name}. How is your {person_pet} doing? Is she {person_pet_age} years old"
)

print("------------")

l = 10
b = 20

print(
    "The area of a rectangle with length = {}, breadth = {} is = {}".format(
        l, b, l * b
    )
)

print(
    "The area of a rectangle with length = {rect_len}, breadth = {rect_wid} is = {rect_area}".format(
        rect_area=l * b, rect_len=l, rect_wid=b
    )
)

print("%f is a floating point number" % 0.3)