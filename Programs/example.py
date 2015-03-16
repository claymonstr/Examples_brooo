#integer assignment
i = 0

#string assignment - strings are immutable
pc = 'lenovo'
print '1', pc
pc = 'hp'
print '2', pc

#list assignment with appending example
numList = [1, 2, 3, 4]
print '3', numList
numList.append(5)
print '4', numList
numList = []
print '5', numList

#dictionary assignment with new key assignment
mydict = {
    'Sony': 'Cameras',
    'Asus': 'monitors'
}
print '6', mydict

mydict['HP'] = 'Printers'

print '7', mydict

#Booleon plus none type
flag = True
antiFlag = False
Nobody = None