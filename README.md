# Information-Network-and-the-WWW

Package requires:
pip install requests beautifulsoup4 lxml 

Instructions:

crawler.py:
    - Make sure the initial pages file is in the same directory as the crawler.py file.
    - Run the crawler.py, it will ask for the name of the file containing the initial pages and the number of pages to crawl.
    - The crawler can crawl forward and backward at a rate of 1s per page.
    - The crawler will crawl the web and display a loglog in-degree a graph of the crawled webpages.
    - The graph will be saved in a file called graph.txt

pagerank.py:
    - Make sure to run the crawler.py first to generate the graph.gml file. If you wish to use a different graph, make sure it's also name graph.gml and is in gml format.
    - Run the pagerank.py file, it will ask for a interval to generate the subgraph with page rank value within that interval.
    - Program will ask if user would like to display node name.
    - Program will generate and display the subgraph. 

provide graph.gml file has 1000 nodes. 

Report:
	This is a fun program assignment that introduce me to web crawling. It is a decently challenging assignment because I need to learn how to use Beaufulti soup library to make request of the web page, and learn the HTML format to extract the needed links. 
	When I first start out, I made a mistake of not finishing crawling back to all existence nodes and form all neccessary edges. But after the I realized my mistake, it is a easy fix. The problem I now have is that the crawling take a very long time due, for 100 nodes it would take about 2 minutes. So waiting to crawl all 5000 nodes would take at least 2 hours. I'm aware that if you use Scrappy, the run time might be slightly faster, but it's more difficult to work with so I prefer to use Beautifulsoup for this project. The page rank was trivial due to the built in function from networkx library.
