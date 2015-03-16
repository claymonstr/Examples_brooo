# these loops are the same

i = 0

print 'while loop'

while i < 10:
    print i
    i = i + 1
    # this above is equivalent to below
    # i += 1

print 'for loop'


for i in range(10):
    print i