#!/usr/bin/python


'''
We might want to help students form study groups. But first we want to see if there are already students on forums that communicate a lot between themselves.

As the first step for this analysis let's write a mapreduce program that for each forum thread (that is a question node with all it's answers and comments) would give us a list of students that have posted there - either asked the question, answered a question or added a comment. If a student posted to that thread several times, they should be added to that list several times as well, to indicate intensity of communication.

'''


import sys
import re
import csv

counter = 0



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
        node_type = line[5]
        parent_id = line[6]
        abs_parent_id = line[7]
        added_at = line[8]
        score = line[9]
 

        # if this node is a question assign self as parent, 
        # so that it's going to be put together with answers after sorting

        if parent_id=="\N":
            parent_id = nodeID    

        row = "\t".join([parent_id,author_id])


        print row

 

