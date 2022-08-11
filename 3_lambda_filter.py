# filter function takes a function and list as argument.
# Return: For the condition which are True those items will be added to new list.

#Example
# Program to filter out only the even items from a list

my_list = [1, 15, 24, 27, 30, 26]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)


