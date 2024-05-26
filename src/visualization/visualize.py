import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(processed_data_path, figures_path):
    processed_data_file = f'{processed_data_path}/sales_data_processed.csv'
    data = pd.read_csv(processed_data_file)

    plt.figure(figsize=(10, 6))
    plt.plot(data['date'], data['sales'])
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.title('Sales Over Time')
    plt.savefig(f'{figures_path}/sales_over_time.png')
    plt.show()

if __name__ == '__main__':
    visualize_data('data/processed', 'reports/figures')
