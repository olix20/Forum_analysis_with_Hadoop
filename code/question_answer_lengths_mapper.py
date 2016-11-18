#!/usr/bin/python


'''
We are interested to see if there is a correlation between the length of a post and the length of answers.

Here we have a mapreduce program that would process the forum_node data and output the length of the post and the average answer (just answer, not comment) length for each post.

'''


import sys
import re
import csv
from datetime import datetime





reader = csv.reader(sys.stdin, delimiter='\t')
#writer = csv.writer(sys.stdout) #, delimiter='\t', quotechar='"',quoting=csv.QUOTE_ALL)


for line in reader:

    

    if len(line) == 19: 

#read data from forum node tsv (user posts)
#"id"	"title"	"tagnames"	"author_id"	"body"	"node_type"	"parent_id"	"abs_parent_id"	"added_at"	"score"

        if line[0] == "id": #skip header
            continue 

        nodeID = line[0]#int(line[0].strip('"'))
        title = line[1]
        tagNames = line[2]
        author_id = line[3]
        body = line[4]
        node_type = line[5]
        parent_id = line[6]
        abs_parent_id = line[7]
        added_at = line[8]
        score = line[9]


        if node_type not in ["question","answer"]:
            continue

        # assign self as parent, if it's a question, so that it's going to be put together with questions after sorting

        if parent_id=="\N":
            parent_id = nodeID    
        

        
        row = "\t".join([parent_id,node_type,str(len(body))])
        #writer.writerow(row)
        print row

 

