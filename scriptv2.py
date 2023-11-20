import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import joblib
import sys
import json

# Read custom data from command line arguments
try:
    custom_data_str = sys.argv[1]
    custom_data = json.loads(custom_data_str)
except IndexError:
    print("Error: No command-line argument provided.")
    sys.exit(1)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {str(e)}")
    sys.exit(1)
# Load your training data
# Replace 'your_training_data.csv' with the actual path to your training data
training_data = pd.read_csv('/home/kasagg21/Downloads/archive (2)/StudentsPerformance.csv')

# Calculate the 'Total Score' and create a new column
training_data['Total Score'] = training_data['math score'] + training_data['reading score'] + training_data['writing score']

# Criterion for getting a passing grade
def result(TS, MS, WS, RS):
    if (TS > 150 and MS > 40 and WS > 40 and RS > 40):
        return '1'
    else:
        return '0'

# Create a new column 'Pass/Fail' based on the 'Total Score', 'math score', 'writing score', and 'reading score'
training_data['Pass/Fail'] = training_data.apply(lambda x: result(x['Total Score'], x['math score'], x['writing score'], x['reading score']), axis=1)

# Load your RandomForestRegressor model with the training data
OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
X_category = training_data[['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']]
X_OH = pd.DataFrame(OH_encoder.fit_transform(X_category))
X_OH.index = X_category.index

model = RandomForestRegressor()
X_train = X_OH  # Replace with your training features
y_train = training_data['Pass/Fail']  # Replace with your target variable
model.fit(X_train, y_train)

# Save the fitted model to a file
joblib.dump(model, 'trained_model_v3.joblib')

def preprocess_custom_data(custom_data):
    # Convert custom input data dictionary to a Pandas DataFrame
    custom_data_df = pd.DataFrame([custom_data])
    custom_data_df = custom_data_df[['gender', 'race/ethnicity', 'parental level of education', 'lunch', 'test preparation course']]

    # Apply one-hot encoding using the fitted encoder
    custom_data_encoded = pd.DataFrame(OH_encoder.transform(custom_data_df))
    custom_data_encoded.index = custom_data_df.index

    return custom_data_encoded

if __name__ == '__main__':
    try:
        # Preprocess the custom input data
        preprocessed_data = preprocess_custom_data(custom_data)

        # Use the loaded model to make predictions
        loaded_model = joblib.load('trained_model_v3.joblib')
        predictions = loaded_model.predict(preprocessed_data)

        # Determine pass/fail based on a threshold value
        pass_fail_prediction = 'P' if predictions[0] >= 0.66 else 'F'

        # Send the prediction back to the Express.js server
        print(json.dumps({'prediction': pass_fail_prediction}))

    except Exception as e:
        print(f"Error during script execution: {str(e)}")
        sys.exit(1)