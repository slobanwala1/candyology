import requests
from bs4 import BeautifulSoup
import csv
import config


# Pull table HTML contents from site using requests and headers
page = requests.get(config.url, headers=config.headers)
soup = BeautifulSoup(page.content, 'html.parser')

# clean out all the junk

tableList = [td.text.replace("\t","").replace("\n","").replace(" ", "") for td in soup.find_all('td')]



#Finds the table headers
table_headers = [th.text.replace("\t","").replace("\n","").replace(" ", "") for th in soup.find_all('th')]

# List size
n = len(table_headers)

# using list comprehension
try:
    final = [tableList[i * n:(i + 1) * n] for i in range((len(tableList) + n - 1) // n)]

    # Write to CSV
    with open(config.csv_path, 'w') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(table_headers)

        # writing the data rows
        writer.writerows(final)
        csv_file.close()
except ZeroDivisionError:
    print("No Table Found")
