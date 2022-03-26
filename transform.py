from extraction import ParseDataFromCsv
import pandas as pd
from utils import make_hash
from datetime import datetime

extract = ParseDataFromCsv()

data1 = extract.dealership_1('data/feeds/provider1/dealership1.csv')
data2 = extract.dealership_2('data/feeds/provider2/dealership2.csv')
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df1.insert(0, 'hash', [make_hash(
    'data/feeds/provider1/dealership1.csv') for i in range(len(df1))])
df2.insert(0, 'hash', [make_hash(
    'data/feeds/provider2/dealership2.csv') for i in range(len(df2))])
main_df = pd.concat([df1, df2], axis=0)
main_df['updated_at'] = [datetime.now().astimezone()
                         for i in range(len(main_df))]
main_df.replace('', 0, inplace=True)
main_df = main_df.astype({'mileage': 'int', 'dealer_year': 'int', 'dealer_msrp': 'int',
                          'dealer_invoice': 'int', 'dealer_inventory_entry_date': 'datetime64[ns]'})
