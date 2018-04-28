import pandas


# Pandas settings:
pandas.set_option('display.max_rows', 999)
pandas.set_option('display.max_columns', 999)
pandas.set_option('precision', 2)

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
        self.airport_cc_df = None
        self.airport_file_merged = 'clean_airport_cc.csv'
        self.aircraft_file_clean = 'clean_aircraft.csv'

    def null_count(self):
        print()
        print(self.file_name, ":")
        print(self.df.isnull().sum())

    def clean(self):
        self.df.drop_duplicates()  # Remove duplicate rows
        print("Cleaning : ", self.file_name)

        # Cleaning specific to the currencyrates.csv file:
        if self.file_name == 'currencyrates.csv':
            # Remove currency code duplicates
            self.df.drop_duplicates(subset='currency_code', keep="last")
            # Drop columns
            self.df.drop(columns=['currency_name'], axis=1, inplace=True)

        # Cleaning specific to the countrycurrency.csv file:
        if self.file_name == 'countrycurrency.csv':
            # drop columns that aren't required
            self.df.drop(columns=['name_fr', 'ISO3166-1-Alpha-2', 'ISO3166-1-Alpha-3', 'ISO3166-1-numeric', 'ITU', 'MARC', 'WMO', 'DS', 'Dial', 'FIFA', 'FIPS', 'GAUL', 'IOC', 'currency_minor_unit', 'currency_name', 'currency_numeric_code', 'is_independent', 'currency_country_name'], axis=1, inplace=True)
            self.df.dropna(axis=0, how='all')
            # drop entire rows where currency code is null
            self.df = self.df[self.df['currency_code'].notnull()]
            # convert country_key column to lowercase
            self.df['country_key'] = self.df['country_key'].str.lower()

        # Cleaning specific to the airport.csv file:
        if self.file_name == 'airport.csv':
            self.df = self.df[self.df['a_icao'].notnull()]
            # drop columns that aren't required
            self.df.drop(columns=['a1', 'a2', 'a3', 'a4'], axis=1, inplace=True)
            # Convert strings in column to uppercase:
            self.df['country_key'] = self.df['country_key'].str.lower()

        # If filename is aircraft.csv perform the merge:
        if self.file_name == file_airport or self.file_name == file_c_rates:
            self.merge()
        self.export()

    # Performs merging operations (if necessary)
    def merge(self):

        # Merge countrycurrency and currencyrates csv files
        country_currency = pandas.merge(country_c.df, currency_c.df, on=['currency_code'])
        # Merge country_currency_df with cleanse_airport.df
        self.airport_cc_df = pandas.merge(airport_c.df, country_currency, on='country_key')

    # Exports files
    def export(self):
        if self.file_name == file_airport:
            # index = false removes the index from the CSV file
            self.airport_cc_df.to_csv('clean_files/'+self.airport_file_merged, index=False)
            print('Created  : ', self.airport_file_merged)
        elif self.file_name == file_aircraft:
            self.df.to_csv('clean_files/'+self.aircraft_file_clean, index=False)
            print('Created  : ', self.aircraft_file_clean)

    @staticmethod
    # Create instances for each file:
    def initialize():
        global country_c, currency_c, airport_c, aircraft_c
        country_c = DataCleanse(file_country_currency)
        currency_c = DataCleanse(file_c_rates)
        airport_c = DataCleanse(file_airport)
        aircraft_c = DataCleanse(file_aircraft)
        print("DataCleanse instances initialized:")
        return country_c, currency_c, airport_c, aircraft_c

    @staticmethod
    # Create instances for each file:
    def start_clean():
        country_c.clean()
        currency_c.clean()
        airport_c.clean()
        aircraft_c.clean()
        return 0


