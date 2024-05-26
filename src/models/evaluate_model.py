import pandas as pd
from sklearn.metrics import mean_squared_error
import joblib

def evaluate_model(split_data_path, model_save_path):
    test_data_file = f'{split_data_path}/test_data.csv'
    test_data = pd.read_csv(test_data_file)

    X_test = test_data[['month', 'year']]
    y_test = test_data['sales']

    model = joblib.load(f'{model_save_path}/sales_forecasting_model.pkl')
    predictions = model.predict(X_test)

    mse = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse}')

if __name__ == '__main__':
    evaluate_model('data/split', 'models')
