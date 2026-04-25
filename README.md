# 5G Resource Allocation & QoS Prediction

A Machine Learning project to optimize 5G network resource distribution based on application requirements and signal quality.

## Preprocessing Highlights
- **Feature Cleaning:** Removed non-predictive columns (Timestamp, User_ID).
- **Unit Normalization:** Converted all data units to standard formats (seconds for latency, Mbps for bandwidth).
- **Encoding:** Applied One-Hot Encoding to `Application_Type`.
- **Statistical Handling:** Prevented the "Dummy Variable Trap" by removing the baseline category.

## Dataset Features
- **Inputs:** Signal Strength (dBm), Latency (s), Required Bandwidth (Mbps), Application Type.
- **Goal:** Predict optimal Resource Allocation and Allocated Bandwidth.

## Status
- [x] Data Cleaning & Preprocessing
- [ ] Train/Test Split
- [ ] Model Training & Evaluation
