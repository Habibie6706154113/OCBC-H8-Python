import person
import sys

def get_personal_info(name, age=18):
    print('Name:', name)
    print('Age:', age)
    print()

#required arguments
get_personal_info('Fikri', 24)
get_personal_info(27, "Adi")

#keyword arguments
get_personal_info(age=17, name='Lucy')

#default arguments
get_personal_info('Ria')

#Pass by reference vs value
def changeme( mylist ):
   mylist = [1, 2, 3, 4]
   print("Values inside the function  : ", mylist)

mylist = [10, 20, 30]
changeme( mylist )
print("Values outside the function : ", mylist)

#variable length argument
def buy(customer_name, *items):
    print('Name: ', customer_name)
    print('Buy: ', items)
    print()

buy('tia', 'eggs', 'wheat', 'flour', 'chocolate bar')
buy('roy')

def person_car(total_data, **kwargs):

  print('Total Data : ', total_data)
  for key, value in kwargs.items():
    print('Person : ', key)
    print('Car    : ', value)
    print()

person_car(3, jimmy='chevrolet', frank='ford', tina='honda')
person_car(3)
print()

#the anonymous functions
sum = lambda arg1, arg2: arg1 + arg2

print('Value of total : ', sum(10, 20))
print()

#return statement & scope of variables
total = 0

def sum( arg1, arg2 ):
   total = arg1 + arg2; 
   print("Inside the function local total   : ", total)
   return total

print("Outside the function global total - before : ", total)
total = sum( 10, 20 )
print("Outside the function global total - after  : ", total)
print()

#docstring
def sum_number(num1, num2):
  '''
  This function is used to sum of 2 variables.
  :param num1: Input number 1 | int or float
  :param num2: Input number 2 | int or float
  
  :return: num3: Sum of number | int or float
  '''
  num3 = num1 + num2
  return num3

print(sum_number.__doc__)

#python modules
print(person.name)
print(person.devices[1])
person.display('Good Night\n')

print(sys.path)
print()

print(dir(person))