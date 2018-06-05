$(document).ready(function(){
$("#select_country").change(function(){
   var countryId = $(this).val(); 
   console.log(countryId);
  $.ajax({
  	url: State_Url,
  	data: {
          'country': countryId
        },
         success: function (states) {
       $("#select_state").html(states);
        }
  });
});
});
