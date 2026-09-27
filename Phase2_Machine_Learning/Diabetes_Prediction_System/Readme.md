#  End-to-End Diabetes Prediction System

An end-to-end Machine Learning pipeline built using **Python** and **Scikit-Learn** to assess diabetes risk based on medical health metrics (Pima Indians Diabetes Dataset). 

The project covers data pre-processing, hidden missing-value imputation, feature scaling, model benchmarking, hyperparameter tuning with `GridSearchCV`, and inference automation.

---

##  Project Overview & Key Features

- **Data Preprocessing & Cleaning:** Identified hidden missing values (zeroes in medical metrics like Glucose, BMI, Insulin, Blood Pressure) and handled them using **Median Imputation**.
- **Feature Scaling:** Applied `StandardScaler` to ensure normalized feature representations across all continuous variables.
- **Model Comparison:** Benchmarked multiple baseline classifiers — **Logistic Regression**, **Decision Tree**, and **Random Forest**.
- **Optimization:** Fine-tuned the Random Forest Classifier using 5-Fold Cross-Validation and `GridSearchCV` to maximize prediction accuracy and medical recall.
- **Model Persistence:** Serialized the trained model and feature scaler using `joblib` for seamless inference deployment.
- **Inference Pipeline:** Built a dedicated `predict_diabetes()` function to process raw patient parameters and return probability-backed predictions.

---

##  Tech Stack & Dependencies

- **Language:** Python 3.x
- **Libraries:** `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `joblib`

---

##  Workflow & Methodology

1. **Exploratory Data Analysis (EDA):** Feature distribution and outcome correlation analysis.
2. **Preprocessing:**
   - Zero-value identification in medically non-zero columns.
   - `SimpleImputer(strategy='median')` for robust imputation.
   - `StandardScaler` fitted exclusively on training data to prevent data leakage.
3. **Model Evaluation Summary:**
   - **Logistic Regression:** Stable base accuracy (~78% CV mean).
   - **Decision Tree:** Overfitted with lower generalization capability (~68% CV mean).
   - **Random Forest Classifier (Selected):** Outperformed baselines in catching positive diabetic cases (higher Recall) with robust overall accuracy (~74%-77%).

---
## testing model
to check model system and dont want to check the notebook then just load both models files in python script file and run with predict funtion with new data values to see the output result

