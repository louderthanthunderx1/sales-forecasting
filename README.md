# Sales Forecasting Project

This project aims to create time-series models to forecast future sales based on historical sales data.

## Project Structure

- `data/`
  - `external/`: Data from third-party sources.
  - `interim/`: Intermediate data that has been transformed.
  - `processed/`: The final, canonical data sets for modeling.
  - `raw/`: The original, immutable data dump.

- `docs/`: Documentation for the project.
- `models/`: Trained and serialized models, model predictions, or model summaries.
- `notebooks/`: Jupyter notebooks for exploration and analysis.
- `references/`: Data dictionaries, manuals, and other explanatory materials.
- `reports/`: Generated analysis as HTML, PDF, LaTeX, etc.
  - `figures/`: Generated graphics and figures to be used in reporting.
- `src/`: Source code for the project.
  - `data/`: Scripts to download or generate data.
    - `make_dataset.py`: Script to create or download datasets.
  - `features/`: Scripts to transform raw data into features suitable for modeling.
    - `build_features.py`: Script to build features from raw data.
  - `models/`: Scripts to train models and make predictions.
    - `predict_model.py`: Script to use trained models for making predictions.
    - `train_model.py`: Script to train models.
    - `evaluate_model.py`: Script to evaluate models' performance.
  - `visualization/`: Scripts for creating visualizations.
    - `visualize.py`: Script to generate visualizations for exploratory data analysis and results.
- `config/`: Configuration files for the project.
  - `config.yaml`: Configuration file for managing project settings.

## Getting Started

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Configure the project settings in `config/config.yaml`.
4. Run the data preparation scripts to generate the datasets.
5. Train and evaluate the models using the scripts in the `src/models` directory.

## Usage

- Use the Jupyter notebooks in the `notebooks` directory for exploratory data analysis and visualization.
- Refer to the scripts in the `src` directory for data processing, feature engineering, model training, prediction, and evaluation.
- or run python main.py to run all scripts.

## License

This project is licensed under the MIT License.
