import os
import sys
import requests
import threading
import platform

GIT = None
PATH = None
PLATFORM = platform.system()


def clone(profile_name, repository_name, profile_in_path=False):  # Run git clone command
    """
    Clone a github repository
    :param profile_name: GitHub username
    :param repository_name: GitHub repository url
    :param profile_in_path: Whether to include the profile as a subfolder
    :return:
    """
    if profile_in_path:
        command = f"git clone https://github.com/{profile_name}/{repository_name}.git \"{PATH}/{profile_name}/" \
                  f"{repository_name}\""
    else:
        command = f"git clone https://github.com/{profile_name}/{repository_name}.git \"{PATH}/{repository_name}\""
    os.system(command)


if PLATFORM == "Windows":
    # Detect what platform the script is running on
    PATH = "%USERPROFILE%\\Documents\\Code"
else:
    # 99.99% Chance this is a Linux distro and if it's not you shouldn't expect this to work
    PATH = "${HOME}/Documents/Code/"

# Get a list of provided profiles
profiles = [argument for argument in sys.argv[1::] if argument[0] != "-"]
print(profiles)

if len(profiles) == 0:
    profiles.append(input("GitHub Username: "))

# Query the GitHub API for a list of the user's repositories and store the response as JSON
for profile in profiles:
    repos = requests.get(f"http://api.github.com/users/{profile}/repos").json()
    for repo in repos:
        # Split executions of the Clone function into multiple threads to clone larger profiles faster
        if '-t' in sys.argv:
            threading.Thread(target=clone, args=(profile, repo["name"], len(profiles) > 1)).start()
        else:
            clone(profile, repo["name"], len(profiles) > 1)
