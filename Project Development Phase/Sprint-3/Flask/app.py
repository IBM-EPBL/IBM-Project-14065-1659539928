from flask import Flask, render_template, url_for, request,redirect
import numpy as np
import pandas as pd
import joblib

filename = 'model.pkl'
pipe = joblib.load(filename)

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != 'admin@gmail.com' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        elif request.form['email'] == '' or request.form['password'] == '':
            error='Please fill the form'
        else:
            return redirect(url_for('home'))
    return render_template('home.html', error=error)

@app.route('/register',methods=['GET','POST'])
def register():
    msg=''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'con_password' in request.form and 'email' in request.form :
        msg = 'You have successfully registered !'
        return redirect(url_for('home'))
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html',msg=msg)


@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/logout')
def logout():
    return render_template('home.html')
@app.route('/predict', methods=['POST'])
def predict():
    arr = []
    
    if request.method == 'POST':
        age = int(request.form['Age'])
        education = int(request.form['Education'])
        education_field = request.form['Education_Field']
        department = request.form['Department']
        distance_from_home = int(request.form['Distance_From_Home'])
        marital_status = request.form['Marital_Status']
        jobrole = request.form['Job_Role']
        monthly_income = int(request.form['Monthly_Income'])//75.20
        gender = request.form['Gender']
        percent_salary_hike = int(request.form['Percent_Salary_Hike'])
        total_working_hours = int(request.form['Total_Working_Hours'])
        total_working_years = int(request.form['Total_Working_Years'])
        years_with_current_manager = int(request.form['Years_With_Current_Manager'])
        training_times_last_year = int(request.form['Training_Times_Last_Year'])
        years_since_last_promotion = int(request.form['Years_Since_Last_Promotion'])
        num_companies_worked = int(request.form['NumCompaniesWorked'])
        years_at_company = int(request.form['YearsAtCompany'])
        job_level = int(request.form['Job_Level'])
        business_travel = request.form['Business_Travel']
        
        arr = [[age, business_travel, department, distance_from_home, education, education_field, gender, job_level, jobrole, marital_status, 
                monthly_income, num_companies_worked, percent_salary_hike, total_working_hours, total_working_years, training_times_last_year, years_at_company, years_since_last_promotion, years_with_current_manager]]
        
        X_test = pd.DataFrame(arr,columns=['Age','BusinessTravel','Department','DistanceFromHome','Education','EducationField','Gender','JobLevel','JobRole','MaritalStatus',
                                           'MonthlyIncome','NumCompaniesWorked','PercentSalaryHike','StandardHours','TotalWorkingYears','TrainingTimesLastYear','YearsAtCompany','YearsSinceLastPromotion','YearsWithCurrManager'])
        pred = pipe.predict(X_test)
        
        if pred == 1:
            pred_text = "It's time to look for new opportunities. According to past data, your job offer is likely to be revoked."
        else:
            pred_text = "Your Job is secure. Good luck for future endeavours!"
    
    return render_template('results.html',pred_text=pred_text)

if __name__ == '__main__':
    app.debug=True
    app.run()
