from flask import Flask, render_template, request
import joblib
from preprocess import preprocessing

app = Flask(__name__)
model = joblib.load('models/randomforest_model.pkl')

@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        sepal_length = request.form.get('sepal_length')
        sepal_width = request.form.get('sepal_width')
        petal_length = request.form.get('petal_length')
        petal_width = request.form.get('petal_width')

        try:
            data = preprocessing(
                sepal_length,
                sepal_width,
                petal_length,
                petal_width
            )

            prediction = model.predict(data)

            return render_template('predict.html', prediction=prediction)

        except ValueError:
            return 'Please Enter valid values'

    else:
        pass

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()