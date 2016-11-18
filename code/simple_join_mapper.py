#!/usr/bin/python

import sys
import re
import csv

firstRow = True
inCompleteRowCount  = 0 
counter = 0



reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"',quoting=csv.QUOTE_ALL)


for line in reader:

    

    if len(line) == 19: 

#read data from forum node tsv (user posts)
#"id"	"title"	"tagnames"	"author_id"	"body"	"node_type"	"parent_id"	"abs_parent_id"	"added_at"	"score"

        if line[0] == "id":
            continue 

        nodeID = line[0]#int(line[0].strip('"'))
        title = line[1]
        tagNames = line[2]
        author_id = line[3]
        node_type = line[5]
        parent_id = line[6]
        abs_parent_id = line[7]
        added_at = line[8]
        score = line[9]
        
        row = "\t".join([author_id,"B",nodeID,title,tagNames,node_type,parent_id,abs_parent_id,added_at,score])
        #writer.writerow(row)
        print row

 
    elif len(line) == 5: 

#read data from forum_users tsv
#"user_ptr_id"	"reputation"	"gold"	"silver"	"bronze"

        if line[0] == "user_ptr_id":
            continue 


        author_id = line[0]        
        reputation  = line[1]
        gold = line[2]
        silver = line[3]
        bronze = line[4] 

        row = "\t".join([author_id,"A",reputation, gold, silver, bronze])
        #writer.writerow(row)
        print row



#print "inCompleteRowCount:",inCompleteRowCount

