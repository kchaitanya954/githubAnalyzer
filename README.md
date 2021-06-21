# githubAnalyzer

## 1. Clone repository
```bash
git clone https://github.com/kchaitanya954/githubAnalyzer.git
```

## 2. Install dependencies
```bash
pip install -r requirements.txt
```

## 3. To save the flake8 style analysis of every python code in the repository
```bash
python git_style.py --username {username}
```
Enter the username of the github user as an arument parser (-user, --username) to get the style information in the form of json file.

## 4. To reformat your git cloned
```bash
python reformat.py --username {username}
```
