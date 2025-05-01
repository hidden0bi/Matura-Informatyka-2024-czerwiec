file = open('slowa.txt','r')
lines = file.readlines()
counter = 0
for line in lines:
    line = line.strip()
    for i in range(len(line) - 2):
        if line[i-1] == 'k' and line[i + 1] == 't':
            counter += 1
            break
print(counter)