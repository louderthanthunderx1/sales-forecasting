import pandas as pd
import joblib

def predict_model(model_save_path, data):
    model = joblib.load(f'{model_save_path}/sales_forecasting_model.pkl')
    predictions = model.predict(data)
    return predictions

if __name__ == '__main__':
    # Example usage
    data = pd.DataFrame({'month': [1, 2], 'year': [2022, 2022]})
    predictions = predict_model('models', data)
    print(predictions)
