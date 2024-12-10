#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import time
import sys
import requests

def print_banner():
    banner = """
    \033[1;35m
    ******************************************
           \033[1;32mGIT AUTOMATION TOOL v1.0\033[1;35m         
    ------------------------------------------
    Automate GitHub repository creation and pushes      
    \033[0m
    """
    print(banner)
def install_github_cli():
    print "\033[1;34m[INFO]\033[0m Checking if GitHub CLI is installed..."
    try:
        subprocess.check_call(["gh", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print "\033[1;32m[INFO]\033[0m GitHub CLI is already installed."
    except subprocess.CalledProcessError:
        print "\033[1;33m[WARN]\033[0m GitHub CLI not found. Installing..."
        if sys.platform.startswith('linux'):
            if 'termux' in sys.argv[0]:
                subprocess.check_call(["pkg", "install", "gh"], stdout=subprocess.PIPE)
            else:
                subprocess.check_call(["sudo", "apt", "install", "gh"], stdout=subprocess.PIPE)
            print "\033[1;32m[INFO]\033[0m GitHub CLI installation complete on Linux/Termux."

        elif sys.platform == 'darwin':
            subprocess.check_call(["brew", "install", "gh"], stdout=subprocess.PIPE)
            print "\033[1;32m[INFO]\033[0m GitHub CLI installation complete on macOS."

        elif sys.platform == 'win32':
            subprocess.check_call(["choco", "install", "gh"], stdout=subprocess.PIPE)
            print "\033[1;32m[INFO]\033[0m GitHub CLI installation complete on Windows."

        else:
            print "\033[1;31m[ERROR]\033[0m Unsupported platform. GitHub CLI installation failed."
            sys.exit(1)

def authenticate_github(token):
    print "\033[1;34m[INFO]\033[0m Authenticating with GitHub..."
    auth_url = "https://api.github.com/user"
    headers = {"Authorization": "token " + token}
    response = requests.get(auth_url, headers=headers)
    if response.status_code == 200:
        print "\033[1;32m[INFO]\033[0m Authentication successful."
        return True
    else:
        print "\033[1;31m[ERROR]\033[0m Authentication failed. Please check your token."
        return False

def create_github_repo(repo_name, token):
    print "\033[1;34m[INFO]\033[0m Creating GitHub repository..."
    headers = {"Authorization": "token " + token}
    description = raw_input("\033[1;34m[INFO]\033[0m Enter a description for the repository: ")
    data = {"name": repo_name, "description": description}
    response = requests.post("https://api.github.com/user/repos", headers=headers, json=data)
    if response.status_code == 201:
        print "\033[1;32m[INFO]\033[0m Repository '" + repo_name + "' created successfully."
        return True
    else:
        print "\033[1;31m[ERROR]\033[0m Failed to create repository. Error: " + str(response.json())
        return False

def git_operations(repo_name, directory, token):
    os.chdir(directory)
    print "\033[1;34m[INFO]\033[0m Initializing git repository in " + directory + "..."
    subprocess.check_call(["git", "init"])
    subprocess.check_call(["git", "config", "--global", "--add", "safe.directory", os.getcwd()])
    github_user = os.getenv('USER') or os.getenv('USERNAME')
    if not github_user:
        github_user = raw_input("\033[1;34m[INFO]\033[0m Enter your GitHub username: ")
    print "\033[1;34m[INFO]\033[0m Adding remote repository: " + repo_name + "..."
    remote_url = "https://{}:{}@github.com/{}/{}.git".format(github_user, token, github_user, repo_name)
    try:
        subprocess.check_call(["git", "remote", "add", "origin", remote_url])
    except subprocess.CalledProcessError:
        print "\033[1;33m[WARN]\033[0m Remote origin already exists. Updating remote URL..."
        subprocess.check_call(["git", "remote", "set-url", "origin", remote_url])

    print "\033[1;34m[INFO]\033[0m Adding files and committing changes..."
    subprocess.check_call(["git", "add", "."])
    subprocess.check_call(["git", "commit", "-m", "Initial commit"])

    print "\033[1;34m[INFO]\033[0m Creating main branch and pushing changes to GitHub..."
    subprocess.check_call(["git", "branch", "-M", "main"])
    subprocess.check_call(["git", "push", "-u", "origin", "main"])
    
    tag_name = raw_input("\033[1;34m[INFO]\033[0m Enter the tag name to add: ")
    print "\033[1;34m[INFO]\033[0m Creating tag: " + tag_name + "..."
    subprocess.check_call(["git", "tag", tag_name])
    subprocess.check_call(["git", "push", "origin", tag_name])

    print "\033[1;32m[INFO]\033[0m Git operations completed."

def main():
    print_banner()
    install_github_cli()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    token_path = os.path.join(script_dir, 'token.txt')

    try:
        token = open(token_path, 'r').read().strip()
    except IOError:
        print "\033[1;31m[ERROR]\033[0m Token file not found at: " + token_path
        sys.exit(1)

    if not authenticate_github(token):
        sys.exit(1)

    repo_name = raw_input("\033[1;34m[INFO]\033[0m Enter the repository name: ")
    if not create_github_repo(repo_name, token):
        sys.exit(1)

    directory = raw_input("\033[1;34m[INFO]\033[0m Enter the directory to process files from: ")
    git_operations(repo_name, directory, token)

    print "\033[1;32m[INFO]\033[0m Workflow complete."

if __name__ == "__main__":
    main()
