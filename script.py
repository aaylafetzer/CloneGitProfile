import os
import sys
import requests
import threading
import platform

GIT = None
PATH = None
PLATFORM = platform.system()


def clone(git, repo):  # Run git clone command
    os.system(f"git clone https://github.com/{git}/{repo}.git \"{PATH}/{repo}\"")


# Detect what platform the script is running on
if PLATFORM == "Linux" or PLATFORM == "Darwin":  # The script is running on Linux or MacOS
    PATH = "~/Documents/Code/"
elif PLATFORM == "Windows":  # The script is running on garbage
    PATH = "%USERPROFILE%\\Documents\\Code"
else:  # The script can't identify the host OS
    input("Unable to identify operating system")
    exit()

if len(sys.argv) == 1:  # Test if a profile name is given in the system arguments
    GIT = input("Github username: ")  # Nothing was provided
else:  # A name was provided
    GIT = sys.argv[1]
# Query the GitHub API for a list of the user's repositories and store the response as JSON
repos = requests.get('/'.join(["http:/", "api.github.com", "users", GIT, "repos"])).json()
for i in repos:
    # Split executions of the Clone function into multiple threads to clone larger profiles faster
    threading.Thread(target=clone, args=(GIT, i["name"])).start()
