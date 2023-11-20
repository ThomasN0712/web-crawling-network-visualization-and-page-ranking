import pickle
import networkx as nx

def main():
    G = pickle.load(open('graph.pickle', 'rb'))
    rank = nx.pagerank(G)
    highest_rank = max(rank, key=rank.get)
    print("The highest rank is: ", highest_rank, "with the score of", rank[highest_rank])
    
if __name__ == '__main__':
    main()
    