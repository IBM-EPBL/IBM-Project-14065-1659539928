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
    dailyrate = float(request.form['dailyrate'])
    distancefromhome = float(request.form['distancefromhome'])
    education = int(request.form['education'])
    environmentsatisfaction = int(request.form['environmentsatisfaction'])
    hourlyrate = float(request.form['hourlyrate'])
    jobinvolvement = int(request.form['jobinvolvement'])
    joblevel = int(request.form['joblevel'])
    jobsatisfaction = int(request.form['jobsatisfaction'])
    monthlyincome = float(request.form['monthlyincome'])
    monthlyrate = float(request.form['monthlyrate'])
    numcompaniesworked = int(request.form['numcompaniesworked'])
    over18 = int(request.form['over18'])
    overtime = int(request.form['overtime'])
    percentsalaryhike = float(request.form['percentsalaryhike'])
    performancerating = int(request.form['performancerating'])
    relationshipsatisfaction = int(request.form['relationshipsatisfaction'])
    stockoptionlevel = int(request.form['stockoptionlevel'])
    totalworkingyears = float(request.form['totalworkingyears'])
    trainingtimeslastyear = int(request.form['trainingtimeslastyear'])
    worklifebalance = int(request.form['worklifebalance'])
    yearsatcompany = float(request.form['yearsatcompany'])
    yearsincurrentrole = float(request.form['yearsincurrentrole'])
    yearssincelastpromotion = float(request.form['yearssincelastpromotion'])
    yearswithcurrmanager = float(request.form['yearswithcurrmanager'])
    travel = request.form['travel']
    dept = request.form['dept']
    edu = request.form['edu']
    gender = request.form['gender']
    jobrole = request.form['jobrole']
    maritalstatus = request.form['maritalstatus']

    response = jsonify({'Attrition' : utilhr.get_attrition(age,dailyrate,distancefromhome,education,environmentsatisfaction,hourlyrate,jobinvolvement,joblevel,jobsatisfaction,monthlyincome,monthlyrate,numcompaniesworked,over18,overtime,percentsalaryhike,performancerating,relationshipsatisfaction,stockoptionlevel,totalworkingyears,trainingtimeslastyear,worklifebalance,yearsatcompany,yearsincurrentrole,yearssincelastpromotion,yearswithcurrmanager,travel,dept,edu,gender,jobrole,maritalstatus)})
    print(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("start")
    utilhr.loading()
    app.run()