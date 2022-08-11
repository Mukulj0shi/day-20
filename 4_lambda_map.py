
# map function takes a function and iterable as argument
# Map function return all the values based on the function in the form of list

#Example
# Program to list multiple of 5

list1 = range(10)
my_list = map(lambda a : a * 5, list1)

print(my_list)

#Convert object to a list
print(list(my_list))

