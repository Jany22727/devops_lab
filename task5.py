import getpass
import requests
import sys
user = input("Github Login: ")
password = getpass.getpass()
which_rep = 'alenaPy/'
name_rep = 'devops_lab/'
print('Search info in repos' + which_rep + name_rep)
pul_nomb = input("PULL's nomber: ")
url = ('https://api.github.com/repos/' + which_rep +
       name_rep + 'pulls/' + pul_nomb)
print('Search info about ' + url)
requests = requests.get(url, auth=(user, password))
requests = requests.json()
arg = (sys.argv)
print(arg)
if str(arg) == "['task5.py', '--n']":
    print('Name:', requests['title'])
elif str(arg) == "['task5.py', '--u']":
    print('Created by:', requests['user']['login'])
if str(arg) == "['task5.py', '--c']":
    print('Created at:', requests['created_at'])
elif str(arg) == "['task5.py', '--s']":
    print('Status:', requests['labels'][0]['name'])
elif str(arg) == "['task5.py', '--a']":
    print('Name:', requests['title'])
    print('Created by:', requests['user']['login'])
    print('Created at:', requests['created_at'])
    print('Status:', requests['labels'][0]['name'])
elif str(arg) == "['task5.py', '--h']":
    print("Show all --all, Name --n , Who created --u" +
          "When created --d, Status --s")

# python task5.py --a
