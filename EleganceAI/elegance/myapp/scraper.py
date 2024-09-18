import requests
from bs4 import BeautifulSoup

def scrape_webpage(url):
    """
    Function to scrape the webpage and extract text from paragraphs.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract text from all paragraphs
        raw_text = ""
        for paragraph in soup.find_all('p'):
            raw_text += paragraph.get_text()

        return raw_text

    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return ""
