def phNum(num):
    if len(num) != 13:
        return print('Number must be 13 digits including country code')
    for i in range(0,1):
        if num[i] != '+':
          return print('Include + Symbol')
    for i in range(1,2):
        if num[i] != '9':
          return print('Invalid Country Code')
    for i in range(2,3):
        if num[i] != '1':
         return print('Invalid Country Code')
    for i in range(3,13):
        if not num[i].isdecimal():
         return print('Invalid Number')
    else:
         print('Number Okay')


phNum('00000')
