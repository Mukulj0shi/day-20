# format :
# 1st) action to be performed,
# 2nd) for statement.
# 3rd) conditional statement


list_even = [x * 2 for x in range(1, 100)]
print(list_even)

list_even = [x for x in range(100, 200) if x % 2 == 0]
print(list_even)

