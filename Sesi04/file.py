from os import read


try:
    file = open('Hack8_Sample_Text.txt')
finally:
    file.close()

with open("sample.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")

f = open('sample.txt', 'r', encoding='utf-8')
print(f.read(4))
print(f.read())

with open("sample.txt",'r',encoding = 'utf-8') as f:
    data = f.read(4)
    print(data)
    data = f.read(4)
    print(data)

    n = f.tell()
    print(n)

    data = f.read(12)
    print(data)
    n = f.tell()
    print(n)

    f.seek(15)
    data = f.read(3)
    print(data)

    f.seek(0)
    for line in f:
        print(line, end= ' ')

    f.seek(0)
    data = f.readline()
    print(data)