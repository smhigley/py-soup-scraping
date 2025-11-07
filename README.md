# A web scraper to check for broken id associations

This is related to the open w3c issue about using relative element references as a DX improvement. The goal of this scraper is to check whether the current `id`-based reference approach results in user-facing problems.

## Websites

I took the top 100 most-visited websites from https://backlinko.com/most-popular-websites, checked against the [wikipedia page with fewer results](https://en.wikipedia.org/wiki/List_of_most-visited_websites). I excluded sites that display almost nothing without a login (e.g. facebook), and porn-related sites, since this is running on my work machine.

## Findings

So far, the conclusion that duplicate `id` attribute values are a widespread problem has been based on the total number of dupicate `id`s existing on the page. However, based on this data, the number of duplicate `id`s used is far smaller.

In the top 100 sites scraped, there were a total of `2705` id-referencing attributes present. Of those:
- 62 sites had duplicate `id`s present, for a total of 1210 total duplicated `id`s across all sites
- 12 sites had id-referencing attributes that pointed to a non-unique `id`, for a total of 160 duplicated `id`s that were referenced across all sites

The number of non-unique `id`s used was actually quite a small fraction of the total number of `id`s used. Specifically, only 6% of id-referencing attributes pointed at a duplicated `id`. Additionally, not all of those are necessarily invalid -- the method of scraping does not account for elements that are hidden with CSS or HTML.

It seems that invalid id refs (i.e. an id-referencing attribute pointing at an id that does not exist) are far more common. This occurred in 41 of the 100 sites, and a total of 249 attributes pointing at invalid `id`s (or 9% of the total attributes).

These also do not necessarily correspond to a real-world bug -- it is possible, for example, to reference an error message element's `id` in `aria-describedby`, counting on the fact that it will only be read if the error message actually exists in the DOM.

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