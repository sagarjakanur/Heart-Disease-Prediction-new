import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load dataset
df = pd.read_csv("heart_cleveland_upload.csv")

# Features and target
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Overwrite old model file
pickle.dump(model, open("heart-disease-prediction-knn-model.pkl", "wb"))

print("New model saved successfully!")