import pandas as pd
import os

def generate_new_data(new_data_path):
    # Example: Generate new data for the next 6 months
    new_data = pd.DataFrame({
        'month': [1, 2, 3, 4, 5, 6],
        'year': [2024, 2024, 2024, 2024, 2024, 2024]
    })

    os.makedirs(new_data_path, exist_ok=True)
    new_data.to_csv(f'{new_data_path}/new_data.csv', index=False)

if __name__ == '__main__':
    generate_new_data('data/new')
