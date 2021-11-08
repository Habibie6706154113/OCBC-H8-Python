x = 0
y = 5

if x < y:
    print('yes')

if 'aul' in 'fault':
    print('yes')

if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
    
print('After conditional')

if 'foo' in ['foo', 'bar', 'baz']:
    print('Outer condition is true')

    if 10 > 20:
        print('Inner condition 1')

    print('Between inner conditions')

    if 10 < 20:
        print('Inner condition 2')

    print('End of outer condition')
print('After outer condition')

x = 20

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
elif uang > hargaMajalah:
    print("beli majalah")
else:
    print("uang tidak cukup")

if 'f' in 'foo': print('1'); print('2'); print('3')

raining = True
print("Let's go to the", 'beach' if not raining else 'library')

if True:
    pass

print('foo')

n = 5
while n > 0:
    n -= 1
    print(n)

a = ['foo', 'bar']

print(a.pop(0))
print(a)

x = range(5)
for n in x:
    print(n)

d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)

for k in d:
    print(d[k])

for k in d.values():
    print(k)

for k in d.keys():
    print(k)

for k, v in d.items(): 
    print(k, ":", v) 