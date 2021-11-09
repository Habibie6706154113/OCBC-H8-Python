import sys

#x = 10
#if x > 5:
#    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

#assert('win32' in sys.platform), "This code runs on windows only"
#assert('linux' in sys.platform), "This code runs on Linux only"


#def check_coins(coins):
#    assert(coins == 10), "some coins fell down on the way"

#coins = 8

#try:
#    check_coins(coins)
#except:
#    raise Exception('Some message coins fell here--')

#def os_interaction():
#    assert('win32' in sys.platform), "This code runs on windows only"
#    assert('linux' in sys.platform), "This code runs on Linux only"
#    print("DOing Something")

#try:
#    os_interaction()
#    print('Masuk ke try block')
#except AssertionError as error:
#    print(error)
#    print('The os_interaction() function was not executed')

#try:
#    with open('file.log') as file:
#        read_data = file.read()
#except:
#    print('Could not open file.log')

#try:
#    with open ('sample.txt') as file:
#        read_data = file.read()
#except FileNotFoundError as error:
#    print(error)
#    print("%#")
#else:
#    print('Executing the else clause')

def os_interaction():
    assert('win32' in sys.platform), "This code runs on windows only"
    assert('linux' in sys.platform), "This code runs on Linux only"
    print("DOing Something")

try:
    os_interaction()
    print('Masuk ke try block')
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')