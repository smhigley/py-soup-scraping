import requests
from bs4 import BeautifulSoup
from browser import get_page_content

URL = "https://new.kasumata.ee/"
# page = requests.get(URL)
# print(page.content)
# soup = BeautifulSoup(page.content, "html.parser")

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

def check_duplicate_ids(new_id):
    if new_id in ids:
        duplicate_id_count += 1
    else:
        ids.append(new_id)

attribute_count = 0
invalid_count = 0
duplicate_id_count = 0
ids = []

page = get_page_content(URL)
soup = BeautifulSoup(page, "html.parser")

# Find all elements with an href
matches = soup.find_all(element_query)
for element in matches:
    if element.has_attr("id"):
        check_duplicate_ids(element["id"])
    for attribute in attributes:
        if attribute in element.attrs:
            attribute_count += 1
            print(f'{attribute} is valid: {check_id(element[attribute])}')
            if not check_id(element[attribute]):
                invalid_count += 1

print(f'Found {attribute_count} attributes, {invalid_count} invalid, {duplicate_id_count} duplicate ids')