def find_maximum_difference(a, b):
#     # code implementation here...
    maximum = 0
    list = []
    list.append(max(a)-min(b))
    list.append(max(b)-min(a))
    maximum = max(list)
    return maximum

print(find_maximum_difference([1, 5, 600], [100, 7, 3, 29, 39]))
print(find_maximum_difference([1, 5, 600], [100, 7, 3, 602, 39]))

