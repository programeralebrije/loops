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