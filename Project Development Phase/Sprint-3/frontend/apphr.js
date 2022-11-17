// function genderValue() 
// {
//     var gender= 
//     switch(gender)
//     console.log(gender);
//     for(var i in gender)
//     {
//       if(gender[i].checked)
//       {
//           return gender[i].value;
//       }
//     }
//     return -1; 
//   }


// function maritalstatusValue() 
// {
//     var ms= document.getElementsByName("ms");
//     console.log(ms);
//     for(var i in ms)
//     {
//       if(ms[i].checked)
//       {
//           return ms[i].value;
//       }
//     }
//     return -1; 
// }


// function above18Value(age) 
// {  
//     if(age>=18)
//     {
//         return 1;
//     }
//     else
//     {
//         return 0;
//     }
// }
// var agestore;

function storeValue(event)
{
    console.log(event);
    console.log(event.target.value);
    sessionStorage.setItem(event.target.id, event.target.value);
}

function onClickedEstimatedAttrition(){
    console.log("Estimate Attrition button clicked");
    var age = sessionStorage.getItem("idage");
    console.log("age store "+age);
    var over18 = (age >=18) ? 1: 0;
    console.log("above 18 "+over18);
    var gender = sessionStorage.getItem("gender");
    console.log("gender "+gender);
    var travel = sessionStorage.getItem("idtravel");
    console.log("travel "+travel);
    var dept = sessionStorage.getItem("iddept");
    console.log("dept "+dept);
    var distancefromhome = sessionStorage.getItem("iddistfrmhm");
    console.log("distancefromhome "+distancefromhome);
    var education = sessionStorage.getItem("ideql");
    console.log("education "+education);
    var edu = sessionStorage.getItem("idef");
    console.log("edu "+edu);
    var joblevel = sessionStorage.getItem("idjl");
    console.log("joblevel "+joblevel);
    var jobrole = sessionStorage.getItem("idjobrole");
    console.log("jobrole "+jobrole);
    var maritalstatus = sessionStorage.getItem("ms");
    console.log("maritalstatus "+maritalstatus);
    var montlyincome = sessionStorage.getItem("idmi");
    console.log("montlyincome "+montlyincome);
    var numcompaniesworked = sessionStorage.getItem("idnocw");
    console.log("numcompaniesworked "+numcompaniesworked);
    var percentsalaryhike = sessionStorage.getItem("idposh");
    console.log("percentsalaryhike "+percentsalaryhike);
    var stockoptionlevel = sessionStorage.getItem("idsol");
    console.log("stockoptionlevel "+stockoptionlevel);
    var totalworkingyears = sessionStorage.getItem("idtwy");
    console.log("totalworkingyears "+totalworkingyears);
    var trainingtimeslastyear = sessionStorage.getItem("idth");
    console.log("ovetrainingtimeslastyearrtime "+trainingtimeslastyear);
    var yearsatcompany = sessionStorage.getItem("idworkingyears");
    console.log("yearsatcompany "+yearsatcompany);
    var yearssincelastpromotion = sessionStorage.getItem("idlastpromotion");
    console.log("yearssincelastpromotion "+yearssincelastpromotion);
    var yearswithcurrmanager = sessionStorage.getItem("idcm");
    console.log("yearswithcurrmanager "+yearswithcurrmanager);
    var estAttrition = document.getElementById("uiEstimatedAttrition");
    console.log(estAttrition);
    var url = "http://127.0.0.1:8080/predict_attrition"; //Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/predict_attrition"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
    $.post(url,{
        age: parseInt(age),
        distancefromhome: parseFloat(distancefromhome),  
        education: parseInt(education),
        joblevel: parseInt(joblevel),
        montlyincome: parseFloat(montlyincome),
        numcompaniesworked: parseInt(numcompaniesworked),
        over18: parseInt(over18),
        percentsalaryhike: parseFloat(percentsalaryhike),
        stockoptionlevel: parseInt(stockoptionlevel),
        totalworkingyears: parseFloat(totalworkingyears),
        trainingtimeslastyear: parseInt(trainingtimeslastyear),
        yearsatcompany: parseFloat(yearsatcompany),
        yearssincelastpromotion: parseFloat(yearssincelastpromotion),
        yearswithcurrmanager: parseFloat(yearswithcurrmanager),
        travel: travel,
        dept: dept,
        edu: edu,
        gender: gender,
        jobole: jobrole,
        maritalstatus: maritalstatus
    },function(data, status) {
        console.log(data.Attrition);
        estAttrition.innerHTML = "<center><h2>Attrition: " + data.Attrition + "</h2></center>";
        console.log(status);
    });

  }

  function onPageLoad() 
  {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:8080/get_travel_details"; // Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_travel_details request");
        if(data) {
            var travel = data.travel;
            var idtravel = document.getElementById("idtravel");
            $('#idtravel').empty();
            for(var i in travel) {
                var opt = new Option(travel[i]);
                $('#idtravel').append(opt);
            }
        }
    });
    var url = "http://127.0.0.1:8080/get_gender_details"; // Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {    
        console.log("got response for get_gender_details request");
        if(data) {
            var genderdet = data.gender;
            var gender = document.getElementById("genderdet");
            $('#gender').empty();
            for(var i in genderdet) {
                var opt = new Option(genderdet[i]);
                $('#gender').append(opt);
            }
        }
    });
    var url = "http://127.0.0.1:8080/get_education_details"; // Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_education_details request");
        if(data) {
            var educ = data.education;
            console.log(data);
            var idef = document.getElementById("idef");
            $('#idef').empty();
            for(var i in educ) {
                var opt = new Option(educ[i]);
                $('#idef').append(opt);
            }
        }
    });
    var url = "http://127.0.0.1:8080/get_dept_details"; // Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_dept_details request");
        if(data) {
            var dept = data.dept;
            var iddept = document.getElementById("iddept");
            $('#iddept').empty();
            for(var i in dept) {
                var opt = new Option(dept[i]);
                $('#iddept').append(opt);
            }
        }
    });
    var url = "http://127.0.0.1:8080/get_jobrole_details"; // Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_jobrole_details request");
        if(data) {
            var jobrole = data.jobrole;
            var idjobrole = document.getElementById("idjobrole");
            $('#idjobrole').empty();
            for(var i in jobrole) {
                var opt = new Option(jobrole[i]);
                $('#idjobrole').append(opt);
            }
        }
    });
    var url = "http://127.0.0.1:8080/get_maritalstatus_details"; // Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_maritalstatus_details request");
        if(data) {
            var mars = data.maritalstatus;
            var ms = document.getElementById("ms");
            $('#ms').empty();
            for(var i in mars) {
                var opt = new Option(mars[i]);
                $('#ms').append(opt);
            }
        }
    });
  }
  
    window.onload = onPageLoad();
