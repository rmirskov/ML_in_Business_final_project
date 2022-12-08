import dill
import pickle
import pandas as pd
from flask import Flask, render_template, request
from forms import DataForm
from flask_wtf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
	))

model = None
best_threshold = None

def load_model(model_path, best_threshold_path=None):
	# load the pre-trained model
	global model
	with open(model_path, 'rb') as f:
		model = dill.load(f)
	
	if best_threshold_path:
		global best_threshold
		with open(best_threshold_path, 'rb') as f:
			best_threshold = pickle.load(f)


@app.route("/", methods=["GET"])
def general():
	return render_template('start.html', title='Start Page')

@app.route("/send", methods=["GET"])
def start():
	form = DataForm()
	return render_template('form.html', form=form, title='Input Data Page')

@app.route("/predict", methods=["GET", "POST"])
def predict():
	if request.method == "POST":
		result = request.form
		predict_dict = {}

		data = pd.DataFrame({
			'age': result['age'], 'workclass': result['workclass'],'education': result['education'],
			'education-num': result['education_num'], 'marital-status': result['marital_status'],
			'occupation': result['occupation'], 'relationship': result['relationship'],
			'race': result['race'], 'sex': result['sex'], 'capital-gain': result['capital_gain'],
			'capital-loss': result['capital_loss'], 'hours-per-week': result['hours_per_week'],
			'native-country': result['native_country'],
			}, index=[0])

		probability = model.predict_proba(data)[:, 1][0]
		predict_dict['probability'] = round(probability, 3)
		if best_threshold:
			predict_dict['class'] = '>50K' if probability > best_threshold else '<=50K'
		else:
			predict_dict['class'] = '>50K' if model.predict(data)[0] else '<=50K'
	
	return render_template('predict.html', result=result, predict=predict_dict, title='Predict Page')


if __name__ == "__main__":
	modelpath = "app/models/model.dill"
	best_threshold_path = "app/models/best_threshold.pickle"
	load_model(modelpath, best_threshold_path=best_threshold_path)
	app.run(host='0.0.0.0')
