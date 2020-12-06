import json

# file = open('nekos_randoms.json', 'r')
with open('nekos_randoms.json', 'r') as file : 
	data = json.loads(file.read())
	print(data["sfw"]["meow"])