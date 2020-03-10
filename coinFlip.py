#! python3

import random

heads = 0
tails = 0

for i in range (1,1001):
    if random.randint(0,1) == 1:
        #print('HEADS!')
        heads = heads + 1
        if heads == 500:
            print('Halfway done')
    else:
        #print('TAILS!')
        tails = tails + 1

print('you got ' + str(heads) + ' HEADS! and ' + str(tails) + ' TAILS')
