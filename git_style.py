from repoDownload import gitDownload
from local_style import localCodeSyle
import json
import argparse
import os


class gitStyle:
    def __init__(self, username):
        self.username = username

    def style(self):
        gitDownload(username).cloneRepo()
        repo_list = gitDownload(username).getRepo()
        user_json = {}
        for repo in repo_list:
            repo_name = repo["full_name"]
            repo_local_path = f"github/{repo_name}"
            style = localCodeSyle(repo_local_path)
            repo_json = style.repo_style()
            user_json[repo_name] = {
                "repo_url": repo["html_url"],
                "repo_style": repo_json,
            }

        return user_json

    def save_json(self):
        json_style = gitStyle(self.username).style()
        try:
            os.mkdir("jsonFiles")
        except:
            pass
        try:
            with open(f"jsonFiles/{self.username}.json", "w") as json_file:
                json.dump(json_style, json_file)
            print(f"json file saved at location {os.getcwd()}")
        except:
            print("json file already exists")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="add username of github profile")
    parser.add_argument(
        "-user",
        "--username",
        type=str,
        action="store",
        dest="username",
        help="username of github user",
    )
    args = parser.parse_args()
    try:
        username = args.username
        github_python = gitStyle(username)
        github_python.save_json()
    except:
        username = input("Enter github username: ")
        github_python = gitStyle(username)
        github_python.save_json()
