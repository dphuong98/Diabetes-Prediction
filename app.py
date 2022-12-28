import numpy as np
import pickle
# from waitress import serve
from flask import Flask, request, render_template

# Load NB model
model = pickle.load(open('model.pkl', 'rb')) 

# Create application
app = Flask(__name__)

# Bind home function to URL
@app.route('/')
def home():
    return render_template('diabetes_classifier.html')

# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def predict():
    
    # Put all form entries values in a list 
    features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(features)]
    print(array_features)
    # Predict features
    prediction = model.predict(array_features)
    # prediction = model.predict([[ 4.,  0.,  3.,  3.,  0.,  1.,  0., 10.,  1.,  1.,  1.,  1.,  1., 1.,  1.,  1.,  0.,  4.,  2.,  2.,  1.]])
    output = prediction

    print(output)
    
    # Check the output values and retrive the result with html tag based on the value
    if output == 0:
        return render_template('diabetes_classifier.html', 
                               result = 'No diabetes')
    else:
        return render_template('diabetes_classifier.html', 
                               result = 'Diabetes')

if __name__ == '__main__':
#Run the application
    # serve(app, host="127.0.0.1", port=8080)
    app.run(debug=True)