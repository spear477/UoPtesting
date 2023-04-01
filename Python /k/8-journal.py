import os
my_dict = {}
def read(filename):
    with open(filename) as file:
        for line in file.readlines():
            line = line.strip().split(':')
            key = line[0].strip()
            values = [item for item in line[1].strip().splitlines()]
            my_dict[key]=values
    return my_dict
read('input.txt')
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        for item in val:
            if item not in inverse:
                inverse[item] = [key]
            else:
                inverse[item].append(key)
    return inverse
invert = invert_dict(my_dict)
def write(invert, filename):
    with open(filename, 'w') as output:
        for key, value in invert.items():
            output.write("'{0}' : {1}\n".format(key,value))
    return format(filename)
filename = "output.txt"
write(invert, filename)