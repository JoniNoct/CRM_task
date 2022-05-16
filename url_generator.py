import json
import re

import requests
from bs4 import BeautifulSoup

import helper

# request-response part
response = requests.get(helper.domain_url)
soup = BeautifulSoup(response.content, 'html.parser')

# parsing locations domain
loc_in_script = soup.find("script", text=re.compile("mydropdowns")).string
loc_raw_json = re.search(r'data:([^\]]+\])', loc_in_script).group(1)
loc_json = json.loads(loc_raw_json)
locations = helper.get_loc_from_json(loc_json)
raw_json = helper.urls_generator(locations)

with open("urls.json", "w") as outfile:
    outfile.write(json.dumps(raw_json))
