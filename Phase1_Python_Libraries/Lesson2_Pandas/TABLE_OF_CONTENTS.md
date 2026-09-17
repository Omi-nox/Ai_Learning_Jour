# Pandas Exercises - Table of Contents

## 📌 Quick Navigation Guide
This document provides an organized overview of all topics and exercises covered in the `excercises.ipynb` notebook.

---

## 📚 Topics Covered

### **CONCEPT 1: The Two Core Structures**
- **Series** — 1D labeled array
  - Creating Series with `pd.Series()`
  - Understanding index and values
  - Data types (dtype)
  
- **DataFrame** — 2D labeled table
  - Creating DataFrames from dictionaries
  - `df.shape` — dimensions (rows × columns)
  - `df.dtypes` — column data types
  - `df.head(n)` — view first n rows
  - `df.tail(n)` — view last n rows
  - `df.info()` — comprehensive data info
  - `df.describe()` — statistical summary

**Code Cell:** Line 1-3 (Series example), Lines 4-6 (DataFrame example with product data)

---

### **CONCEPT 2: Selecting and Accessing Data**
- **Single Column Selection**
  - `df['Name']` → returns Series
  
- **Multiple Column Selection**
  - `df[['Name', 'Score']]` → returns DataFrame
  
- **Row Selection Methods**
  - `iloc[]` — numeric indexing (like NumPy)
  - `loc[]` — label-based indexing
  - Key difference: `iloc` excludes end, `loc` includes end
  
- **Combined Selection**
  - `iloc[0:2, 1:3]` — rows by position, columns by position
  - `loc[0:2, ['Name', 'Score']]` — rows by label, columns by name
  
- **Single Value Access**
  - `df.iloc[row, col]` — numeric indices
  - `df.loc[row, 'Column']` — label indices

**Practice Set 1:** Student grades data (lines with "Umar", "Ali", "Sara")
- Extract single column (Math scores)
- Extract multiple columns (Student, English)
- View first 3 rows with `iloc`
- View rows 1-3 with `loc`
- Access specific value (Sara's Science score)

**Practice Set 2:** Football players data (Ronaldo, Messi, Neymar, Mbappe, Salah)
- Extract Goals column as Series
- Extract multiple columns (Goals, Rating, Player)
- View last two rows
- View rows 1-3 with `loc`
- Access Neymar's rating using `iloc`
- Access Mbappe's assists using `loc`
- View rows 0-2 with specific columns
- View rows 2-4 with first three columns
- Access last player's rating

---

### **CONCEPT 3: Filtering Data**
- **Boolean Masking** — filter rows based on conditions
  - `df['Goals'] > 22` → creates boolean Series
  - `df[df['Goals'] > 22]` → keeps only True rows
  
- **Combining Conditions**
  - `&` — AND (both conditions true)
  - `|` — OR (either condition true)
  - Each condition must be wrapped in `( )`
  
- **The `.isin()` Method**
  - `df['Grade'].isin(['A', 'B'])` → checks if value in list
  - Cleaner than multiple OR conditions

**Practice Set Example:** Student grades data (Umar, Ali, Sara, John, Ayesha, Bilal)
- Students with Math > 70
- Students with Math > 70 AND Science > 75
- Students with Grade in ['A', 'B']
- Students who failed (Math < 50)
- Students with Math > 60 (select Student and Grade columns)

---

### **CONCEPT 4: Adding, Updating & Deleting Columns**
- **Adding New Columns**
  - `df['NewCol'] = expression` → element-wise operations
  - `df['Total'] = df['Math'] + df['Science']`
  - `df['Bonus'] = 5000` → fixed value for all rows
  - `df['Result'] = condition` → boolean column
  
- **Mapping Values**
  - `df['Result'].map({True: 'Pass', False: 'Fail'})`
  
- **Updating Existing Columns**
  - `df['Math'] = df['Math'] + 5` → modify all values
  - `df.loc[condition, 'Column'] = new_value` → conditional update
  - `df.loc[3, 'Student'] = 'John Wick'` → update specific cell
  
- **Deleting Columns**
  - `df.drop('ColumnName', axis=1, inplace=True)`
  - `inplace=True` modifies original; False requires reassignment
  
- **Renaming Columns**
  - `df.rename(columns={'OldName': 'NewName'}, inplace=True)`
  
- **Adding Rows**
  - `df.loc[new_index] = [value1, value2, ...]`
  - `pd.concat([df, new_df], ignore_index=True)` — combine DataFrames

**Practice Set Exercise:** Football players data (Ronaldo, Messi, Neymar, Mbappe)
- Task 1: Add `Contributions` column (Goals + Assists)
- Task 2: Add `Bonus` column with fixed value 5000
- Task 3: Add `Star_Player` column (True if Goals > 20)
- Task 4: Update Neymar's Goals to 25
- Task 5: Delete the `Bonus` column
- Task 6: Rename `Goals` → `Total_Goals` and `Assists` → `Total_Assists`

---

### **CONCEPT 5: Handling Missing Data**
- **Detecting Missing Values**
  - `None` → Python's representation
  - Pandas converts to `NaN` (Not a Number)
  - `df.isnull()` → boolean DataFrame (True = missing)
  - `df.isnull().sum()` → count missing per column ⭐ **Most used**
  
- **Row-wise Missing Data Checks**
  - `df.isnull().sum(axis=1)` — missing count per row
  - `df[df.isnull().any(axis=1)]` — rows with ANY missing value
  - `df[df.isnull().any(axis=1)].index.tolist()` — get row indices with NaN
  - `df[df.isnull().any(axis=1)]['ColumnName'].tolist()` — get specific column values from rows with NaN
  
- **Column-wise Missing Data Checks**
  - `df.columns[df.isnull().any()].tolist()` — list column names with missing values
  
- **Dropping Missing Values**
  - `df.dropna()` → remove all rows with ANY missing value
  - `df.dropna(subset=['Math'])` → remove only if Math is missing
  - Must reassign: `df = df.dropna()`
  
- **Filling Missing Values**
  - `df.fillna(0)` → replace NaN with 0
  - `df['Math'].fillna(df['Math'].mean())` → fill with column mean ⭐ **Most common for ML**
  - `df['Grade'].fillna('Unknown')` → fill text columns with label
### Concept 6 - Group by col, mean ad aggregassion
```
print(df.groupby('Cluster')[['Income','Spending_Score']].mean())
```
**Practice Set Example:** Student data with missing values (Umar, Ali, Sara, John, Ayesha)
- Detect missing values with `isnull()`
- Count missing per column
- Drop rows with missing values
- Identify which rows have NaN
- Get indices of rows with NaN
- Get column names with NaN
- Drop specific column with missing values
- Fill NaN with 0
- Fill Math column with mean
- Fill Grade column with 'Unknown'

---

### **BONUS CONCEPT: Finding Exact Location of NaN**
- **Using `np.where()`** — locate missing values precisely
  - `np.where(condition)` → returns tuple of indices
  - For 1D arrays: `(array([indices]),)`
  - For 2D arrays: `(array([row_indices]), array([col_indices]))`
  - Can zip results for pairs: `zip(row_indices, col_indices)`

**Example Code:** Locate NaN in DataFrame with ID, Name, Age columns

---

## 📊 Quick Function Reference

| Function | Purpose | Example |
|----------|---------|---------|
| `pd.Series()` | Create 1D labeled array | `pd.Series([10, 20, 30])` |
| `pd.DataFrame()` | Create 2D table | `pd.DataFrame(dict_data)` |
| `df.shape` | Get dimensions | Returns `(rows, columns)` |
| `df.head(n)` | View first n rows | `df.head(3)` |
| `df.tail(n)` | View last n rows | `df.tail(2)` |
| `df.info()` | Data overview | Shows dtypes, null counts, memory |
| `df.describe()` | Statistical summary | Shows mean, std, min, max, etc. |
| `df['Col']` | Select one column | Returns Series |
| `df[['C1', 'C2']]` | Select multiple columns | Returns DataFrame |
| `df.iloc[i, j]` | Numeric indexing | Row i, column j by position |
| `df.loc[i, 'Col']` | Label indexing | Row i by label, column by name |
| `df[df['Col'] > val]` | Filter rows | Boolean masking |
| `df.isnull()` | Detect NaN | Returns boolean DataFrame |
| `df.dropna()` | Remove missing rows | Returns new DataFrame |
| `df.fillna(val)` | Fill missing values | Returns new DataFrame |
| `df.rename()` | Rename columns | Updates column names |
| `df.drop()` | Delete columns | Use `axis=1` for columns |

---

## 🎯 Learning Path

**Start Here:**
1. ✅ Concept 1 — Understand Series and DataFrame basics
2. ✅ Concept 2 — Learn to access and select data
3. ✅ Concept 3 — Filter data with conditions
4. ✅ Concept 4 — Modify DataFrames (add/update/delete)
5. ✅ Concept 5 — Handle missing data
6. ✅ Bonus — Find exact NaN locations

**Practice Order:**
- Practice Set 1 (Student grades) → Basic selection
- Practice Set 2 (Football players) → Advanced selection
- Filtering Exercise (Student data) → Boolean masking
- Modification Exercise (Players data) → CRUD operations
- Missing Data Exercise (Student data) → Data cleaning

---

## 💡 Key Takeaways

- **Series** = 1D column, **DataFrame** = 2D table with column names
- Use `iloc[]` for positions (0, 1, 2...), `loc[]` for labels
- **Boolean masking** is the most powerful filtering technique
- **`df.isnull().sum()`** is your first tool for data quality checks
- **Fill with mean** for numbers, **fill with 'Unknown'** for text
- Always use `inplace=True` or reassign when modifying DataFrames

---

## 📂 File Structure
```
Phase1_Python_Libraries/Lesson2_Pandas/
├── excercises.ipynb          ← Main notebook with all code
├── TABLE_OF_CONTENTS.md      ← This file (navigation guide)
└── [Add other resource files here]
```

---

**Last Updated:** 2026-09-16  
**Status:** ✅ All 5 Concepts + Bonus covered with exercises
