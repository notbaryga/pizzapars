import requests
from bs4 import BeautifulSoup as bs


def get_category_blocks(ramen) -> list:
    category_blocks = []
    try:
        for el in ramen.findAll(class_="category"):
            category_blocks.append(el)
    except:
        ...
    return category_blocks


def get_category_names(category_blocks: list) -> list:
    category_names = []
    try:
        for block in category_blocks:
            for el in block.findAll(class_="category-name"):
                category_names.append(el.text.strip())
    except:
        ...
    return category_names


def main(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/110.0.0.0 Safari/537.36 '
    }
    page = requests.get(url, headers=headers)
    ramen = bs(page.text, "html.parser")
    category_blocks = get_category_blocks(ramen)
    category_names = get_category_names(category_blocks)
    for el in category_names:
        print(el)



if __name__ == '__main__':
    main('https://pizzamia.smartomato.ru/')
