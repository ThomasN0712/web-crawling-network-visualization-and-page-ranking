from bs4 import BeautifulSoup
import requests

# Replace 'url' with the URL of the website you want to scrape
url = "https://en.wikipedia.org/wiki/Wiki"

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all anchor tags (links) in the HTML
    links = soup.find_all('a')

    # Extract and print the href attribute from each link
    for link in links:
        href = link.get('href')
        print(href)
else:
    print('Failed to retrieve the webpage. Status code:', response.status_code)
