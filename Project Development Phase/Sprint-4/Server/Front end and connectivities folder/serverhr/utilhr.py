import json
import pickle
import numpy as np

__travel = None
__data_columns = None
__model = None
__dept = None
__edu = None
__gen = None
__jr = None
__ms = None

def get_attrition(age,dailyrate,distancefromhome,education,environmentsatisfaction,hourlyrate,jobinvolvement,joblevel,jobsatisfaction,monthlyincome,monthlyrate,numcompaniesworked,over18,overtime,percentsalaryhike,performancerating,relationshipsatisfaction,stockoptionlevel,totalworkingyears,trainingtimeslastyear,worklifebalance,yearsatcompany,yearsincurrentrole,yearssincelastpromotion,yearswithcurrmanager,travel,dept,edu,gender,jobrole,maritalstatus):
    try:
        ms_index = __data_columns.index(maritalstatus.lower())
    except:
        ms_index = -1

    try:
        travel_index = __data_columns.index(travel.lower())
    except:
        travel_index = -1

    try:
        dept_index = __data_columns.index(dept.lower())
    except:
        dept_index = -1

    try:
        edu_index = __data_columns.index(edu.lower())
    except:
        edu_index = -1

    try:
        gen_index = __gen_columns.index(gender.lower())
    except:
        gen_index = -1

    try:
        jobrole_index = __data_columns.index(jobrole.lower())
    except:
        jobrole_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = age
    x[1] = dailyrate
    x[2] = distancefromhome
    x[3] = education
    x[4] = environmentsatisfaction
    x[5] = hourlyrate
    x[6] = jobinvolvement
    x[7] = joblevel
    x[8] = jobsatisfaction
    x[9] = monthlyincome
    x[10] = monthlyrate
    x[11] = numcompaniesworked
    x[12] = over18
    x[13] = overtime
    x[14] = percentsalaryhike
    x[15] = performancerating
    x[16] = relationshipsatisfaction
    x[17] = stockoptionlevel
    x[18] = totalworkingyears
    x[19] = trainingtimeslastyear
    x[20] = worklifebalance
    x[21] = yearsatcompany
    x[22] = yearsincurrentrole
    x[23] = yearssincelastpromotion
    x[24] = yearswithcurrmanager

    if ms_index >= 0:
        x[ms_index] = 1

    if travel_index >= 0:
        x[travel_index] = 1

    if dept_index >= 0:
        x[dept_index] = 1

    if edu_index >= 0:
        x[edu_index] = 1

    if gen_index >= 0:
        x[gen_index] = 1

    if jobrole_index >= 0:
        x[jobrole_index] = 1

    return __model.predict([x])[0]


def loading():
    print("load")
    global __travel
    global __dept
    global __data_columns
    global __edu
    global __jr
    global __ms
    global __gen

    with open("./artifactshr/columnshr.json",'r') as f:
        __data_columns = json.load(f)["data_columns"]
        __travel = __data_columns[25:28]
        __dept = __data_columns[28:31]
        __gen = __data_columns[37:39]
        __edu = __data_columns[31:37]
        __jr = __data_columns[39:48]
        __ms = __data_columns[48:]
        print("load done")

    global __model
    if __model is None:
        with open("./artifactshr/HR_Attrition_prediction.pickle", 'rb') as f:
            __model = pickle.load(f)

def get_travel_details():
    return __travel

def get_dept_details():
    return __dept

def get_education_details():
    return __edu

def get_gender_details():
    return __gen

def get_jobrole_details():
    return __jr

def get_maritalstatus_details():
    return __ms


if __name__ == '__main__':
    loading()
    print(get_travel_details())
    print(get_dept_details())
    print(get_gender_details())
    print(get_jobrole_details())
    print(get_maritalstatus_details())
    print(get_education_details())
    print(get_attrition(41,1102,1,2,2,94,3,2,4,5993,19479,8,1,1,11,3,1,0,8,0,1,6,4,0,5,'travel_rarely','Sales','life sciences','female','sales executive','single'))
    print(get_attrition(49,279,8,1,3,61,2,2,2,5130,24907,1,1,0,23,4,4,1,10,3,3,10,7,1,7,'travel_frequently','research & development','life sciences','male','research scientist','married'))
    print(get_attrition(34,1346,19,2,2,93,3,1,4,2661,8758,0,1,0,11,3,3,1,3,2,3,2,2,1,2,'travel_rarely','research & development','medical','male','laboratory technician','divorced'))
    print(get_attrition(50, 1346, 19, 2, 2, 93, 3, 1, 4, 2661, 8758, 0, 1, 0, 11, 3, 3, 1, 3, 2, 3, 2, 2, 1, 2,'travel_frequently', 'research & development', 'medical', 'female', 'laboratory technician','divorced'))

