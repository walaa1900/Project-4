import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Replace this with your actual dataset
data = {
    'id': [9046, 51676, 31112, 60182, 1665, 56669, 53882, 10434, 27419, 60491],
    # Include other columns with corresponding values here...
    'stroke': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Preprocessing steps (handling missing values, encoding categorical variables, etc.)
# Replace this with your actual preprocessing steps

# Selecting features and target variable
X = df.drop(columns=['id', 'stroke'])  # Features
y = df['stroke']  # Target

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model (using Logistic Regression as an example)
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(report)
