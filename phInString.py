def phNum(num):
    if len(num) != 13:
        return False
    #for i in range(0,1):
        if num[0] != '+':
          return False
    #for i in range(1,2):
        if num[1] != '9':
          return False
    for i in range(2,3):
        if num[2] != '1':
         return False
    for i in range(3,13):
        if not num[i].isdecimal():
         return False
    else:
         return True

##print(phNum('+91000000o000'))

num = 'Call me at +91XXXXX24 tomorrow. +910000000000 is my office.'
foundNumber = True
for i in range(len(num)):
     chunk = num[i:i+13]
     if phNum(chunk):
         print('Phone number found: ' + chunk)
         foundNumber = True

if not foundNumber:
    print('no phones found')
