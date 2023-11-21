import networkx as nx
import matplotlib.pyplot as plt

def main():
    def filter_node(node):
        if (rank[node] >= float(lower)) and (rank[node] <= float(upper)):
            return True
        else: 
            return False
    
    # Read graph
    G = nx.read_gml('graph.gml')
    # Rank nodes
    rank = nx.pagerank(G)

    # Ask user for lower and upper bound, global variables are used to be used in filter_node function
    global lower
    lower = input("Enter the lower bound: ")
    global upper
    upper = input("Enter the upper bound: ")

    # Ask user if they wish to display label
    label = (input("Do you wish to display label? (y/n): ")).upper()

    # Filter nodes based on user input
    subgraph = nx.subgraph_view(G, filter_node)

    # Get list of ranks values of the subgraph
    subgraph_rank = nx.pagerank(subgraph)
    ranks = list(subgraph_rank.values())
    rank_max = max(ranks)
    rank_min = 0

    # Normalize list of ranks values
    nodes_size = list(((value-rank_min)/(rank_max-rank_min)) * 1000 for value in ranks)
    nodes_color = list(((value-rank_min)/(rank_max-rank_min)) * 100 for value in ranks)
    # Display graph
    pos = nx.spring_layout(G) 
    nx.draw(subgraph, pos, node_size = nodes_size, node_color = nodes_color, cmap=plt.cm.YlOrRd, vmin = 0, vmax = 27)
    # Display label is optional because graph can look messy
    if label == 'Y':
        nx.draw_networkx_labels(subgraph, pos, font_size = 8, font_color= "black" )
    plt.show()

if __name__ == '__main__':
    main()
    