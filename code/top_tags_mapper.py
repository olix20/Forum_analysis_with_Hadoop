#!/usr/bin/python


'''
We are interested to see what are the top tags used in posts.

Here we have a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in.


In a general case,  2 map reduce programes are required: the first one extracts and creates an index of tags. The second sorts and selects top(n) tags. But here on Cloudera we have only one reducer which makes it possible to achieve this with only one map-reduce. 

'''


import sys
import re
import csv





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
    

        if node_type not in ["question"]:
            continue
        
        for tag in tagNames.split():
            print "\t".join([tag,str(nodeID)])


        #writer.writerow(row)


 

