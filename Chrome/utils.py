import json

def get_data():
    with open("config.json","r") as f:
        stuff = json.load(f)
    return stuff
