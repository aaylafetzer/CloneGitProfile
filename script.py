import os
import requests
import subprocess
import platform

GIT = None
PATH = None
PLATFORM = platform.system()

if PLATFORM == "Windows":
    # If the program is running on Windows
    PATH = "%USERPROFILE%\\Documents\\Code\\"
else:
    # This should work if it's most things that aren't Windows
    PATH = "${HOME}/Documents/Code/"

# Get gitlab profile name
user = input("GitLab username: ")

# Query the GitHub API for a list of the user's repositories and store the response as JSON
API_URL = f"https://gitlab.com/api/v4/users/{user}/projects"
print("Sending query to GitLab API")
data = requests.get(url=API_URL).json()
print(str(len(data)) + " Public projects found")
# Print out a response
for project in data:
    print("Cloning " + project["name"])
    http_url = project["http_url_to_repo"]
    path = PATH + project["path"]
    command = f"git clone {http_url} {path}"
    # Using subprocess instead of os.system because os.system is deprecated
    with open(os.devnull, 'wb') as devnull:
        subprocess.call(command, shell=True, stdout=devnull, stderr=devnull)
