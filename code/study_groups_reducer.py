#!/usr/bin/python


'''

Test case: https://www.udacity.com/wiki/ud617/local-testing-instructions/student-times?nocache
test command: cat student_test_posts.csv | ./popular_times_mapper.py | sort | ./popular_times_reducer.py 

'''

import sys
#import numpy as np

oldKey = None
studentList = []



for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    
    thisKey = data_mapped[0] #node id



    if oldKey and oldKey != thisKey:

        print oldKey, "\t".join(studentList)
        studentList = []     
        oldKey = thisKey;


    studentList.append(data_mapped[1])     # append student id 
    oldKey = thisKey
    

# this capture the last author_id
if oldKey != None:
    print oldKey, "\t", "\t".join(studentList)



