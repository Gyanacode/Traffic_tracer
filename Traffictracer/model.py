import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load the vehicle data
vehicle_data = pd.read_csv('vehicle_data.csv')

# Data preprocessing
label_encoder = LabelEncoder()
vehicle_data['RoadType'] = label_encoder.fit_transform(vehicle_data['RoadType'])
X = vehicle_data[['Latitude', 'Longitude', 'Speed']]
y = vehicle_data['RoadType']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy * 100:.2f}%')
