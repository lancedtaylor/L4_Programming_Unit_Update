my_list = [69, 420, "motorbike", 1+2, "Lab 3"]
print(len(my_list))
my_list.append("new element")
my_list.insert(0, "beginning of list element")
my_list.remove(my_list[-1])
len(my_list)
print(my_list[0])
my_list[1] = 360
print(type(my_list))
my_list = tuple(my_list)
print(type(my_list))
print(my_list[0])
print(len(my_list))
#my_list[0] = "replacement tuple"
second_tuple = (7, 31, 69)
joined_tuple = my_list + second_tuple
print(joined_tuple)
your_list = list(joined_tuple)
print(type(your_list))
my_set = set(your_list)
len(my_set)
my_set.add("set element")
print(my_set)
my_set.add("set element")
print(my_set)
