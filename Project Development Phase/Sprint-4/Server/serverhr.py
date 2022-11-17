from flask import Flask,request,jsonify
import utilhr

app = Flask(__name__)

@app.route('/get_travel_details',methods=['GET'])
def get_travel_details():
    response = jsonify({'travel': utilhr.get_travel_details()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_gender_details',methods=['GET'])
def get_gender_details():
    response = jsonify({'gender': utilhr.get_gender_details()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_education_details',methods=['GET'])
def get_education_details():
    response = jsonify({'education': utilhr.get_education_details()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_dept_details',methods=['GET'])
def get_dept_details():
    response = jsonify({'dept': utilhr.get_dept_details()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_jobrole_details',methods=['GET'])
def get_jobrole_details():
    response = jsonify({'jobrole': utilhr.get_jobrole_details()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_maritalstatus_details',methods=['GET'])
def get_maritalstatus_details():
    response = jsonify({'maritalstatus': utilhr.get_maritalstatus_details()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_attrition',methods=['POST'])
def predict_attrition():

    age = int(request.form['age'])
    distancefromhome = float(request.form['distancefromhome'])
    education = int(request.form['education'])
    joblevel = int(request.form['joblevel'])
    monthlyincome = float(request.form['monthlyincome'])
    numcompaniesworked = int(request.form['numcompaniesworked'])
    over18 = int(request.form['over18'])
    percentsalaryhike = float(request.form['percentsalaryhike'])
    stockoptionlevel = int(request.form['stockoptionlevel'])
    totalworkingyears = float(request.form['totalworkingyears'])
    trainingtimeslastyear = int(request.form['trainingtimeslastyear'])
    yearsatcompany = float(request.form['yearsatcompany'])
    yearssincelastpromotion = float(request.form['yearssincelastpromotion'])
    yearswithcurrmanager = float(request.form['yearswithcurrmanager'])
    travel = request.form['travel']
    dept = request.form['dept']
    edu = request.form['edu']
    gender = request.form['gender']
    jobrole = request.form['jobrole']
    maritalstatus = request.form['maritalstatus']

    response = jsonify({'Attrition' : utilhr.get_attrition(age,distancefromhome,education,joblevel,monthlyincome,numcompaniesworked,over18,percentsalaryhike,stockoptionlevel,totalworkingyears,trainingtimeslastyear,yearsatcompany,yearssincelastpromotion,yearswithcurrmanager,travel,dept,edu,gender,jobrole,maritalstatus)})
    print(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("start")
    utilhr.loading()
    app.run()