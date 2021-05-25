from github import Github
import requests
import urllib.request


# username = raw_input("Enter the github username:")
# request = requests.get('https://api.github.com/users/'+username+'/repos')
# json = request.json()
# print(json)
#for i in range(0,len(json)):
#    print("Project Number:",i+1)
#    print("Project Name:",json[i]['name'])
#    print("Project URL:",json[i]['svn_url'],"\n")
    
# webUrl  = urllib.request.urlopen('https://github.com/kchaitanya954')
# print ("result code: " + str(webUrl.getcode()))

# # read the data from the URL and print it
# data = webUrl.read()
# print (data[0])

g = Github()
user = g.get_user('kchaitanya954')
# for repo in user.get_repos():
#     print(repo) 

rep = user.get_repo('clickhouse_kafka')
print(rep)
print(rep.get_readme)
# import urllib3
# http = urllib3.PoolManager()
# r = http.request('GET', 'https://github.com/kchaitanya954')
# print(r.status)
# print(r.data)