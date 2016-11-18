#!/usr/bin/python

import sys


oldKey = None

# Loop around the data
# It will be in the format key\tval



def joinData(bNodes,userInfo ):
    if len(bNodes) == 0 or len(userInfo) ==0:
        return

    for b in bNodes:
        j = "\t".join(b + userInfo)
        
        print j

    


oldKey = None
BNodes = []
currentUser = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    
    thisKey = data_mapped[0] #author_id

    if data_mapped[1] == "B": #B type rows are user post data
        BNodes.append(data_mapped)


    elif data_mapped[1] == "A": #A type rows are user information
        currentUser = data_mapped


# if we have both user data and post data, we'll join them 
    if oldKey and oldKey != thisKey:
        if BNodes and currentUser:
            joinData(BNodes,currentUser[1:])


        oldKey = thisKey;
        BNodes = []
        currentUser = None

    
    oldKey = thisKey
    

# this capture the last author_id
if oldKey != None:
    if BNodes and currentUser:
        joinData(BNodes,currentUser[1:])    



