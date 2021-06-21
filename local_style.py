
from flake8.api import legacy
import io
from contextlib import redirect_stdout
import os




class localCodeSyle():
    def __init__(self, path):
        self.path = path

    def getLocalFile(self, filter_extension='.py'):
        pythonFiles = {}
        for root, _, files in os.walk(self.path):
            for file in files:
                if filter_extension is None or file.lower().endswith(filter_extension):
                    pythonFiles[file] = f'{root}/{file}'
                
        return pythonFiles

    def checkStyle(self, file_path):
        with io.StringIO() as out, redirect_stdout(out):
            style_guide = legacy.get_style_guide()
            report = style_guide.check_files([file_path])
            agg_report =report.get_statistics('')
            flake8output = out.getvalue()[:-2].split('\n')
            err_json = {}
            file_json = {}
            # if len(flake8output) > 0:
            try:
                for err in flake8output:                
                    details = err.split(':')
                    row = details[1]
                    col = details[2]
                    error = details[3]
                    key = f'row: {row}_col: {col}'
                    err_json[key] = error
                    file_json["formatting_errors"] = err_json
                    file_json["agg_report"] = agg_report
            except:
                file_json["formatting_errors"] = None
                file_json["agg_report"] = None

          
        return file_json

    def repo_style(self):
        python_files = localCodeSyle(self.path).getLocalFile()
        repo_style_json = {}
        for key, value in python_files.items():
            repo_style_json[key] = localCodeSyle(self.path).checkStyle(value)
            endpoint = value.replace(self.path, '')
            repo_path = self.path.split('/', 1)[1]
            repo_style_json[key]['file_url'] = f'https://github.com/{repo_path}/blob/master{endpoint}'
        return repo_style_json