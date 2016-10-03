def selectionsort(list):
    for i in range(0, len(list)/2):
        maxind = i
        minind = i
        for j in range(i+1, len(list)-i):
            if list[j] < list[minind]:
                minind = j
            if list[j] > list[maxind]:
                maxind = j
        if(maxind == i and minind == len(list)-1-i):
            (list[minind], list[maxind]) = (list[maxind], list[minind])
        elif(minind == len(list)-1-i):
            (list[minind], list[i]) = (list[i], list[minind])
            (list[maxind], list[len(list)-1-i]) = (list[len(list)-1-i], list[maxind])
        else:
            (list[maxind], list[len(list)-1-i]) = (list[len(list)-1-i], list[maxind])
            (list[minind], list[i]) = (list[i], list[minind])

import random
import datetime

a = range(1, 10001)
random.shuffle(a)
t1 = datetime.datetime.now()
selectionsort(a)
t2 = datetime.datetime.now()
print 'Time:', t2 - t1
