# Students Performance Analysis

## Overview
This project aims to analyze the impact of various factors such as gender, ethnicity, parental education level, lunch type, and completion of a test preparation course on student performance. The analysis involves exploring how these factors influence students' scores and ultimately, training a model to predict student performance.

## Objective
The key objective is to understand:
- The role of gender in academic performance.
- The influence of parental education on student scores.
- The impact of ethnicity on academic achievements.
- The benefits of completing a test preparation course.
- How the type of lunch affects student performance.

## Dataset
The dataset used in this project, `StudentsPerformance.csv`, includes the following columns:
- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch
- Test Preparation Course
- Math Score
- Reading Score
- Writing Score

## Installation
To run this analysis, you need Python and the following libraries:
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

You can install these packages via pip:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```
## Usage
To perform the analysis, follow these steps:

1. Clone the repository:
    ```bash
    git clone [repository-url]
    ```

2. Navigate to the cloned repository:
    ```bash
    cd [repository-name]
    ```

3. Run the Jupyter notebook:
    ```bash
    jupyter notebook Analyzing_StudentPerformance.ipynb
    ```

## Analysis Steps

### Data Loading and Initial Exploration
- Read the dataset.
- Display basic information and statistics.

### Data Cleaning
- Check and handle missing values.

### Data Visualization
- Use bar plots, pie charts, and box plots to visualize the data.

### Feature Engineering
- Create a `Total Score` and a `Pass/Fail` status based on scores.

### Predictive Modeling
- Encode categorical variables.
- Split the data into training and testing sets.
- Train a `RandomForestRegressor` model.
- Evaluate the model using MAE and R² metrics.

## Results
The analysis reveals trends and correlations between students' demographic characteristics, academic performance, and likelihood of passing or failing based on total score. Insights from the analysis could be valuable for educational strategies and interventions.
