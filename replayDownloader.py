import os, json, sys, requests

import requests

# open config file for download location

with open("config.json", "r") as f:
    config = json.load(f)

def getReplays(replayID):
    print("Getting replay...")

    # Check directory exists
    newDir = os.getcwd() + (config['download_path'])
    if not os.path.exists(newDir):
        os.makedirs(newDir)

    # Assign file directory
    directory = os.path.join(newDir)
    filename = directory + replayID + ".osr"

    # Download replay
    try:
        # Download URL + Location
        url = config['download_endpoint']
        dlpath = str(filename)

        # Download
        r = requests.get(url + replayID)
        with open(dlpath, "wb") as stream:
            stream.write(r.content)
        print("Downloading replay...")
    except Exception as e:
        print("Could not download", e)
        sys.exit(1)
    print("Download Complete")
    return

# Main file

replayID = input("Which replay would you like to download? ID: ")
getReplays(replayID)