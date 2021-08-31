planets = ['Earth', 'Mars', 'Saturn', 'Venus']
print(planets)

our_world = ['Earth', ['United States', 'Canada', 'Mexico'], [1, 2, 3]]
print(our_world)

my_tuple = ('doctor', 'nurse', 'PA')
print(my_tuple)


# Mixed Data Type Tuples 

# you've already seen a string tuple
string_tuple = ("this", "contains", "string", "values")

# you can, of course, create tuples with numbers
number_tuple = (23, 23.5, 9, 144)

# like lists, you can create tuples with a mix of types
mixed_tuple = ("Bob", 33, "Sally", 29, "Spike", 8)


print(string_tuple , number_tuple, mixed_tuple)

items_witget_tuple = ('white', 'black', 'brown', '25')

print(items_witget_tuple)

items = ('widget', ['white', 'black', 'brown'], 25)

print(items)

colors_list = ['red', 'green', 'blue', 'yellow']
num_colors = len(colors_list)
print(num_colors)

# print the third item of the list
colors_list = ['red', 'green', 'blue', 'yellow']
print(colors_list[2])

# print the second item of the tuple
numbers_tuple = (22, 33, 44, 55)
print(numbers_tuple[1])

# print the last item of the list
colors_list = ['red', 'green', 'blue', 'yellow']
print(colors_list[-1])

# print the last item of the tuple
numbers_tuple = (22, 33, 44, 55)
print(numbers_tuple[-1])

colors_list = ['red', 'green', 'blue', 'yellow']

# access the last item with index `-1`
first_from_end = colors_list[-1]

# access the next-to-last item with index `-2`
second_from_end = colors_list[-2]

# access the second from the last item with index `-3`
third_from_end = colors_list[-3]

print(first_from_end)
print(second_from_end)
print(third_from_end)


colors_list = ['red', 'green', 'blue', 'yellow']
# Accessing Multiple Items Within a Range
# get the first three items
first_three_items = colors_list[0:3]

# get the middle two items
middle_two_items = colors_list[1:3]

print(first_three_items)
print(middle_two_items)

# Modifying Lists

# the starting list
contacts = ['Sally', 'Bob', 'Mary', 'Steven']

# Bob prefers to go by "Robert"
# Bob is at index 1 in the list
contacts[2] = "Robert"

print(contacts)

colors_list = ['white', 'white', 'white', 'white']
print(colors_list)

colors_list[0] = 'red'
colors_list[1] = 'green'
colors_list[2] = 'blue'
colors_list[3] = 'yellow'
print(colors_list)

colors_list[-1] = 'purple'
print(colors_list)


# Adding an Item to the End of the List

my_string = "Hello there Bob"

# splits string into list using space as the delimiter/separator
my_string_items = my_string.split()
print(my_string_items)

# but we forgot Sally!
# add 'and' and 'Sally' to the list
my_string_items.append("and")
my_string_items.append("Sally")

print(my_string_items)


my_list = [1, 2, 3]

# Oops! Forgot 3!
my_list.insert(3, 4)
print(my_list)

colors = ['red', 'white', 'blue']
colors.insert(1, 'green')
colors.insert(3, 'yellow')
print(colors)

numbers = [1, 2, 3, 4]

# delete item at index 2
del numbers[2]
print(numbers)

# the position of value 4 has changed
# its index went from 3 to 2, due to the deletion

# delete the first item
del numbers[0]
print(numbers)

# delete the last item
del numbers[-1]
print(numbers)


colors = ['green', 'white', 'green', 'yellw', 'yellw', 'white']
colors[4] = "yellow"
colors[3] = "yellow"
colors.remove("white")
colors.remove("white")
colors.append('purple')

print(colors)


# Creating a List from a Range of Numbers

numbers = list(range(1, 10))
print(numbers)