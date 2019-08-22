import requests
from lxml import html
import random


def random_link_trail():
    response = requests.get('https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wMnZ4bhIiUExuUzZNOHZRRmtkTDdVak92NnpXcDRzNl9KTDgxWDZSbA%3D%3D')
    parser_tree = html.fromstring(response.content)
    content = parser_tree.xpath('//*[contains(@class, "yt-lockup-thumbnail")]/a[@href]')
    links = [el.get('href') for el in content]
    return random.choice((links))


def random_link_fun():
    response = requests.get('https://www.youtube.com/results?search_query=%D1%81%D0%BC%D0%B5%D1%88%D0%BD%D0%BE%D0%B5&sp=CAISBAgBEAE%253D')
    parser_tree = html.fromstring(response.content)
    content = parser_tree.xpath('//*[contains(@class, "yt-lockup-thumbnail")]/a[@href]')
    links = [el.get('href') for el in content]
    return random.choice((links))


def random_link_musik():
    response = requests.get('https://www.youtube.com/feed/trending?bp=4gIuCggvbS8wNHJsZhIiUExGZ3F1TG5MNTlha0dhb1otcEZsR0FrOUl6aV9zLXloXw%3D%3D')
    parser_tree = html.fromstring(response.content)
    content = parser_tree.xpath('//*[contains(@class, "yt-lockup-thumbnail")]/a[@href]')
    links = [el.get('href') for el in content]
    return random.choice((links))



def random_link_fackts():
    response = requests.get('https://www.youtube.com/results?search_query=%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%B5%D1%81%D0%BD%D1%8B%D0%B5+%D1%84%D0%B0%D0%BA%D1%82%D1%8B+joy-pup&sp=EgIQAQ%253D%253D')
    parser_tree = html.fromstring(response.content)
    content = parser_tree.xpath('//*[contains(@class, "yt-lockup-thumbnail")]/a[@href]')
    links = [el.get('href') for el in content]
    return random.choice((links))


