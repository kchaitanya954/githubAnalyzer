from repoDownload import gitDownload
from local_style import localCodeSyle



class gitStyle():
    def __init__(self, username):
        self.username = username
    
    def style(self):
        gitDownload(username).cloneRepo()
        repo_list = gitDownload(username).getRepo()
        user_json = {}
        for repo in repo_list:
            repo_name = repo['full_name']
            repo_local_path = f'github/{repo_name}'
            style  = localCodeSyle(repo_local_path)
            repo_json = style.repo_style()
            user_json[repo_name] = {'repo_url': repo['html_url'], 'repo_style': repo_json}
        
        return user_json

if __name__ == '__main__':
    username = input('Enter github username: ')
    github_python = gitStyle(username)
    print(github_python.style())




