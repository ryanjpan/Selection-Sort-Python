def insertionsort(list):
    for i in range(0, len(list)):
        minind = i
        for j in range(i+1, len(list)):
            if list[j] < list[minind]:
                minind = j
        (list[minind], list[i]) = (list[i], list[minind])

import random
import datetime

a = range(1, 10001)
random.shuffle(a)
t1 = datetime.datetime.now()
insertionsort(a)
t2 = datetime.datetime.now()
print 'Time:', t2 - t1
