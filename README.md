See the requirements given in the requirements.txt file.

To test the link prediction task on the cold start nodes using a test set of the last 25% of links formed in the graph, run:

python3 test_cold_start.py 


To run it on the larger reddit dataset, in test.py, change the dataset path and the training set path to:
"../datasets/redditdataset_75.txt", "../datasets/redditdataset_test.txt"

in the run function call.

The output of the function gives two lines; the number of links successfully predicted, 
and the Mean Average Precision @ 10 for the ranking of links returned for each node

To test the link prediction task on all nodes using a range of train-test splits, run:

python3 test_all_nodes.py

The output will be the precision, recall and f1 score for each train-test split, and finally the average f-1 score value


