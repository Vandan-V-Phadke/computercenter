var day;
var zone;
var hour;
var tablecontents;
var tf = 9;
var tt = 10;
var selectedParam;
var selectedZones=[];
var hourNzone;

function setCallbacks(){
        $(".day").click(function(){
            day = $(this).attr('data-day');
            
            //Get the time, date and day
            var e = document.getElementById("monthchooser");
            var month = e.options[e.selectedIndex].text;

            var e1 = document.getElementById("yearchooser");
            var year = e1.options[e.selectedIndex].text;

            console.log(day);
            console.log(month);
            console.log(year);

            if(month == 'January') month = 1 ; 

            //Send data and fetch the availability here
            var sendData = { day:day, month:month, year:year};
            var query =
                $.ajax({
                    
                    url: "http://127.0.0.1:8000/ccbook/available",
                    type : "POST",
                    crossDomain: true,
                    data: sendData,
                    dataType: 'json',
                    
                    // handle a successful response
        success : function(json) {
                    var json = json;
                    console.log("success"); // another sanity check
                    alert(json["data"]);
                                },

                    // handle a non-successful response
        
        error : function(json) {
                    var json = $.parseJSON(json); 
                    console.log("failure"); // another sanity check           
        }
                
            });


            CreateTable();
            showTable();
            
        });

}

function showTable(){
    $("#table-container").html(tablecontents);
    
       $(".zone").click(function(){

            zone = $(this).attr('data-zone');
            hour = $(this).attr('data-hour');
            //hourNzone=[hour,zone];
            selectedZones[hour]=zone;
            var n=selectedZones.length;
            
            if(hourNzone in selectedZones){
              // Find and remove item from zone array
        var index = selectedZones.indexOf(hourNzone);
        console.log(index); 
        if(index != -1) {
          selectedZones.splice(index, 1);
        }

            }else{
              //add item to zone array
              selectedZones.push(hourNzone);

            } 

            selectedParam="("+ day + ")  (Hour:" + hour + ")  (Zone: " + zone +")";
            console.log(selectedParam);
            //for(var i;i<selectedZones.length;i++){
            console.log(selectedZones);
            console.log(selectedZones.length); 
            
        });
}


function checkZones(){

  for( var i=0; i<selectedZones.length; i++ ) {
      if( selectedZones[i][1] == zone && selectedZones[i][0] == hour ) {
          var index = selectedZones.indexOf(hourNzone);
      if(index != -1) {
        selectedZones.splice(index, 1);
        alert("Value Removed");
      }
    }else{
      selectedZones.push(hourNzone);
        alert("Value added");
    }
  }

}

function showData(){
  $("#table-container").html(selected);
}
 
   
function CreateTable()
{
    tablecontents = "";

    tablecontents = "<center><table border=2 cellpadding="+ 5 + " >";
    tablecontents += "<TR><TH>" + "Interval" +"</TH><TH>" + "09-10" +"</TH><TH>"+ "10-11" + "</TH><TH>" + "11-12" +"</TH><TH>" 
              + "12-01" +"</TH><TH>" + "01-02" +"</TH><TH>" 
              + "02-03" +"</TH><TH>" + "03-04" +"</TH><TH>"
              + "04-05" +"</TH><TH>" + "05-06" +"</TH><TH>"
              + "06-07" +"</TH><TH>" + "07-08" +"</TH><TH>"
              + "08-09" +"</TH><TH>" + "09-10" +"</TH><TH>"
              + "10-11" +"</TH></TR>";
    tablecontents += "<TR><TH>" + "Hours" +"</TH><TH>" + "1" +"</TH><TH>"+ "2" + "</TH><TH>" + "3" +"</TH><TH>" 
              + "4" +"</TH><TH>" + "5" +"</TH><TH>" 
              + "6" +"</TH><TH>" + "7" +"</TH><TH>"
              + "8" +"</TH><TH>" + "9" +"</TH><TH>"
              + "10" +"</TH><TH>" + "11" +"</TH><TH>"
              + "12" +"</TH><TH>" + "13" +"</TH><TH>"
              + "14" +"</TH></TR>";
   
  tablecontents += "<tr>";
  tablecontents += "<td rowspan=6><b>" + "Zones" + "</b></td>";      
    
      for(var j=1;j<=14;j++){
        tablecontents += "<td><span class='zone' style=\"color: #f00;\" data-zone='1/1' data-hour='"+ j +"'>" + "1/1" + "</span></td>";
      }
    tablecontents += "</tr><tr>";



    for(var j=1;j<=14;j++){
        tablecontents += "<td><span class='zone' style=\"color: #f00;\" data-zone='1/2' data-hour='"+ j +"'>" + "1/2" + "</span></td>";
      }
      tablecontents += "</tr><tr>";


      for(var j=1;j<=14;j++){
        tablecontents += "<td><span class='zone' style=\"color: #f00;\" data-zone='2/1' data-hour='"+ j +"'>" + "2/1" + "</span></td>";
      }

      tablecontents += "</tr><tr>";



      for(var j=1;j<=14;j++){
        tablecontents += "<td><span class='zone' style=\"color: #f00;\" data-zone='2/2' data-hour='"+ j +"'>" + "2/2" + "</span></td>";
      }
      tablecontents += "</tr><tr>";

      for(var j=1;j<=14;j++){
        tablecontents += "<td><span class='zone' style=\"color: #f00;\" data-zone='3/1' data-hour='"+ j +"'>" + "3/1" + "</span></td>";
      }
      tablecontents += "</tr><tr>";


      for(var j=1;j<=14;j++){
        tablecontents += "<td><span class='zone' style=\"color: #f00;\" data-zone='3/2' data-hour='"+ j +"'>" + "3/2" + "</span></td>";
      }
      tablecontents += "</tr>";
      
   tablecontents += "</table></center>";
}



// day of week of month's first day
function getFirstDay(theYear, theMonth){
    var firstDate = new Date(theYear,theMonth,1)
    return firstDate.getDay()
}
// number of days in the month
function getMonthLen(theYear, theMonth) {
    var oneDay = 1000 * 60 * 60 * 24
    var thisMonth = new Date(theYear, theMonth, 1)
    var nextMonth = new Date(theYear, theMonth + 1, 1)
    var len = Math.ceil((nextMonth.getTime() - thisMonth.getTime())/oneDay)
    return len
}

// create array of English month names
var theMonths = ["January","February","March","April","May","June","July","August","September","October","November","December"]

// return IE4+ or W3C DOM reference for an ID
function getObject(obj) {
    var theObj
    if (document.all) {
        if (typeof obj == "string") {
            return document.all(obj)
        } else {
            return obj.style
        }
    }
    if (document.getElementById) {
        if (typeof obj == "string") {
            return document.getElementById(obj)
        } else {
            return obj.style
        }
    }
    return null
}

/************************
  DRAW CALENDAR CONTENTS
*************************/
// clear and re-populate table based on form's selections
function populateTable(form) {
    
    var theMonth = form.chooseMonth.selectedIndex
    var theYear = parseInt(form.chooseYear.options[form.chooseYear.selectedIndex].text)
    
    // initialize date-dependent variables
    var firstDay = getFirstDay(theYear, theMonth)
    var howMany = getMonthLen(theYear, theMonth)
    
    // fill in month/year in table header
    getObject("tableHeader").innerHTML = theMonths[theMonth] + " " + theYear
    
    // initialize vars for table creation
    var dayCounter = 1
    var TBody = getObject("tableBody")
    
    // clear any existing rows
    while (TBody.rows.length > 0) {
        TBody.deleteRow(0)
    }

    var newR, newC
    var done=false
    while (!done) {
        // create new row at end
        newR = TBody.insertRow(TBody.rows.length)
        for (var i = 0; i < 7; i++) {
            // create new cell at end of row
            newC = newR.insertCell(newR.cells.length)
            if (TBody.rows.length == 1 && i < firstDay) {
                // no content for boxes before first day
                newC.innerHTML = ""    
                continue
            }
            if (dayCounter == howMany) {
                // no more rows after this one
                done = true
            }
            // plug in date (or empty for boxes after last day)
            var temp = (dayCounter <= howMany) ? dayCounter++ : "";
            newC.innerHTML = "<span class='day' data-day='" + temp + "'>"+temp+"</span>";
        }
        
    }
    setCallbacks();
}

/*******************
  INITIALIZATIONS
********************/
// create dynamic list of year choices
function fillYears() {
    var today = new Date()
    var thisYear = today.getFullYear()
    var yearChooser = document.dateChooser.chooseYear
    for (i = thisYear; i < thisYear + 5; i++) {
        yearChooser.options[yearChooser.options.length] = new Option(i, i)
    }
    setCurrMonth(today)
}

// set month choice to current month
function setCurrMonth(today) {
    document.dateChooser.chooseMonth.selectedIndex = today.getMonth()
}



      // Check if added value exists
/*      
  for( var i=0; i<selectedZones.length; i++ ) {
    console.log("Here 1");
      if(hourNzone in selectedZones) {
          console.log("Here 2");
          var index = selectedZones.indexOf(hourNzone);
      if(index != -1) {
        console.log("Here 3");
        selectedZones.splice(index, 1);
        alert("Value Removed");
      }
    }else{
      console.log("Here 4");
      selectedZones.push(hourNzone);
        alert("Value added");
    }
  }
console.log("Here 5");
      //checkZones();

*/


 /*  
function CreateTable()
{
    tablecontents = "";
    tablecontents = "<center><table border=2 cellpadding="+ 10 + " >";
    tablecontents += "<TR><TH>" + "Interval" +"</TH><TH>" + "Hour" +"</TH><TH COLSPAN=6>"+ "Zones" + "</TH></TR>";
    

for (var i = 1; i <= 14; i ++)
   {

    tablecontents += "<tr>";
    
    if(tf>12 && tt>12){
        var tf1=tf%12;
        var tt1=tt%12;
      tablecontents += "<b><td>" + tf1 + ":00 pm - " + tt1 + ":00 pm" + "</td></b>";
    }else if(tf==12){
      tablecontents += "<b><td>12:00 pm - 1:00 pm</td></b>";
    }else{      
      if(tf<12 && tt<12){ // 9-10 10-11
        tablecontents += "<b><td>" + tf + ":00 am - " + tt + ":00 am" + "</td></b>"; 
      }else if(tt==12){ // 11-12
        tablecontents += "<b><td>" + tf + ":00 am - " + tt + ":00 pm" + "</td></b>"; 
      }
    }
    tf=tf+1;
    tt=tf+1;
    //hour=i;
      tablecontents += "<b><td><span class='hour'>" + i + "th Hour" + "</td></b>";
      tablecontents += "<td><span class='zone' data-zone='1/1' data-hour='"+ i +"'>" + "1/1" + "</span></td>";
      tablecontents += "<td><span class='zone' data-zone='1/2' data-hour='"+ i +"'>" + "1/2" + "</span></td>";
      tablecontents += "<td><span class='zone' data-zone='2/1' data-hour='"+ i +"'>" + "2/1" + "</span></td>";
      tablecontents += "<td><span class='zone' data-zone='2/2' data-hour='"+ i +"'>" + "2/2" + "</span></td>";
      tablecontents += "<td><span class='zone' data-zone='3/1' data-hour='"+ i +"'>" + "3/1" + "</span></td>";
      tablecontents += "<td><span class='zone' data-zone='3/2' data-hour='"+ i +"'>" + "3/2" + "</span></td>";
      tablecontents += "</tr>";

   } //for 
  

   tablecontents += "</table></center>";
}
*/
