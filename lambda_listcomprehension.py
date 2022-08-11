# Using list as an argument with lambda function.

my_list = lambda list1: [x + y for x in range(10) for y in range(5)]

# Here my_list should be provided with list as positional argument.
print(my_list([]))

x = my_list([])
print(x)

# Using filter function with x
# Convert the object to list using list function.

my_list1 = filter(lambda y: (y % 2 == 0), x)

print(my_list1)
print(list(my_list1))
