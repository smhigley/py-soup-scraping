import requests
from bs4 import BeautifulSoup
from browser import get_page_content

URL = "https://cfapi.centminmod.com/"

# list of attributes that use idrefs for accessibility-related relationships
attributes = ["for", "aria-activedescendant", "aria-controls", "aria-describedby", "aria-details", "aria-errormessage", "aria-labelledby", "aria-owns"]

# get all elements with an id-referencing attribute
def element_query(tag):
    for attribute in attributes:
        if tag.has_attr(attribute):
            return True
    return False

# function to verify whether an id or list of ids exist in the document
def check_id(id_string):
    # check for multiple ids
    ids = id_string.split()
    for id in ids:
        if len(id.strip()) > 0 and soup.find(id=id) is None:
            return False
    return True

attribute_count = 0
invalid_count = 0
id_count = 0
ids = []
duplicate_ids = []
duplicate_id_used = 0

page = get_page_content(URL)
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
            print(f'{attribute} is valid: {check_id(element[attribute])}')
            if not check_id(element[attribute]):
                invalid_count += 1
            if element[attribute] in duplicate_ids:
                duplicate_id_used += 1
                print(f'  {element[attribute]} uses a duplicate id')

print(f'Found {attribute_count} attributes, {invalid_count} invalid, {len(duplicate_ids)} duplicate ids, {id_count} total ids, {duplicate_id_used} duplicate ids used')