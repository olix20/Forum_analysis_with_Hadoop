## Analyzing Forum Usage using Hadoop MapReduce


In this project I experiment with some discussion forum data. It is a type of user generated content that you can find all around the web. Most popular websites have some kind of a forum, and the things I do here can be  transferred to other similar projects. 


### The Data Set

This particular dataset was taken from the Udacity forums which run on a free, opensource software called OSQA, and was designed to be similar to the popular StackOverflow forums. The basic structure is - the forum has nodes. All nodes have a body and author_id. Top level nodes are called questions, and will also have a title and tags. Questions can have answers. Both questions and answers can have comments.

I run the code here only on a cloudera VM, but it can also be run on a real Hadoop cluster. You can download the dataset from data folder. To unarchive it, download it to your VM run:

tar zxvf forum_data.tar.gz

There are 2 files in the dataset. The first is "forum_nodes.tsv", and that contains all forum questions and answers in one table. It was exported from the RDBMS by using tab as a separator, and enclosing all fields in doublequotes. You can find the field names in the first line of the file "forum_node.tsv". The ones that are the most relevant to the task are:

    "id": id of the node
    "title": title of the node. in case "node_type" is "answer" or "comment", this field will be empty
    "tagnames": space separated list of tags
    "author_id": id of the author
    "body": content of the post
    "node_type": type of the node, either "question", "answer" or "comment"
    "parent_id": node under which the post is located, will be empty for "questions"
    "abs_parent_id": top node where the post is located
    "added_at": date added

The second table is "forum_users.tsv". It contains fields for "user_ptr_id" - the id of the user. "reputation" - the reputation, or karma of the user, earned when other users upvote their posts, and the number of "gold", "silver" and "bronze" badges earned. 



To make sure the code is running properly, we also have a smaller data set and set of expected outputs to check your work. It's under data folder "student_test_posts.csv". More info in [here](https://www.udacity.com/wiki/ud617/local-testing-instructions)


Instructions on setting up the VM are (here)[https://www.udacity.com/wiki/ud617#!#setting-up-the-vm-datasets]
If you're new to Hadoop you can get a headstart from (here)[https://www.udacity.com/wiki/ud617]

### Shell Commands

Upload data into Hadoop fs: 
    hadoop fs -mkdir forum_data
    hadoop fs -put data/forum_users.tsv forum_data
    hadoop fs -put data/forum_node.tsv forum_data

Check hadoop fs: 
    hadoop fs -ls forum_data
    hadoop fs -tail forum_data/forum_users.tsv 



Running the program:
    hs code/popular_times_mapper.py code/popular_times_reducer.py forum_data popular_times_output



Check output
    hadoop fs -get popular_times_output/part-00000
    gedit part-00000




