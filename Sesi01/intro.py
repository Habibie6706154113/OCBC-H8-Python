print(10)
print(type(10))
print('OCBC'.lower())
print(type('OCBC'))
print('ciat'.upper())

mix = [1, "a", 4, True, 5.1]
print(mix)

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[1:4])
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
print(a)

(s1, s2, s3, s4) = ('foo', 'bar', 'baz', 'qux')
print(s1)

MLB_team = {    
    'Colorado': 'Rockies',    
    'Boston': 'Red Sox',    
    'Minnesota': 'Twins',
}
print(MLB_team['Minnesota'])

MLB_team['Minnesota'] = "Twist"
MLB_team['Boston'] = MLB_team['Boston'].split('\n')
MLB_team['Boston'].append('White Fox')
print(MLB_team['Boston'])
MLB_team['Kansas City'] = 'Royals'
print(MLB_team)

person = {}
person['fname'] = 'Hack'
person['lname'] = 8
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}
print(person)
print(person['children'][1])
