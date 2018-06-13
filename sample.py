f = open('datas.txt')
list = []
for line in f:
    list.append(line[:-1])
print(list)
f.close()
i = len(list)
print(i) 
