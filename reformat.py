from subprocess import call
from local_style import localCodeSyle
import argparse
from repoDownload import gitDownload

class formatCode():
    def __init__(self, username):
        self.username = username
        self.repo_list = gitDownload(username).getRepo()

    def format_style(self):
        for repo in self.repo_list:
            repo_path = f"github/{repo['full_name']}"
            python_files = localCodeSyle(repo_path).getLocalFile()

            for fileName, filePath in python_files.items():
                try:
                    call(f"black {filePath}", shell=True)
                    print(f"file {fileName} got reformatted")
                except:
                    print(f"unable to format file {fileName} ")
            print(f"formating for repo {repo['full_name']} completed")
    
    def git_push(self, password):
        # for repo in self.repo_list:
            # repo_path = f"github/{repo['full_name']}"
            
        pass

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description="add username, password,  of github profile")
    parser.add_argument(
        "-U",
        "--username",
        type=str,
        action="store",
        dest="username",
        help="username of github user",
    )

    args = parser.parse_args()
    try:
        username = args.username

        format = formatCode(username)
        format.format_style()
        
    except:
        username = input("Enter github username: ")
        format = formatCode(username)
        format.format_style()

    print("-"*50)
    # push = input("Enter 1 to push the code: ")
    # if push == 1:
    #     password = input("Enter github password: ")
        


        