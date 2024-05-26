import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

def train_model(processed_data_path, model_save_path):
    processed_data_file = f'{processed_data_path}/sales_data_processed.csv'
    data = pd.read_csv(processed_data_file)

    X = data[['month', 'year']]
    y = data['sales']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    joblib.dump(model, f'{model_save_path}/sales_forecasting_model.pkl')

    print('Model trained and saved successfully!')

if __name__ == '__main__':
    train_model('data/processed', 'models')
