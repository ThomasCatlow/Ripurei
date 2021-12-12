import os
import requests
import json
import sys
import shutil

# open config file for download location
configFileCheck = os.path.join(os.getcwd(), "config.json")
if not os.path.exists(configFileCheck):
    shutil.copy2("./config-sample.json", "./config.json")

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

print("""
Welcome! Thank you for choosing Ripurei!

Please submit a Replay ID below to start the replay download.
""")
replayID = input("Selected Replay ID: ")
getReplays(replayID)
