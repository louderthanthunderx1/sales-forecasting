import pandas as pd
from sklearn.metrics import mean_squared_error
import joblib

def evaluate_model(processed_data_path, model_save_path):
    processed_data_file = f'{processed_data_path}/sales_data_processed.csv'
    data = pd.read_csv(processed_data_file)

    X = data[['month', 'year']]
    y = data['sales']

    model = joblib.load(f'{model_save_path}/sales_forecasting_model.pkl')
    predictions = model.predict(X)

    mse = mean_squared_error(y, predictions)
    print(f'Mean Squared Error: {mse}')

if __name__ == '__main__':
    evaluate_model('data/processed', 'models')
