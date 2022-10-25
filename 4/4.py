file = open('test.txt')
a = sorted([[int(x) for x in line.split()][1:] for line in file])

for i in range(len(a)):
    print(i + 1, a[i])