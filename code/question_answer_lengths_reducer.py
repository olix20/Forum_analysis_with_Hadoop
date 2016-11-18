#!/usr/bin/python


'''

Test case: https://www.udacity.com/wiki/ud617/local-testing-instructions/student-times?nocache
test command: cat student_test_posts.csv | ./~_mapper.py | sort | ./~_reducer.py 

'''

import sys
#import numpy as np

oldKey = None
answer_lengths = []
question_length = 0 



for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    
    thisKey = data_mapped[0] #question_id
    node_type = data_mapped[1]
    




    if oldKey and oldKey != thisKey:
        
        answer_length_avg = sum(answer_lengths)/float(len(answer_lengths)) if len(answer_lengths) != 0 else 0    
        print "\t".join([str(oldKey), str(question_length),str(answer_length_avg)]) 

        
        answer_length_avg = 0
        question_length = 0 
        answer_lengths = []
        oldKey = thisKey;

    
    if node_type == "question" :
        question_length = int(data_mapped[2])

    else:
        answer_lengths.append(int(data_mapped[2]))

    oldKey = thisKey
    

# this capture the last node_id
if oldKey != None:
        answer_length_avg = sum(answer_lengths)/len(answer_lengths) if len(answer_lengths) != 0 else 0    
        print "\t".join([str(oldKey), str(question_length),str(answer_length_avg)]) 



