import requests
from bs4 import BeautifulSoup
from browser import get_page_content
from write_results import write_results
from urls import top100

# for ad-hoc testing
test_url = "https://microsoft.com"

# list of attributes that use idrefs for accessibility-related relationships
attributes = ["for", "aria-activedescendant", "aria-controls", "aria-describedby", "aria-details", "aria-errormessage", "aria-labelledby", "aria-owns", "interestfor", "commandfor"]

# get all elements with an id-referencing attribute
def element_query(tag):
    for attribute in attributes:
        if tag.has_attr(attribute):
            return True
    return False

# function to verify whether an id or list of ids exist in the document
def check_id(id_string, soup):
    # check for multiple ids
    ids = id_string.split()
    for id in ids:
        if len(id.strip()) > 0 and soup.find(id=id) is None:
            return False
    return True

def test_page(url):
    attribute_count = 0
    invalid_count = 0
    id_count = 0
    ids = []
    duplicate_ids = []
    duplicate_id_used = 0

    try:
        page = get_page_content(url)
    except:
        print(f'Error fetching {url}')
        return

    soup = BeautifulSoup(page, "html.parser")

    els_with_ids = soup.find_all(id=True)
    for el in els_with_ids:
        id_count += 1
        id = el['id']
        if id in ids:
            duplicate_ids.append(id)
        else:
            ids.append(id)

    # Find all elements with an href
    matches = soup.find_all(element_query)
    for element in matches:
        for attribute in attributes:
            if attribute in element.attrs:
                attribute_count += 1
                if not check_id(element[attribute], soup):
                    print(f'Invalid idref {element[attribute]} in attribute {attribute} on element {element}')
                    invalid_count += 1
                if element[attribute] in duplicate_ids:
                    duplicate_id_used += 1

    print(f'Testing {attribute_count} attributes and {id_count} ids, {invalid_count} invalid, {len(duplicate_ids)} duplicate ids, {duplicate_id_used} duplicate ids used')
    return ([attribute_count, id_count, invalid_count, len(duplicate_ids), duplicate_id_used])

def test_all_urls(urls):
    data_columns = ['url', 'attribute count', 'id count', 'invalid idref count', 'duplicate id count', 'duplicate ids used']
    data_rows = []
    for url in urls:
        print(f'Testing {url}')
        result = test_page(url)
        if result:
            data_rows.append([url] + result)

    write_results(data_columns, data_rows)

# test_page(test_url)
test_all_urls(top100)