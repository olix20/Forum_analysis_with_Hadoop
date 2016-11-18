#!/usr/bin/python


'''

Test case: https://www.udacity.com/wiki/ud617/local-testing-instructions/student-times?nocache
test command: cat student_test_posts.csv | ./~_mapper.py | sort | ./~_reducer.py 

'''

import sys
#import numpy as np

oldKey = None
tagCount = 0 
N = 10
topN = []

def add_and_sort():
    topN.append((oldKey,tagCount))

    topN.sort( key=lambda tup: tup[1],reverse=True)

    if len(topN) > N: 
        topN.pop(N)
    

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    
    thisKey = data_mapped[0] # tag name
    node_id = data_mapped[1]
    




    if oldKey and oldKey != thisKey:
        add_and_sort()

        tagCount = 0
        oldKey = thisKey;

    
 
    tagCount += 1
    oldKey = thisKey
    

# this captures the last tag
if oldKey != None:
    add_and_sort()



for t in topN:  
    print  t[0], "\t", t[1]


