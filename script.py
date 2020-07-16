import argparse
import requests
from git import Repo

# Handle arguments with argparse
parser = argparse.ArgumentParser(description="Clone a GitHub or GitLab profile")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--gitlab", action="store_true", help="clone a GitLab Profile")
group.add_argument("--github", action="store_true", help="clone a GitHub Profile")
parser.add_argument("username", help="username of the profile to clone")
parser.add_argument("path", help="folder to clone repositories into")
args = parser.parse_args()

repositories = []

if args.gitlab:
    # Request a GitLab user's repositories
    page = 1
    while True:
        request = \
            requests.get(f"https://gitlab.com/api/v4/users/{args.username}/projects?per_page=100&page={page}").json()
        if not request:
            break
        else:
            for repo in [repo for repo in request]:
                repositories.append({"url": repo["http_url_to_repo"], "name": repo["name"]})
            page += 1

elif args.github:
    # Request a GitHub user's repositories
    page = 1
    while True:
        request = requests.get(f"https://api.github.com/users/{args.username}/repos?per_page=100&page={page}").json()
        if not request:
            break
        else:
            for repo in [repo for repo in request]:
                repositories.append({"url": repo["clone_url"], "name": repo["name"]})
            page += 1

# Clone repositories
print(f"Found {len(repositories)} repositories to clone")
for repo in repositories:
    print("Cloning Project: " + repo["name"])
    Repo.clone_from(repo["url"], args.path + "/" + repo["name"])