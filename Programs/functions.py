import sys

def multiply(num1, num2):
    return num1 * num2

def add(num1, num2):
    return num1 + num2

print multiply(3, multiply(2, 2))
print 3 * (2 * 2)

try:
    print 5/0
except:
    print '{}'.format(sys.exc_info())
##finally:
##    print 'here again'