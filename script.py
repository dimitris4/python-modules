import requests

content = requests.get('https://github.com/dimitris4/python-modules/blob/master/script.py')

print(content)