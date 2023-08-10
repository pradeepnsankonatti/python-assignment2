#DEMOSTRATION BASIC LIST METHODS

# 1] index() method

#first letus create list named names
names=['cat','bat','rat','mat','sat']
names.index('sat')

# 2] append() method
spam=['ram','shyam','bham','somu']
spam.append('nagu')
spam

# 3] insert() method
krishna=['murali','shyam','gopal','govind']
krishna.insert(4,'radhe')
print(krishna)

# 4]  remove() method
name=['radha','rukmini','satyabhama','jambavati','sita']
name.remove('sita')
print(name)

# 5] reverse() method
name.reverse()
print(name)

# 6] sort() method
num=['9','-5','0','2','7']
num.sort()
print(num)

# 7]del statement
carlist=['ford','kia','fortuner','safari','harrier','thar']
del carlist[0] #deleting 1 item in list by  specifying index value
print(carlist)

# 8] clear()
carlist.clear() #clear() will empties the list
print(carlist)  


# 9] pop() function
tables=['5','10','15','18','20','25']
tables.pop(3)  #pop removes item from list by taking index value
print(tables)