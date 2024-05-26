import pandas as pd
from sklearn.model_selection import train_test_split
import os

def split_data(processed_data_path, split_data_path, test_size=0.2, random_state=42):
    processed_data_file = f'{processed_data_path}/sales_data_processed.csv'
    train_data_file = f'{split_data_path}/train_data.csv'
    test_data_file = f'{split_data_path}/test_data.csv'

    data = pd.read_csv(processed_data_file)
    
    train_data, test_data = train_test_split(data, test_size=test_size, random_state=random_state)

    os.makedirs(split_data_path, exist_ok=True)
    train_data.to_csv(train_data_file, index=False)
    test_data.to_csv(test_data_file, index=False)

if __name__ == '__main__':
    split_data('data/processed', 'data/split')
