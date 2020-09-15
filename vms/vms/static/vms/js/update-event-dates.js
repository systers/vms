// Loads at the start

var container=$('.bootstrap-iso form').length>0 ? $('.bootstrap-iso form').parent() : "body";
var eventList = document.getElementById("events");
var selectedEvent = eventList.options[eventList.selectedIndex];
var firstelementStartDate = selectedEvent.getAttribute("start_date");
var firstelementEndDate = selectedEvent.getAttribute("end_date");
var firstelementNonFormattedStartDate = selectedEvent.getAttribute("non_formatted_start_date");
var firstelementNonFormattedEndDate = selectedEvent.getAttribute("non_formatted_end_date");
document.getElementById("start_date_here").innerHTML = firstelementNonFormattedStartDate;
document.getElementById("end_date_here").innerHTML = firstelementNonFormattedEndDate;

$(document).ready(function() {
  $("#datepicker").datepicker();
});

$(function(){
  $('#from').datepicker({
        format: 'dd/mm/yyyy',
        minDate:firstelementStartDate,
        maxDate:firstelementEndDate,
        container: container,
        todayHighlight: true,
        autoclose: true,
        changeMonth:true,
        changeYear:true,
    });

    $('#to').datepicker({
        format: 'dd/mm/yyyy',
        minDate:firstelementStartDate,
        maxDate:firstelementEndDate,             
        container: container,
        todayHighlight: true,
        autoclose: true,
        changeMonth:true,
        changeYear:true,

    });
});  


/** Update Selected event and corresponding date picker */
function updateEventDates() {
  var eventList = document.getElementById("events");
  var selectedEvent = eventList[eventList.selectedIndex];
  var startDate = selectedEvent.getAttribute("start_date");
  var endDate = selectedEvent.getAttribute("end_date");
  var nonFormattedStartDate = selectedEvent.getAttribute("non_formatted_start_date");
  var nonFormattedEndDate = selectedEvent.getAttribute("non_formatted_end_date");
  document.getElementById("start_date_here").innerHTML = nonFormattedStartDate;
  document.getElementById("end_date_here").innerHTML = nonFormattedEndDate;
  var container=$('.bootstrap-iso form').length>0 ? $('.bootstrap-iso form').parent() : "body";

  $('#from').datepicker("destroy");

  $('#from').datepicker({
        format: 'dd/mm/yyyy',
        minDate:startDate,
        maxDate:endDate,
        container: container,
        todayHighlight: true,
        autoclose: true,
        changeMonth:true,
        changeYear:true,

    });


    $('#to').datepicker("destroy");

    $('#to').datepicker({
        format: 'dd/mm/yyyy',
        minDate:startDate,              
        maxDate:endDate,              
        container: container,
        todayHighlight: true,
        autoclose: true,
        changeMonth:true,
        changeYear:true,
    });
}

