#!/usr/bin/python


'''

Test case: https://www.udacity.com/wiki/ud617/local-testing-instructions/student-times?nocache
test command: cat student_test_posts.csv | ./popular_times_mapper.py | sort | ./popular_times_reducer.py 

'''

import sys
#import numpy as np

oldKey = None






# Having trouble with installing numpy in Cloudera CentOS image.. i have to implement argmax function

def argmax (l):
    m = -1
    lmax = 0
    for i,e in enumerate(l):
            if e > m:
                lmax = i
                m = e
    return lmax


oldKey = None
hours = [0]*24



for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    
    thisKey = data_mapped[0] #author_id
    h = int(data_mapped[1])


    if oldKey and oldKey != thisKey:

        print oldKey, "\t", argmax(hours)
        hours = [0]*24        
        oldKey = thisKey;

    hours[h] = hours[h] + 1       
    oldKey = thisKey
    

# this capture the last author_id
if oldKey != None:
    print oldKey, "\t", argmax(hours) 



