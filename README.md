# Information-Network-and-the-WWW

Package requires:
pip install requests beautifulsoup4 lxml 

Instructions:
crawler.py:
    - Make sure the initial pages file is in the same directory as the crawler.py file.
    - Run the crawler.py, it will ask for the name of the file containing the initial pages and the number of pages to crawl.
    - The crawler will crawl the web and display a loglog in-degree a graph of the crawled webpages.
    - The graph will be saved in a file called graph.txt

pagerank.py:
    - Make sure to run the crawler.py first to generate the graph.gml file. If you wish to use a different graph, make sure it's also name graph.gml and is in gml format.
    - Run the pagerank.py file, it will ask for a interval to generate the subgraph with page rank value within that interval.
    - Program will ask if user would like to display node name.
    - Program will generate and display the subgraph. 
