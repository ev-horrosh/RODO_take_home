import csv
from datetime import datetime
from utils import make_hash

class ParseDataFromCsv():
    '''
    extracts necessary data from csvs provided the path for the dealership

    '''

    def __init__(self):
        pass

    def dealership_1(self, file):

        dealership1 = []
        with open(file, 'r') as f:
            filereader = csv.DictReader(f)
            for r in filereader:
                dealership1.append({
                    'hash':make_hash(file),
                    'dealership_id': r['Dealer ID'],
                    'vin': r['VIN'],
                    'mileage': r['Miles'],
                    'is_new': [True if r['Type'].lower() == 'new' else False for i in r['Type']][0],
                    'stock_number': r['Stock'],
                    'dealer_year': r['Year'],
                    'dealer_make': r['Make'],
                    'dealer_model': r['Model'],
                    'dealer_trim': r['Trim'],
                    'dealer_model_number': r['ModelNumber'],
                    'dealer_msrp': [r['List Price'] for i in r['MSRP'] if r['Type'].lower() != 'new'][0],
                    'dealer_invoice': [r['List Price'] if r['Type'].lower() != 'new' else r['Invoice'] for i in r['Invoice']][0],
                    'dealer_body': r['Body'],
                    'dealer_inventory_entry_date':datetime.strptime(r['DateInStock'],'%m/%d/%Y'),
                    'dealer_exterior_color_description': r['ExteriorColor'],
                    'dealer_interior_color_description': r['InteriorColor'],
                    'dealer_exterior_color_code': r['ExteriorColorCode'],
                    'dealer_interior_color_code': r['InteriorColorCode'],
                    'dealer_transmission_name': None,
                    'dealer_installed_option_codes': [r['OptionCode']],
                    'dealer_installed_option_descriptions': [r['OptionDescription']],
                    'dealer_additional_specs': r['AdditionalSpecs'],
                    'dealer_doors': None,
                    'dealer_drive_type': r['Drivetrain'],
                    'updated_at': datetime.now(),
                    'dealer_images': [i for i in r['ImageList'].split(',')],
                    'dealer_certified': [True if r['Certified'].lower() == 'yes' else False for i in r['Certified']][0]
                })

        return dealership1

    def dealership_2(self, file):

        dealership2 = []
        with open(file, 'r') as f:
            filereader = csv.DictReader(f)
            for r in filereader:
                dealership2.append({
                    'hash':make_hash(file),
                    'dealership_id': r['DealerId'],
                    'vin': r['VIN'],
                    'mileage': r['Mileage'],
                    'is_new': [True if r['New/Used'].lower() == 'n' else False for i in r['New/Used']][0],
                    'stock_number': r['Stock #'],
                    'dealer_year': r['Year'],
                    'dealer_make': r['Make'],
                    'dealer_model': r['Model'],
                    'dealer_trim': r['Trim'],
                    'dealer_model_number': r['Model Code'],
                    'dealer_msrp': None if not r['MSRP'] else int(r['MSRP']),
                    'dealer_invoice': None if not r['Invoice'] else int(r['Invoice']),
                    'dealer_body': None,
                    'dealer_inventory_entry_date': datetime.strptime(r['Inventory Date'],'%m/%d/%Y'),
                    'dealer_exterior_color_description': r['Exterior Color'],
                    'dealer_interior_color_description': r['Interior Color'],
                    'dealer_exterior_color_code': r['Exterior Color Code'],
                    'dealer_interior_color_code': r['Interior Color Code'],
                    'dealer_transmission_name': r['Transmission'],
                    'dealer_transmission_type': None,
                    'dealer_installed_option_codes': [r['Option Codes']],
                    'dealer_installed_option_descriptions': [r['Options']],
                    'dealer_additional_specs': None,
                    'dealer_doors': None,
                    'dealer_drive_type': None,
                    'dealer_images': [i for i in r['Photos'].split('|')],
                    'dealer_certified': None
                })
        return dealership2
