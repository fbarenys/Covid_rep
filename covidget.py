from bs4 import BeautifulSoup
import codecs
import pandas as pd

file = codecs.open("///Users/felixbarenysmarimon/Downloads/lineage_list.html", "r", "utf-8")



soup = BeautifulSoup(file, 'html.parser')

# empty list
data = []
# for getting the header from
# the HTML file
list_header = []

header = soup.find_all("table")[0].find("tr")
print(header)
for items in header:
    try:
        list_header.append(items.get_text())
    except:
        continue

# for getting the data
HTML_data = soup.find_all("table")[0].find_all("tr")[1:]

for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue
    data.append(sub_data)

# Storing the data into Pandas
# DataFrame
dataFrame = pd.DataFrame(data=data, columns=list_header)

# Converting Pandas DataFrame
# into CSV file
dataFrame.to_csv('covid_variants.csv')