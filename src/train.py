import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
import joblib

# Load dataset
df = pd.read_csv("data/Original_Dataset.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Combine all symptom columns into one text
symptom_cols = [col for col in df.columns if col != "Disease"]

df["combined"] = df[symptom_cols].fillna("").apply(
    lambda row: " ".join(row.values.astype(str)), axis=1
)

# Features & target
X = df["combined"]
y = df["Disease"]

# Vectorize text
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model/health_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("✅ Model trained successfully")

