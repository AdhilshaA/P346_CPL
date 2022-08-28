contents = []
with open('input.txt') as inp:
    contents = inp.readlines()
dict1 = {}
i = 1
dict1[1] = list()
for content in contents:
    if content == '\n':
        i += 1
        dict1[i] = list()
        continue
    dict1[i].append(list((content.split())))

print(dict1)

