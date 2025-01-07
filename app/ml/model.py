import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle

MODEL_PATH = "app/ml/model.pkl"

def train_model(data_path: str):
    # Load data
    data = pd.read_csv(data_path)
    X = data[["math_score", "reading_score", "writing_score"]]
    y = data["performance"]

    # Encode labels
    le = LabelEncoder()
    y = le.fit_transform(y)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save model
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
    print("Model trained and saved.")

def predict_performance(features: list):
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    prediction = model.predict([features])[0]
    
    # Debugging line to check the raw prediction value (should be 0, 1, or 2)
    print("Predicted raw value:", prediction)
    
    performance_map = {0: "Below Average", 1: "Average", 2: "Above Average"}
    return performance_map[prediction]



'''features = [85.0, 95.0, 90.0]  # Benny's scores
prediction = predict_performance(features)
print(prediction)'''