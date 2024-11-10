# Students Performance Analysis

## Overview
This project analyzes the impact of various factors such as gender, ethnicity, parental education level, lunch type, and completion of a test preparation course on students' academic performance. It explores how these factors affect scores and develops a predictive model for student performance. Additionally, a web interface allows users to predict student outcomes based on input parameters.

## Objective
To understand how:
- Gender influences academic performance.
- Parental education impacts student scores.
- Ethnicity affects academic achievements.
- Completion of a test preparation course benefits students.
- The type of lunch consumed influences performance.

## Dataset
The dataset, `StudentsPerformance.csv`, contains several attributes, including:
- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch
- Test Preparation Course
- Math Score
- Reading Score
- Writing Score

## Installation
Requirements:
- Python
- Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn

Install the required Python libraries using pip:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```
## Usage
To perform the analysis and use the web application, follow these steps:

1. Clone the repository:
    ```bash
    git clone [[repository-url]](https://github.com/KasAgg21/predicting-student-pass-fail.git)
    ```

2. Navigate to the repository directory:
    ```bash
    cd predicting-student-pass-fail
    ```

3. Run the Jupyter notebook:
    ```bash
    jupyter notebook Analyzing_StudentPerformance.ipynb
    ```

4. Start the web application:
    ```bash
    node server.js
    ```

## Web Application
The web application allows users to input student details and receive a Pass/Fail prediction. It is built using HTML, CSS (Bootstrap), and JavaScript, with a Node.js backend handling API requests.

### HTML Form
Users input data via a form, which includes selections for gender, ethnicity, parental education, lunch type, and test preparation course status.

### Backend API
A Node.js server receives form data and processes it using a trained machine learning model to return predictions.

## Analysis Steps

1. **Data Loading and Initial Exploration**: Load the dataset and perform initial exploration.
2. **Data Cleaning**: Check for and handle missing values.
3. **Data Visualization**: Visualize the data using various charts.
4. **Feature Engineering**: Create 'Total Score' and 'Pass/Fail' status based on scores.
5. **Predictive Modeling**: Encode categorical variables, split the data, train a `RandomForestRegressor` model, and evaluate it.

## Results
The analysis reveals how demographic characteristics and educational factors correlate with academic performance, providing insights that could inform educational strategies.
