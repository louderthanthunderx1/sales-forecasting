import pandas as pd
import os

def make_dataset(raw_data_path, interim_data_path):
    raw_data_file = os.path.join(raw_data_path, 'sales_data.csv')
    interim_data_file = os.path.join(interim_data_path, 'sales_data_interim.csv')

    # Create some dummy data for example
    data = pd.DataFrame({'date': pd.date_range(start='1/1/2020', periods=100, freq='D'),
                         'sales': range(100)})
    data.to_csv(raw_data_file, index=False)

    data = pd.read_csv(raw_data_file)
    data.dropna(inplace=True)
    data.to_csv(interim_data_file, index=False)

if __name__ == '__main__':
    make_dataset('data/raw', 'data/interim')