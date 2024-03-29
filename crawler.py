from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import requests
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def is_same_domain(url, base_url):
    """
    Check if the given URL has the same domain as the base URL.
    """
    return urlparse(url).netloc == urlparse(base_url).netloc

def is_different_path(url, base_url):
    """
    Check if the given URL has a different path than the base URL.
    """
    return urlparse(url).path != urlparse(base_url).path

def crawling_back(G, url, root_links):
    '''
    Search backward to exist node and create edge if exist path
    G : Graph
    url : current url to check
    root_links : List of existed links
    '''

    print("Crawling back: ", url)
    
    # Send an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all anchor tags (links) in the HTML
        links = soup.find_all('a')

        # Extract and print the href attribute from links with the same domain
        for j in range(0, len(links)):
            link = links[j]
            href = link.get('href')
            absolute_url = urljoin(url, href)  # Build absolute URL

            # Check if URL is in the same domain and has a different path
            if absolute_url in root_links and url != absolute_url: 
                G.add_edge(url, absolute_url) # Add edge to the graph

def crawling(G, url, current_number_of_nodes, root_links, min_number_of_nodes):
    """
    Add nodes and edges to the graph.
    G : Graph
    current_number_of_nodes : Current number of nodes in the graph
    root_links : List of links
    """
    
    print("Crawling: ", url)

    # Send an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all anchor tags (links) in the HTML
        links = soup.find_all('a')

        # Extract and print the href attribute from links with the same domain
        for j in range(0, len(links)):
            link = links[j]
            href = link.get('href')
            absolute_url = urljoin(url, href)  # Build absolute URL

            # Check if URL is in the same domain and has a different path
            if is_same_domain(absolute_url, url) and is_different_path(absolute_url, url): 
                if absolute_url not in root_links:
                    root_links.append(absolute_url) # Add link to the list of root links for further crawling
                G.add_node(absolute_url) # Add node to the graph
                G.add_edge(url, absolute_url) # Add edge to the graph

                #Check if the new node have a connection to an existence node
                crawling_back(G, absolute_url, root_links)
                if current_number_of_nodes >= min_number_of_nodes:
                    print(current_number_of_nodes)
                    break
                print("Number of nodes: ", current_number_of_nodes)
                current_number_of_nodes += 1
        return current_number_of_nodes
    else:
        print('Cannot retrieve page information. Status code:', response.status_code)

def graph_analysis(G):
    # Calculate the degree of each node
    xlog = list(np.log(x) for x in range(1, len(G.degree()) + 1))
    ylog = sorted((np.log(d) for n, d in G.degree()), reverse=True)
    
    fig = plt.figure("Degree of graph")
    # Plot the degree distribution
    plt.scatter(xlog, ylog)
    plt.title("Degree of graph")
    plt.ylabel("Number of pages")
    plt.xlabel("in-degree")
    plt.show()
        
def main():
    #max nodes for each root link
    file_name = input("Enter the initial pages file name: ")
    min_number_of_nodes = int(input("Enter the minimum number of nodes: "))

    # Add links from a file
    with open(file_name, 'r') as f:
        root_links = f.read().splitlines()
        root_links.pop(0) 
        root_links.pop(len(root_links) - 1) 
    
    # Initilize the graph
    G = nx.DiGraph()

    # Initilize the node counter
    current_number_of_nodes = 1

    # Initialize the crawling
    for link in root_links:
        current_number_of_nodes = crawling(G, link, current_number_of_nodes, root_links, min_number_of_nodes)
        if current_number_of_nodes >= min_number_of_nodes:
            print(current_number_of_nodes)
            break
    
    # Draw the graph 
    # pos = nx.spring_layout(G) 
    # nx.draw(G, pos)
    # plt.show()

    # Plot the graph into a loglog plot of the in-degree distribution using matplotlib
    graph_analysis(G)

    # Save the graph
    nx.write_gml(G, 'graph.gml')

if __name__ == '__main__':
    main()
