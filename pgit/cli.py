import argparse
import sys
import os
from datetime import datetime


def main(): 
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="command", required=True)

    if len(sys.argv) == 1:
        return noarg()

    main_parser = subparser.add_parser("main")
    main_parser.set_defaults(func=default)

    testfunc_parser = subparser.add_parser("testfunc")
    testfunc_parser.set_defaults(func = testfunc)

    init_parser = subparser.add_parser("init")
    init_parser.add_argument("location")
    init_parser.add_argument("msg", nargs="?", default = "repo")
    init_parser.set_defaults(func = init)

    setcurrentrepo_parser = subparser.add_parser("setcurrent")
    setcurrentrepo_parser.add_argument("location")
    setcurrentrepo_parser.set_defaults(func = setcurrentrepo)

    getcurrentrepo_parser = subparser.add_parser("current")
    getcurrentrepo_parser.set_defaults(func = getcurrentrepo)

    getallrepos_parser = subparser.add_parser("allrepos")
    getallrepos_parser.set_defaults(func = getallrepos)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        print("No command provided")

def default(args=None):
    print("MEOW")

def testfunc(args=None):
    print("Printing info from testfunc()")

def noarg():
    print("No arguments provided")

def getallrepos(args=None):
    project_path = "/Users/pearcepackman/Documents/Personal/CodingProjects/PGitTests"
    repos = os.listdir(project_path)
    print("")
    for repo in repos:
        repo_path = os.path.join(project_path, repo)
        if os.path.isdir(repo_path):
            print(repo)
    print("")

def setcurrentrepo(args):
    print("")
    project_path = args.location
    os.chdir(args.location)
    print("Location changed!")
    print("")

def getcurrentrepo():
    print("")#NOT WORKING AT ALL LOL
    print(f"Current Repo: ")
    print("")

def init(args):
    print("")
    project_path = os.path.join(args.location, args.msg)

    
    try: 
        os.mkdir(project_path)
        print(f"Init started at: {project_path}")
        history(project_path, "Repo initialized")
        os.chdir(project_path)
        print(f"Current directory: {project_path}")
    except:
        print(f"INIT FAILED")
    print("")

def history(path, action):
    history_path = os.path.join(path, "history.txt")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] : {action}\n"

    try:
        with open(history_path, "a") as file:
            file.write(entry)
    except:
        print('failed to write')