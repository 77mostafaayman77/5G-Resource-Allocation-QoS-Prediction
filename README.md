# 5G Resource Allocation & QoS Prediction 

An end-to-end Machine Learning project designed to optimize dynamic resource allocation in 5G networks. The model predicts the optimal **Resource Allocation Ratio** based on real-time network conditions and specific application Quality of Service (QoS) requirements.

## Project Overview
In 5G networks, efficient resource distribution is critical. This project leverages a dataset containing various 5G traffic types (VoIP, Video Streaming, IoT, etc.) to learn how a network should prioritize bandwidth and resources under different signal strengths and latency conditions.

## Data Preprocessing
A significant portion of this project focused on transforming raw, "noisy" telecommunications data into a machine-learning-ready format:

- **Regex-Based Extraction:** Used advanced Regular Expressions (`r'(-?\d+)'`) to surgically extract numerical values from strings like "-80 dBm" or "15 Mbps", ensuring negative signs for signal strength were preserved.
- **Unit Normalization:** Developed custom functions to unify data units, converting all bandwidth metrics from Kbps to Mbps and ensuring latency is represented in seconds.
- **Feature Encoding:** Applied **One-Hot Encoding** to categorical application types while carefully removing baseline categories to avoid the **Dummy Variable Trap**.
- **Data Integrity:** Dropped redundant features and potential "Data Leaks" (like `Allocated_Bandwidth`) to ensure the model learns generalized patterns rather than memorizing direct outputs.

## Exploratory Data Analysis (EDA)
Key insights derived from the cleaned data:
- **Correlation Insights:** Confirmed a strong positive correlation (0.61) between `VoIP_Call` and resource allocation, reflecting the high priority of real-time voice traffic.
- **Latency Impact:** Scatter plots revealed a clear downward trend in allocation as latency exceeds 0.08s, demonstrating the network's QoS-driven "penalty" for high-delay links.
- **App-Type Distribution:** Box plots highlighted that high-priority apps (VoIP, Streaming) maintain narrow, high-allocation bands, while IoT traffic exhibits wider, lower-priority variance.

## Features & Target
- **Input Features:**
  - `Signal_Strength (dBm)`
  - `Latency (s)`
  - `Required_Bandwidth (Mbps)`
  - `Application_Type` (One-Hot Encoded: VoIP, Streaming, Gaming, IoT, etc.)
- **Target Variable:**
  - `Resource_Allocation`: A ratio (0.0 to 1.0) representing the percentage of allocated resources.

## Project Status
- [x] Data Cleaning & Unit Normalization
- [x] Feature Engineering & Encoding
- [x] Exploratory Data Analysis (EDA) & Visualization
- [ ] Train/Test Data Splitting
- [ ] Model Training (Baseline vs. Optimized)
- [ ] Performance Evaluation (R-squared, MSE)

## Tech Stack
- **Language:** Python
- **Environment:** Google Colab
- **Libraries:** Pandas, NumPy, Scikit-Learn, Matplotlib, Seaborn
