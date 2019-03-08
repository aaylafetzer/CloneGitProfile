import os, sys, requests, json, threading, platform

GIT = None
PATH = None
PLATFORM = platform.system()
    
def Clone(git, repo): #Run git clone command
    os.system("git clone " + '/'.join(['https:/','github.com',git,repo]) + ".git " + '/'.join([PATH,repo])) #Use the system command line to run git clone

#Detect what platform the script is running on
if (PLATFORM == "Linux" or PLATFORM == "Darwin"): #The script is running on Linux or MacOS
    PATH = "~/Documents/Code/"
elif (PLATFORM == "Windows"): #The script is running on garbage
    PATH = "%USERPROFILE%\\Documents\\Code"
else: #The script can't identify the host OS
    input("Unable to identify operating system")
    exit()

if (len(sys.argv) == 1): #Test if a profile name is given in the system arguments
    GIT = input("Github username: ") #Nothing was provided
else: #A name was provided
    GIT = sys.argv[1]

repos = requests.get('/'.join(["http:/","api.github.com","users",GIT,"repos"])).json() #Query the GitHub API for a list of the user's repositories and store the repsonse as JSON
for i in repos:
    threading.Thread(target=Clone, args=(GIT, i["name"])).start() #Split executions of the Clone function into multiple threads to clone larger profiles faster