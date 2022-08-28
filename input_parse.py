f = open('input.txt')
lines = f.readlines()
print(lines)
lineindex = 0
curr_input = 0
while lineindex < len(lines):
    if lines[lineindex][0] == '#':
        curr_input += 1
        lineindex += 1
    if curr_input == 1:
        seed = int(lines[lineindex].split()[0])
        lineindex += 1
    elif curr_input == 2:
        length = int(lines[lineindex].split()[0])
        lineindex += 1
    elif curr_input == 3:
        li = lines[lineindex].split()
        for i in range(len(li)):
            li[i] = int(li[i])
        print(li)
        lineindex += 1
    elif curr_input == 4:
        mat = []
        while lines[lineindex][0] != '#':
            li = lines[lineindex].split()
            for i in range(len(li)):
                li[i] = int(li[i])
            mat.append(li)
            lineindex += 1
        print(mat)
    else:
        pass

