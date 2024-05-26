import pandas as pd

def build_features(interim_data_path, processed_data_path):
    interim_data_file = f'{interim_data_path}/sales_data_interim.csv'
    processed_data_file = f'{processed_data_path}/sales_data_processed.csv'

    data = pd.read_csv(interim_data_file)
    data['month'] = pd.to_datetime(data['date']).dt.month
    data['year'] = pd.to_datetime(data['date']).dt.year

    data.to_csv(processed_data_file, index=False)

if __name__ == '__main__':
    build_features('data/interim', 'data/processed')
