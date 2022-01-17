from sys import argv

param = len(argv)

with open('bakery.csv', 'r', encoding='utf-8') as f:
    if param == 1:
        print(f.read())
    elif param == 2:
        for line in f.readlines()[int(argv[1])-1:]:
            print(line.strip())
    else:
        for line in f.readlines()[int(argv[1]) - 1:int(argv[2])-1]:
            print(line.strip())

