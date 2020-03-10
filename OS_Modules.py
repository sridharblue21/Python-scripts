##import os
##
##totalSize = 0
##for filename in os.listdir('D:\\SRI\\pyScripts'):
##    if os.path.isfile(os.path.join('D:\\SRI\\pyScripts', filename)):
##        totalSize = totalSize + os.path.getsize(os.path.join('D:\\SRI\\pyScripts', filename))
##    else:
##        continue
##print(totalSize)


#PlainText example
file = open('D:\\SRI\\pyScripts\\test.txt')
print(file.read())


#shelve module
import shelve
shelveFile = shelve.open('data')
shelveFile['lang'] = ['js','c#','c++','c']
print(list(shelveFile.values()))
