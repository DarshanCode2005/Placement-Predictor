# Placement Prediction Using Logistic Regression

## Project Overview

This project aims to predict job placement outcomes using a logistic regression model. The model was trained on a small dataset and achieved an accuracy of 88%. The dataset has been preprocessed using one-hot encoding to handle categorical variables.

## Implementation Details

- **Model:** Logistic Regression
- **Accuracy:** 88%
- **Preprocessing:** One-hot encoding for categorical features
- **Dataset:** A small dataset uploaded along with this project
- **Application:** A Streamlit-based web app to interact with the model

## Streamlit Application

The trained logistic regression model has been integrated into a Streamlit app (`app.py`) to allow users to input features and get placement predictions.

## How to Run the App

1. Run the Streamlit application:
   ```sh
   streamlit run app.py
   ```

## Files Included

- **app.py** - Streamlit application script
- **model.pkl** - Saved logistic regression model
- **Job\_Placement\_Data.csv** - Dataset used for training
- **Placement\_prediction.ipynb** - Python Notebook 

## Future Improvements

- Expand dataset size for better generalization
- Experiment with other machine learning models
- Add more features to improve prediction accuracy

## Author

Developed by Darshan