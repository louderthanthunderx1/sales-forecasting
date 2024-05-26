import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

def train_model(split_data_path, model_save_path):
    train_data_file = f'{split_data_path}/train_data.csv'
    train_data = pd.read_csv(train_data_file)

    X_train = train_data[['month', 'year']]
    y_train = train_data['sales']

    model = LinearRegression()
    model.fit(X_train, y_train)

    os.makedirs(model_save_path, exist_ok=True)
    joblib.dump(model, f'{model_save_path}/sales_forecasting_model.pkl')

    print('Model trained and saved successfully!')

if __name__ == '__main__':
    train_model('data/split', 'models')
