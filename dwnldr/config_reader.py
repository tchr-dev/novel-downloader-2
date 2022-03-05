import json
import os
import re
import sys


def get_config(url) -> dict:
    """
    """
    # basic setup
    BASE_PATH = os.path.dirname(os.path.realpath(__file__))

    with open(BASE_PATH+"/config.json") as json_data_file:
        data = json.load(json_data_file)

    # retriev all supported keys

    default = data["defaults"]
    base_url_regex = data["base_url_regex"]
    if re.match(base_url_regex, url):
        found_url = re.match(base_url_regex, url).group(0)
    else:
        sys.exit("URL not recognized!")

    key = ""
    for k in default:
        if default[k]["url"] == found_url:
            key = default[k]["key"]
            return data[key]
        else:
            sys.exit(f"Key {key} not found!")


