# Table of Contents — Matplotlib Exercises Notebook

**File:** `Phase1_Python_Libraries/Lesson3_Matplotlib/exercises.ipynb`  
**Main focus:** Creating, styling, comparing, and customizing visualizations with Matplotlib, NumPy, and Pandas.

---

## 1. Matplotlib Introduction and Basic Line Plots

### Topics covered

- Importing Matplotlib:

  `import matplotlib.pyplot as plt`

- Creating a simple line plot with:

  - `plt.plot()`
  - `plt.title()`
  - `plt.xlabel()`
  - `plt.ylabel()`
  - `plt.show()`

- Styling plots with:

  - `color`
  - `linewidth`
  - `linestyle`
  - `marker`

- Adding multiple lines to one graph

- Adding labels and legends:

  - `label=`
  - `plt.legend()`

- Adding grid lines:

  - `plt.grid(True)`

### Examples included

- Simple line plot using `x` and `y` values
- Student Mathematics and Science marks plotted together

### Practice exercises

1. Plot monthly sales.
2. Style the sales line with:
   - Green color
   - Dashed line
   - Triangle markers
3. Add an expenses line.
4. Add labels, title, legend, and grid.

### Main functions

| Function | Purpose |
|---|---|
| `plt.plot()` | Creates a line plot |
| `plt.title()` | Adds a chart title |
| `plt.xlabel()` | Labels the x-axis |
| `plt.ylabel()` | Labels the y-axis |
| `plt.legend()` | Displays line labels |
| `plt.grid()` | Adds grid lines |
| `plt.show()` | Displays the chart |

---

## 2. Bar Charts and Histograms

### Topics covered

- Vertical bar charts
- Horizontal bar charts
- Histograms
- Comparing categories
- Understanding data distribution
- Using bins in histograms
- Adding bar borders with `edgecolor`

### Examples included

- Revenue comparison between cities:
  - Karachi
  - Lahore
  - Islamabad
  - Peshawar

- Age distribution using a histogram

### Practice exercises

1. Create a vertical bar chart of revenue per city.
2. Create a horizontal bar chart using the same data.
3. Create a histogram of ages using `bins=4`.
4. Identify the age range containing the most people.

### Main functions

| Function | Purpose |
|---|---|
| `plt.bar()` | Creates a vertical bar chart |
| `plt.barh()` | Creates a horizontal bar chart |
| `plt.hist()` | Creates a histogram |
| `np.sort()` | Sorts NumPy data |
| `edgecolor=` | Adds borders around histogram bars |
| `bins=` | Controls the number of histogram groups |

---

## 3. Scatter Plots

### Topics covered

- Showing relationships between two numerical variables
- Positive correlation
- Comparing groups using different colors
- Changing point size and marker style

### Examples included

- Study hours versus exam scores
- Karachi Mathematics versus Science scores
- Lahore Mathematics versus Science scores

### Practice exercises

1. Create a scatter plot of study hours and scores.
2. Add:
   - Title
   - X-axis label
   - Y-axis label
   - Grid
3. Compare Math and Science scores for different cities.

### Main functions

| Function | Purpose |
|---|---|
| `plt.scatter()` | Creates a scatter plot |
| `marker=` | Changes the point shape |
| `s=` | Changes the point size |
| `color=` | Changes point color |
| `label=` | Adds a group name |
| `plt.legend()` | Displays group labels |

---

## 4. Subplots

### Topics covered

- Creating multiple charts in one figure
- One-row, two-column layouts
- Two-row, two-column layouts
- Working with the `fig` and `axes` objects
- Using subplot-specific functions
- Adjusting subplot spacing

### 4.1 One-by-two subplot

Creates two charts side by side:

```text
1 row × 2 columns
```

#### Charts included

- Line chart of student scores
- Bar chart of science scores

### 4.2 Two-by-two subplot grid

Creates four charts on one page:

```text
2 rows × 2 columns
```

#### Charts included

- Top-left: Line plot
- Top-right: Bar chart
- Bottom-left: Scatter plot
- Bottom-right: Histogram

### Practice exercises

1. Create a scatter plot of study hours versus scores.
2. Create a `1 × 2` subplot:
   - Left: Line plot
   - Right: Scatter plot
3. Create a `2 × 2` subplot:
   - Top-left: Math bar chart
   - Top-right: Science bar chart
   - Bottom-left: Math versus Science scatter plot
   - Bottom-right: Math histogram

### Main functions

| Function | Purpose |
|---|---|
| `plt.subplots()` | Creates multiple plots |
| `axes[0]` | Accesses the first subplot |
| `axes[0, 0]` | Accesses a subplot in a 2D grid |
| `set_title()` | Adds a subplot title |
| `set_xlabel()` | Adds a subplot x-axis label |
| `set_ylabel()` | Adds a subplot y-axis label |
| `plt.tight_layout()` | Prevents overlapping subplot content |

---

## 5. Plotting with Pandas DataFrames

### Topics covered

- Creating a Pandas DataFrame
- Displaying DataFrame data
- Using descriptive statistics
- Checking DataFrame information
- Plotting directly from a DataFrame
- Plotting multiple columns
- Creating bar charts, line charts, and histograms with Pandas

### DataFrame operations included

| Operation | Purpose |
|---|---|
| `pd.DataFrame()` | Creates a DataFrame |
| `df.describe()` | Shows statistical summary |
| `df.info()` | Shows column types and missing values |
| `df[['Math', 'Science']]` | Selects multiple columns |
| `df.plot()` | Creates a plot from DataFrame data |

### Examples included

- Student Math and Science scores
- Monthly Sales and Expenses
- Histogram of Math and Science scores

### Practice exercises

1. Plot Revenue per City using `df.plot()`.
2. Plot Revenue and Expenses as grouped bars.
3. Plot Revenue, Expenses, and Profit as lines with markers.
4. Create a scatter plot of Expenses versus Profit.

### Pandas plotting styles used

| `kind` value | Chart type |
|---|---|
| `'bar'` | Bar chart |
| `'line'` | Line chart |
| `'scatter'` | Scatter plot |
| `'hist'` | Histogram |

---

## 6. Customizing Plots

### Topics covered

- Creating a specific figure size
- Controlling image resolution
- Changing font sizes
- Making titles bold
- Changing title and label colors
- Customizing tick labels
- Adding annotations
- Highlighting important data points

### Customization functions and arguments

| Function or argument | Purpose |
|---|---|
| `plt.figure()` | Creates a new figure |
| `figsize=(10, 5)` | Controls figure dimensions |
| `dpi=100` | Controls image resolution |
| `fontsize=` | Changes text size |
| `fontweight='bold'` | Makes text bold |
| `color=` | Changes text or plot color |
| `plt.xticks()` | Customizes x-axis tick labels |
| `plt.yticks()` | Customizes y-axis tick labels |
| `plt.annotate()` | Adds text and an arrow to a chart |

### Examples included

- Customized sales report
- Custom title and axis fonts
- Student score bar chart
- Highlighting the highest-scoring student with an annotation

---

## 7. Bar Labels and Rectangle Objects

### Topics covered

- Understanding what `plt.bar()` returns
- Working with bar objects
- Reading the height, position, and width of bars
- Adding values above bars
- Centering text over each bar

### Bar object methods explained

| Method | Purpose |
|---|---|
| `bar.get_height()` | Gets the bar height |
| `bar.get_x()` | Gets the left-side x-position |
| `bar.get_width()` | Gets the bar width |

### Formula for placing labels

```text
X position = bar.get_x() + bar.get_width() / 2
Y position = bar.get_height() + 1
Text       = str(score)
```

### Main function

| Function | Purpose |
|---|---|
| `plt.text()` | Adds text to a chart |
| `ha='center'` | Horizontally centers the text |

---

# Complete Function Reference

## Matplotlib functions

| Function | Use |
|---|---|
| `plt.plot()` | Line plots |
| `plt.bar()` | Vertical bar charts |
| `plt.barh()` | Horizontal bar charts |
| `plt.hist()` | Histograms |
| `plt.scatter()` | Scatter plots |
| `plt.subplots()` | Multiple plots in one figure |
| `plt.figure()` | Creates a figure |
| `plt.title()` | Adds a title |
| `plt.xlabel()` | Labels the x-axis |
| `plt.ylabel()` | Labels the y-axis |
| `plt.grid()` | Adds grid lines |
| `plt.legend()` | Adds a legend |
| `plt.show()` | Displays a plot |
| `plt.tight_layout()` | Adjusts spacing |
| `plt.xticks()` | Customizes x-axis ticks |
| `plt.yticks()` | Customizes y-axis ticks |
| `plt.annotate()` | Adds an annotation and arrow |
| `plt.text()` | Adds text to a chart |

## Pandas functions

| Function | Use |
|---|---|
| `pd.DataFrame()` | Creates a DataFrame |
| `df.plot()` | Creates plots from DataFrame columns |
| `df.describe()` | Displays statistics |
| `df.info()` | Displays DataFrame structure |

## NumPy function

| Function | Use |
|---|---|
| `np.sort()` | Sorts numerical data |

---

# Quick Topic Finder

| If you want to learn... | Go to this section |
|---|---|
| Basic line charts | Section 1 |
| Multiple lines | Section 1 |
| Sales versus expenses | Sections 1 and 5 |
| Vertical bars | Section 2 |
| Horizontal bars | Section 2 |
| Histograms | Section 2 |
| Relationships between variables | Section 3 |
| Study hours versus scores | Section 3 |
| Multiple charts together | Section 4 |
| `1 × 2` subplot layouts | Section 4.1 |
| `2 × 2` subplot layouts | Section 4.2 |
| Plotting from DataFrames | Section 5 |
| Pandas `df.plot()` | Section 5 |
| Figure size and resolution | Section 6 |
| Font and title styling | Section 6 |
| Chart annotations | Section 6 |
| Adding values above bars | Section 7 |
| Working with bar objects | Section 7 |

---

# Overall Learning Progression

```text
1. Basic line plots
2. Line plot styling
3. Bar charts and histograms
4. Scatter plots
5. Subplots
6. Pandas DataFrame plotting
7. Plot customization
8. Bar labels and annotations
```

This notebook progresses from basic Matplotlib syntax to more practical data-visualization techniques used in machine learning and data analysis.