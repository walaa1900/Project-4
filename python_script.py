import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load the data
file_path = '../csvs_files/cleaning_data.csv'
data = pd.read_csv(file_path)


# Preprocessing categorical columns
label_encoder = LabelEncoder()
data['gender'] = label_encoder.fit_transform(data['gender'])  # Encode binary column

# Perform one-hot encoding for other categorical columns
categorical_columns = ['ever_married', 'work_type', 'Residence_type', 'smoking_status']
data = pd.get_dummies(data, columns=categorical_columns)

# Preprocessing numerical columns (normalize)
scaler = StandardScaler()
numerical_columns = ['age', 'avg_glucose_level', 'bmi']
data[numerical_columns] = scaler.fit_transform(data[numerical_columns])

# Separating input features (X) and target variable (y)
X = data.drop(columns=['stroke'])
y = data['stroke']

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the neural network model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.1)
