from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import pandas as pd

# 1. Load and preprocess the dataset
df = pd.read_csv("mbti_1.csv")  

# Separate the data into X and y
X = df["posts"].tolist()  # Text samples
y = df["type"].tolist()   # MBTI types

# Example usage
#print("X (text samples):")
#print(X[:5]) 
#print("\ny (MBTI types):")
#print(y[:5])  

# 2. Feature extraction
vectorizer = TfidfVectorizer(max_features=1000)  
X_tfidf = vectorizer.fit_transform(X)

# 3. Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

# 4. Train the model
model = LogisticRegression(max_iter=1000) 
model.fit(X_train, y_train)

# 5. Evaluate the model
y_pred = model.predict(X_test)
#print(classification_report(y_test, y_pred))

# 6. Use the trained model for prediction
def predict_personality(text):
    text_tfidf = vectorizer.transform([text])
    personality_type = model.predict(text_tfidf)
    return personality_type[0]

# Example usage
#user_input = input("Enter text to predict personality type: ")
#predicted_type = predict_personality(user_input)
#print("Predicted personality type:", predicted_type)
