import csv
from pprint import pprint



# create a dictionary
covid_test_record = {
    'Name': 'Jonah Henschel',
    'ID Number': 123456,
    'Result': 'negative',
    'Date': '03-03-2022',
}

ms_ifft_covid_test_record = {
    'Name': 'Brianna Ifft',
    'ID Number': 123457,
    'Result': 'negative',
    'Date': '03-03-2022',
}

print(covid_test_record)

# add an element to a dictionary
covid_test_record['Grade Level'] = 12

print(covid_test_record)

# retrieve an element from your dictionary
print(covid_test_record["ID Number"])

# retrieve an element from your dictionary using get
print(covid_test_record.get("Grade Level"))
print(ms_ifft_covid_test_record.get("Grade Level"))

# update a key value pair
covid_test_record["Result"] = "positive"

print(covid_test_record)

# iterate over dictionary
for key in covid_test_record:  # i will be the key of the key value pair
    print(key + ": " + str(covid_test_record[key]))


csv_file = open('phone_book.csv')
phone_book_reader = csv.DictReader(csv_file)
print(list(phone_book_reader))