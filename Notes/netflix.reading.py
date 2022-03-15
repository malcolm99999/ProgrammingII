import csv
from pprint import pprint

netflix_data = open('netflix.csv')
dict_reader = csv.DictReader(netflix_data)
#pprint(list(dict_reader))

show_title = input("What show do you want to know about?: ")
show_info = input("What would you like to know about it?: ")

for i in (list(dict_reader)):
    if i.get('Title') == show_title:
        print(i[show_info])
        break
    else:
        print("Not in list")
