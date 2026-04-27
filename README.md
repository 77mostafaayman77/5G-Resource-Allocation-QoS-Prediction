# 5G Resource Allocation and QoS Prediction

An end-to-end Machine Learning project designed to optimize dynamic resource allocation in 5G networks. The model predicts the optimal Resource Allocation Ratio based on real-time network conditions and specific application Quality of Service (QoS) requirements.

## Project Overview
In 5G networks, efficient resource distribution is critical. This project uses a dataset containing various 5G traffic types (like VoIP, Video Streaming, and IoT) to learn how a network should prioritize bandwidth under different signal strengths and latency conditions.

## Data Preprocessing
We transformed raw telecommunications data into a clean format ready for machine learning:
- Text Extraction: Used Regular Expressions to extract numbers from text (like getting "-80" from "-80 dBm").
- Unit Normalization: Converted all bandwidth values to Mbps and latency to seconds so all metrics use the same scale.
- Feature Encoding: Converted categorical data (application types) into numerical format using One-Hot Encoding.
- Data Cleanup: Removed redundant columns to prevent the model from cheating (Data Leakage).

## Exploratory Data Analysis (EDA)
Key findings from the data:
- Voice calls (VoIP) have a strong connection with high resource allocation, showing they get top priority.
- Higher latency (delay) leads to a clear drop in allocated resources.
- Important real-time apps (like VoIP and Streaming) get steady high resources, while background tasks (like IoT sensors) get wider, lower priority allocation.

## Features and Target
- Input Features: Signal Strength (dBm), Latency (seconds), Required Bandwidth (Mbps), and Application Type.
- Target Variable: Resource Allocation (a ratio from 0.0 to 1.0 representing the percentage of resources given).

## Machine Learning Pipeline
- Data Splitting: Divided the dataset into 80% for training and 20% for testing to properly evaluate the model.
- Feature Scaling: Applied StandardScaler to the input features so all numbers are treated fairly by the algorithms.
- Model Selection: Tested multiple algorithms including Linear Regression, Random Forest, XGBoost, and SVR.
- Optimization: Selected the Random Forest Regressor and improved it using RandomizedSearchCV to find the best settings without overfitting.
- Results: The final model achieved a highly stable Cross-Validated R-squared score of approximately 93%.
- Export: Saved the trained model and the scaler as `.pkl` files to be used in a real-time web application.

## Project Status
- [x] Data Cleaning and Unit Normalization
- [x] Feature Engineering and Encoding
- [x] Exploratory Data Analysis (EDA)
- [x] Train/Test Data Splitting and Scaling
- [x] Model Training and Hyperparameter Tuning
- [x] Model Export (.pkl files)
- [ ] Web App Deployment (Streamlit)

## Tech Stack
- Language: Python
- Libraries: Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn, Joblib
