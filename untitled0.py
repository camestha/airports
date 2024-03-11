"""

This is a temporary script file.
"""
import pandas as pd
import requests
import mechanicalsoup
from bs4 import BeautifulSoup


# URL of the page to crawl
url = "https://www.ogimet.com/metars.phtml.en"

response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'lxml')

