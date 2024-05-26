import pandas as pd
import joblib
import os

def predict_model(model_save_path, new_data_path, prediction_save_path):
    model_file = f'{model_save_path}/sales_forecasting_model.pkl'
    new_data_file = f'{new_data_path}/new_data.csv'
    prediction_file = f'{prediction_save_path}/predictions.csv'

    if not os.path.exists(new_data_file):
        print(f"No new data file found at {new_data_file}. Skipping predictions.")
        return

    model = joblib.load(model_file)
    new_data = pd.read_csv(new_data_file)
    
    X_new = new_data[['month', 'year']]
    predictions = model.predict(X_new)

    new_data['predictions'] = predictions

    os.makedirs(prediction_save_path, exist_ok=True)
    new_data.to_csv(prediction_file, index=False)

    print(f'Predictions saved to {prediction_file}')

if __name__ == '__main__':
    predict_model('models', 'data/new', 'data/predictions')
