import requests
import urllib.request
from bs4 import BeautifulSoup

def get_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    release_year = soup.find("span", id="titleYear").text.strip('()')

    credit = soup.find("div", class_="credit_summary_item").text.strip()
    credit_list = credit.splitlines()
    director = credit_list[1].strip('|')

    summary = soup.find("div", class_="summary_text").contents[0].strip()

    return release_year, director, summary

