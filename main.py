from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import requests
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

def crawling(G, url, number_of_nodes):
    """
    Add nodes and edges to the graph.
    G : Graph
    url : URL of the website to scrape
    number_of_nodes : Number of nodes to add to the graph
    """
    # Send an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all anchor tags (links) in the HTML
        links = soup.find_all('a')

        i = 0
        min_num = min(number_of_nodes, len(links))

        # Extract and print the href attribute from links with the same domain
        #for j in range(0, len(links)):
        for j in range(0, 10):
            if i == min_num:
                break
            link = links[j]
            href = link.get('href')
            absolute_url = urljoin(url, href)  # Build absolute URL
            if is_same_domain(absolute_url, url) and is_different_path(absolute_url, url): # Check if URL is in the same domain
                # print(absolute_url) ## Delete later
                G.add_node(absolute_url)
                G.add_edge(url, absolute_url) # Add edge to the graph
                i += 1
        return i
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)
        

def main():
    number_of_nodes = 10000

    # TODO: Add links from a separate file
    root_links = ['https://dblp.org/', 'https://dblp.org/pid/e/PErdos.html', 'https://dblp.org/pid/s/PaulGSpirakis.html', 'https://dblp.org/pid/s/PaulGSpirakis.html']

    # Initilize the graph
    G = nx.DiGraph()

    i = 0
    # Initialize the crawling
    for link in root_links:
        i += crawling(G, link, number_of_nodes)
    print(i)

    # Draw the graph
    nx.draw(G)
    plt.show()

if __name__ == '__main__':
    main()
