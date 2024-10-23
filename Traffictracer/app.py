from flask import Flask, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load the model and label encoder
model = None
label_encoder = None

def load_model():
    global model, label_encoder
    # Load the trained model and label encoder from disk (if saved)
    # For simplicity, we will initialize a new model here
    model = RandomForestClassifier()  # Placeholder; replace with actual loading code
    label_encoder = LabelEncoder()  # Placeholder; replace with actual loading code

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_data = [[data['Latitude'], data['Longitude'], data['Speed']]]
    prediction = model.predict(input_data)
    predicted_road_type = label_encoder.inverse_transform(prediction)
    return jsonify({'Predicted Road Type': predicted_road_type[0]})

if __name__ == '__main__':
    load_model()
    app.run(debug=True)