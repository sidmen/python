files = ['a.txt', 'b.txt', 'c.txt']
for file in files:
    readfile = open(file, 'r')
    content = readfile.read()
    print(content)
    readfile.close()
