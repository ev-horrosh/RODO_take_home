from dataclasses import field
from extraction import ParseDataFromCsv
import pandas as pd
from models.models import Table
import csv

extract = ParseDataFromCsv()

data1 = extract.dealership_1('data/feeds/provider1/dealership1.csv')
data2 = extract.dealership_2('data/feeds/provider2/dealership2.csv')
dealer_data1 = [Table(**d).dict() for d in data1]
dealer_data2 = [Table(**d).dict() for d in data2]
df1 = pd.DataFrame(dealer_data1)
df2 = pd.DataFrame(dealer_data2)
main_df = pd.concat([df1, df2], axis=0)
main_df.replace('', 0, inplace=True)

''' OPTIONAL CSV WRITE DATA TO ONE CSV'''
# with open('main.csv', 'w',newline='') as main:
#     fieldnames=list(dealer_data1[0].keys())
#     writer=csv.DictWriter(main,fieldnames=fieldnames)
#     writer.writeheader()
#     for r in dealer_data1:
#         writer.writerow(r)
#     for r in dealer_data2:
#         writer.writerow(r)