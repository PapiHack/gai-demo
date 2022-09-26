import numpy as np
from flask import Flask, request, render_template, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    int_feature = [int(x) for x in request.form.values()]
    final_feature = [np.array(int_feature)]
    prediction = model.predict(final_feature)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Enploye salary sould be $ {}'.format(output))

@app.route('/api/predict', methods=['POST'])
def api_predict():

    data = request.get_json(force=True)

    prediction = model.predict([np.array([int(data['experience']), int(data['test_score']), int(data['interview_score'])])])

    output = round(prediction[0], 2)

    return jsonify({'salary': output, 'currency': '$'})


if __name__== '__main__':
    app.run(host="0.0.0.0", debug=True)

