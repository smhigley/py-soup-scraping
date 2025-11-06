# A web scraper to check for broken id associations

This is related to the open w3c issue about using relative element references as a DX improvement. The goal of this scraper is to check whether the current `id`-based reference approach results in user-facing problems.

## Websites

I took the top 100 most-visited websites from https://backlinko.com/most-popular-websites, checked against the [wikipedia page with fewer results](https://en.wikipedia.org/wiki/List_of_most-visited_websites). I excluded sites that display almost nothing without a login (e.g. facebook), and porn-related sites, since this is running on my work machine.

## How to run the scripts

This is a python-based web scraper, and assumes python3 and pip are installed.

```bash
# create the virtual environment
python -m venv venv

# activate the virtual environment
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# Optional: re-run the scraper to update data
python src/scraper.py

# Print info about the scraped data
python src/process.py

# deactivate the virtual environment when done
deactivate
```