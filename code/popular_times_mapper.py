#!/usr/bin/python


'''
Our students come from all around the world, so we need to know both at what times of day the activity is the highest, and to know which of the students are active at that time.

through 'popular_times' mapper/reducer we'll find for each student what is the hour during which the student has posted the most posts. Output from reducers should be:


For example:

13431511\t13
54525254141\t21

If there is a tie: there are multiple hours during which a student has posted a maximum number of posts, we print the student-hour pairs on separate lines. 

Here we  ignore the time-zone offset for all times - for example in the following line: "2012-02-25 08:11:01.623548+00" - you can ignore the +00 offset.

We use the date_added field and NOT the last_activity_at field.

'''


import sys
import re
import csv
from datetime import datetime

inCompleteRowCount  = 0 
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
        # 2012-04-29 14:45:19.216809+00
        
        row = "\t".join([author_id,str(datetime.strptime(added_at[0:13], '%Y-%m-%d %H').hour)])
        #writer.writerow(row)
        print row

 

