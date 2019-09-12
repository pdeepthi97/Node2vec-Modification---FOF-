import networkx as nx
import pandas as pd
from FriendofFriend import FriendOfFriend
from collections import defaultdict
from EvalUtils import EvalUtils


def test(dataset, testset):
    g = nx.read_weighted_edgelist(dataset, create_using=nx.DiGraph())
    gtest= nx.read_weighted_edgelist(testset, create_using=nx.DiGraph())
    df1 = pd.read_csv(dataset, names = ['v1','v2','timestamp'],sep = '\t',lineterminator='\n',header = None, dtype=str)
    df2 = pd.read_csv(testset, names = ['v1','v2','timestamp'],sep = '\t',lineterminator='\n',header = None, dtype=str)
    fof = FriendOfFriend(filename=dataset, is_temporal=True, walk_length=8)  # Use temp_folder for big graphs

    model = fof.fit(window=10, min_count=1, batch_words=4)  # Any keywords acceptable by gensim.Word2Vec can be passed, `diemnsions` and `workers` are automatically passed (from the FriendOfFriend constructor)

    all_connections = defaultdict(list)
    for index, row in df1.iterrows():
        all_connections[row["v1"]].append((row["v2"]))

    predicted = defaultdict(list)
    count = 0
    actual_links = set(gtest.edges)
    preds = 0
    actual_list = []
    pred_list = []
    for key in all_connections.keys():
        if g.out_degree(key) != 1:
            continue

        try:
            listobj = model.wv.most_similar(key)[:10]
            nodes = [elem[0] for elem in listobj]
            pred_edges = [(key, node) for node in nodes]
            pred_set = set(pred_edges)

            preds += len(actual_links.intersection(pred_set))
            pred_list.append(pred_edges)
            actual_list.append(actual_links)

        except KeyError:
            continue



    print(EvalUtils.mapk(actual_list,pred_list,k=10))
    print(preds)



test("../datasets/redditdataset_75.txt", "../datasets/redditdataset_test.txt")