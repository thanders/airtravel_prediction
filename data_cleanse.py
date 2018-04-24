import pandas


# Pandas settings:
pandas.set_option('display.max_rows', 999)
pandas.set_option('display.max_columns', 999)
pandas.set_option('precision', 5)

# File variables:
file_country_currency = 'countrycurrency.csv'
file_c_rates = 'currencyrates.csv'
file_aircraft = 'aircraft.csv'
file_airport = 'airport.csv'


# The purpose of this class is to handle all data cleanse activities for each file
class DataCleanse:

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_folder = 'data_files/'
        self.file_folder_clean = 'clean_files/'
        self.df = pandas.read_csv(self.file_folder+self.file_name, keep_default_na=True, sep=',\s+', delimiter=',', skipinitialspace=False)
        self.rows = self.df.shape[0]
        self.columns = self.df.shape[1]
        self.naan = None

    def null_count(self):
        print()
        print(self.file_name, ":")
        print(self.df.isnull().sum())

    def clean(self):
        self.df.drop_duplicates()  # Remove duplicate rows
        print("Cleaning ", self.file_name, ":")

        # Cleaning specific to the currencyrates.csv file:
        if self.file_name == 'currencyrates.csv':
            print("Removing currency code duplicates")
            self.df.drop_duplicates(subset='currency_code', keep="last")
            self.df.drop(columns=['currency_name'], axis=1, inplace=True)

        # Cleaning specific to the countrycurrency.csv file:
        if self.file_name == 'countrycurrency.csv':
            print("Dropped columns that aren't required")
            self.df.drop(columns=['name', 'name_fr', 'ISO3166-1-Alpha-2', 'ISO3166-1-Alpha-3', 'ISO3166-1-numeric', 'ITU', 'MARC', 'WMO', 'DS', 'Dial', 'FIFA', 'FIPS', 'GAUL', 'IOC', 'currency_minor_unit', 'currency_name', 'currency_numeric_code', 'is_independent'], axis=1, inplace=True)
            self.df.dropna(axis=0, how='all')
            self.df = self.df[self.df['currency_country_name'].notnull()]
            self.df = self.df[self.df['currency_code'].notnull()]

        # Cleaning specific to the airport.csv file:
        if self.file_name == 'airport.csv':
            self.df = self.df[self.df['OAHR'].notnull()]

    @staticmethod
    def process_files():
        print("Clean data:")
        cleanse_country.clean()
        cleanse_currency.clean()
        cleanse_airport.clean()
        cleanse_aircraft.clean()

    @staticmethod
    def export_files():
        cleanse_country.export()
        cleanse_currency.export()
        cleanse_airport.export()
        cleanse_aircraft.export()

    @staticmethod
    def merge():

        # Merge countrycurrency.csv and currencyrates.csv
        global Country_Currency
        Country_Currency = pandas.merge(cleanse_country.df, cleanse_currency.df, how='left', left_on=['currency_code'],
                                        right_on=['currency_code'])

    def export(self):
        if self.file_name == 'countrycurrency.csv' or self.file_name == 'currencyrates.csv':
            Country_Currency.to_csv('clean_files/Clean_Country_Currency.csv')
        else:
            self.df.to_csv('clean_files/'+self.file_name+'.csv')


# Create instances of each class:
cleanse_country = DataCleanse(file_country_currency)
cleanse_currency = DataCleanse(file_c_rates)
cleanse_airport = DataCleanse(file_airport)
cleanse_aircraft = DataCleanse(file_aircraft)


# Perform data cleanse:
DataCleanse.process_files()

# Merge files:
DataCleanse.merge()

# Export clean csv files:
DataCleanse.export_files()


# Load new countrycurrency file into CCAtlas with rates
# Load airport into airport class