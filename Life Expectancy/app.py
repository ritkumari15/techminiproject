from flask import Flask,render_template,request
import pickle
import numpy as np

#Load pickel file
filename = 'life_expectancy.pkl'
rfc = pickle.load(open(filename, 'rb'))



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():

    if request.method == 'POST':
        adultmortality = int(request.form['adultmortality'])
        infantdeaths = int(request.form['infantdeaths'])
        Alcohol = float(request.form['Alcohol'])
        HepatitisB = int(request.form['HepatitisB'])
        Measles = int(request.form['Measles'])
        bmi = float(request.form['bmi'])
        underfivedeaths = int(request.form['under-five-deaths'])
        Polio = int(request.form['Polio'])
        Diphtheria = int(request.form['Diphtheria'])
        HIVAIDS = float(request.form['HIV/AIDS'])
        thinnessyears = float(request.form['thinness 1-19 years'])
        icr = float(request.form['icr'])
        Schooling = float(request.form['Schooling'])

        data = np.array([[ adultmortality,infantdeaths,Alcohol,HepatitisB,Measles,
                          bmi,underfivedeaths,Polio,Diphtheria,HIVAIDS,thinnessyears
                          ,icr,Schooling]])


        my_prediction = rfc.predict(data)[0].round(1)

        return render_template('index.html',prediction = my_prediction)

if __name__ == '__main__':
	app.run(debug=True)