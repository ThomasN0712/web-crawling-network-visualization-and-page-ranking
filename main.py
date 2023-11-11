from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import requests

def is_same_domain(url, base_url):
    """
    Check if the given URL has the same domain as the base URL.
    """
    return urlparse(url).netloc == urlparse(base_url).netloc

# Replace 'url' with the URL of the website you want to scrape
url = 'https://dblp.org/pid/e/PErdos.html'

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all anchor tags (links) in the HTML
    links = soup.find_all('a')

    # Extract and print the href attribute from links with the same domain
    for link in links:
        href = link.get('href')
        absolute_url = urljoin(url, href)  # Build absolute URL
        if is_same_domain(absolute_url, url):
            print(absolute_url)
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
