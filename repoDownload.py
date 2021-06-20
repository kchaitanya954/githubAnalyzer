from github import Github
import requests
from funcy import project
import os
from git.repo.base import Repo



class gitDownload():
    def __init__(self, username):
        self.username = username

    def getRepo(self):
        response = requests.get(f"https://api.github.com/users/{self.username}/repos")
        repoJSON = response.json()
        python_repo = []
        for repo in repoJSON:
            if repo['language'] == 'Python' and repo['private'] == False:
                small_dict = project(repo, ['id', 'full_name', 'clone_url', 'html_url', 'contents_url'])
                python_repo.append(small_dict)
        return python_repo

    def cloneRepo(self):
        repos = gitDownload(self.username).getRepo()
        for repo in repos:
            Repo.clone_from(repo['clone_url'], f'github/{repo["full_name"]}')
        print(f"Repositores cloned into the file location: {os.getcwd()}")

