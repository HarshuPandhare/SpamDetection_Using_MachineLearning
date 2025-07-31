from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Initialize Flask app
app = Flask(__name__)

# Load dataset (Ensure the file exists at this path)
try:
    dataset_path = 'C:\coding\Harsh\Asep 2\emails.csv'  # Update this to the correct location
    dataset = pd.read_csv(dataset_path)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print(f"Error: Dataset not found at path: {dataset_path}")
    raise

# Train Naive Bayes model
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(dataset['text'])
x_train, x_test, y_train, y_test = train_test_split(x, dataset['spam'], test_size=0.2,random_state=42)
                                                    

model = MultinomialNB()
model.fit(x_train, y_train)

# Test the accuracy
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2f}")


# Define a prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input message from the POST request Using Jasan Body
        data = request.get_json()

        # Check if "message" key exists in the JSON body
        if not data or "message" not in data:
            return jsonify({"error": "Invalid input. Missing 'message' field."}), 400

        message = data["message"]

        # Transform input message using the trained vectorizer
        message_vector = vectorizer.transform([message])

        # Predict using the trained model
        prediction = model.predict(message_vector)[0]
        result = "Spam" if prediction == 1 else "Not Spam"

        # Return JSON response with the prediction result
        return jsonify({
            "message": message,
            "prediction": result
        })

    except Exception as e:
        # Catch and return any internal error
        print(f"Error in prediction: {e}")
        return jsonify({"error": str(e)}), 500


# Run Flask app
if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=8080, debug=True)
