# 🎓 Logistic Regression Model for Student Pass/Fail Prediction

## 📝 Overview
This Jupyter Notebook demonstrates the implementation of a Logistic Regression model to predict whether a student will pass or fail based on their study hours. It covers the entire machine learning pipeline from data preparation and model training to evaluation and prediction.

> 💡 **Note:** The complete mathematical formulas and underlying concepts are thoroughly explained inside the Jupyter Notebook.

---

## 🧠 Key Concepts Covered
* **Logistic Regression:** Understanding its application as a classification algorithm, despite its name.
* **Sigmoid Function:** Visualizing how the sigmoid function squishes outputs between 0 and 1, representing probabilities.
* **Model Training:** Splitting data into training and testing sets, and fitting a `LogisticRegression` model.
* **Model Evaluation:** Using `accuracy_score` and `classification_report` to assess model performance.
* **Prediction:** Making predictions (pass/fail) and obtaining probability scores for new data points.

---

## 📊 Dataset
The dataset used is a simple synthetic one, containing two columns:
* `StudyHours`: The number of hours a student studied (Feature $X$).
* `Passed`: A binary variable indicating whether the student passed (1) or failed (0) (Target $y$).

---

## 🗂️ Notebook Structure
The notebook includes the following sections sequentially:

1. **Data Loading and Preparation:** Defining the dataset and creating a pandas DataFrame.
2. **Feature and Label Definition:** Separating `StudyHours` as the feature ($X$) and `Passed` as the label ($y$).
3. **Data Splitting:** Dividing the dataset into training and testing sets using `train_test_split`.
4. **Model Training:** Initializing and training a `LogisticRegression` model.
5. **Model Testing and Prediction:** Generating predictions (`y_pred`) and probabilities (`y_prob`) on the test set.
6. **Model Evaluation:** Displaying actual vs. predicted values, accuracy, and a detailed `classification_report`.
7. **Mapping Predictions:** Converting numerical predictions (0/1) to 'Fail'/'Pass' for better readability.
8. **Sigmoid Curve Visualization:** Plotting the sigmoid function to illustrate the decision boundary.
9. **New Data Prediction:** Demonstrating how to predict the outcome for a student with a new study hour value (e.g., 3.5 hours).

---

## ⚙️ Dependencies
The following Python libraries are required to run this notebook:
* `numpy`
* `pandas`
* `matplotlib`
* `scikit-learn`
* `scipy`

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Execution Setup
* **Google Colab:** Upload the `.ipynb` file to Google Colab, or open it directly from Google Drive.
* **Dependencies:** Pre-installed on Colab. If running locally, install missing ones via:
  ```bash
  pip install numpy pandas matplotlib scikit-learn scipy
  ```

### 3. Run Cells
Execute the cells sequentially from top to bottom to see the model training and output visualization in action.

---

## 🏋️ Exercises Included
The notebook contains a **Practice Set** section with the following hands-on exercises:
* Building a complete Logistic Regression model and printing actual vs. predicted values.
* Printing probability scores and identifying the student with the highest pass probability.
* Analyzing the classification report and overall accuracy.
* Plotting the sigmoid curve with customized titles and labels.
* Predicting outcomes for raw custom study hours.
* Discussing **why accuracy might not always be the best metric** for imbalanced classification tasks.
