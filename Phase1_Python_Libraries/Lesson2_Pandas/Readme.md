#  Student Performance & Data Analytics - Mini Project

This repository contains a **Python-based data analysis** project. It demonstrates a complete end-to-end workflow—from handling raw datasets with missing values to generating a final ranked leaderboard using **Pandas** and **NumPy**.

##  Project Overview
The project processes two separate datasets: a main student records table and an extra information table (Grades/Fees). The goal was to clean the data, perform feature engineering, and merge the datasets to provide a meaningful summary of student performance.

##  Key Data Operations
- **Data Exploration:** Used `.info()`, `.shape`, and `.isnull()` to understand the data structure and identify gaps.
- **Data Cleaning (Imputation):** Handled missing values (`NaN`) in Math, Science, and English columns by filling them with the **Mean** value of each subject.
- **Feature Engineering:** 
  - Calculated `Total Marks` and `Average`.
  - Created a `Passed` status column based on a 60% threshold.
  - Implemented **Logic Mapping** to convert Boolean values (True/False) into readable "Pass/Fail" strings.
- **Data Integration:** Performed a **Left Join** (Merge) on the `ID` column to combine academic scores with administrative data (Grades and Fee Status).
- **Advanced Aggregation:** Used `.groupby()` to calculate city-wise average performance for Karachi and Lahore.
- **Ranking System:** Assigned a numerical **Rank** to students based on their average scores in descending order.

##  Tech Stack
- **Python** 🐍
- **Pandas** (Data Manipulation)
- **NumPy** (Mathematical Operations)

##  Final Results
The project concludes with a sorted summary table that highlights:
1. Which students passed and paid their fees.
2. The overall ranking of students from highest to lowest average.
3. A clear picture of missing data handled during the process.


*This project represents my initial steps into the world of Data Science and Analytics and MAchine Learning. I am focused on writing clean, efficient, and logical code.* 
