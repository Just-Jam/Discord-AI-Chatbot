import openai
import os
from dotenv import load_dotenv # python-dotenv
import re
import requests


def fetch_mtg_card(card_name):
    res = requests.get(SCRYFALL_API + card_name)
    if res.status_code == 200:
        data = res.json()
        print(data)
        card_info = {
            "name": data.name,
            "mana_cost": data.mana_cost,
            "type_line": data.type_line,
            "oracle_text": data.oracle_text
        }
        return card_info
    else:
        return f"Error fetching {card_name}"
def contains_mtg_card(input_string):
    pattern = re.compile(r'\[\[([^\]]*)\]\]')
    matches = pattern.findall(input_string)

    if matches:
        return matches
    else:
        return None

# Example usage
input_string = "This is a string containing."
card_list = contains_mtg_card(input_string)
print(contains_mtg_card(input_string))
#
# SCRYFALL_API = "https://api.scryfall.com/cards/named?fuzzy="
# res = requests.get(SCRYFALL_API + "8s7ad67asft8236edyuad")
# if res.status_code == 200:
#     data = res.json()
#     print(data)
# else:
#     print("Error fetching card")
#get data.name, data.mana_cost, type_line, oracle_text