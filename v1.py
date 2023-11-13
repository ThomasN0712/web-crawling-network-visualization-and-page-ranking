from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import requests
import networkx as nx
import matplotlib.pyplot as plt
#for timing code, delete later
import time

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

def crawling(G, url, current_number_of_nodes, max_number_of_nodes, start_time, root_links):
    """
    Add nodes and edges to the graph.
    G : Graph
    url : URL of the website to scrape
    number_of_nodes : Number of nodes to add to the graph
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

        print(len(links))
        # # TIME 
        # elapsed_time_section1 = time.time() - start_time
        # print(f"This {url} section took {elapsed_time_section1} seconds")
        # # END TIME

        # Extract and print the href attribute from links with the same domain
        for j in range(0, len(links)):
            if current_number_of_nodes >= max_number_of_nodes:
                break
            if j > 50:
                break
            link = links[j]
            href = link.get('href')
            absolute_url = urljoin(url, href)  # Build absolute URL
            if is_same_domain(absolute_url, url) and is_different_path(absolute_url, url): # Check if URL is in the same domain
                root_links.append(absolute_url)
                G.add_node(absolute_url)
                G.add_edge(url, absolute_url) # Add edge to the graph
                current_number_of_nodes += 1
        return current_number_of_nodes
    else:
        print('Failed to retrieve the webpage. Status code:', response.status_code)
        

def main():
    start_time = time.time()
    #max nodes for each root link
    max_number_of_nodes = 100

    # TODO: Add links from a separate file
    root_links = ['https://dblp.org/', 'https://dblp.org/pid/e/PErdos.html', 'https://dblp.org/pid/s/PaulGSpirakis.html', 'https://dblp.org/pid/89/8192.html']
    
    # Initilize the graph
    G = nx.DiGraph()

    current_number_of_nodes = 0
    # Initialize the crawling
    for link in root_links:
        current_number_of_nodes = crawling(G, link, current_number_of_nodes, max_number_of_nodes, start_time, root_links)
        print(len(root_links))
        if current_number_of_nodes >= max_number_of_nodes:
            break
    print(current_number_of_nodes)

    # Draw the graph
    pos = nx.spring_layout(G) 
    nx.draw(G, pos)
    plt.show()

    #TIME
    elapsed_time_section1 = time.time() - start_time
    print(f"Draw graph took {elapsed_time_section1} seconds")
    #END TIME

if __name__ == '__main__':
    main()
