$(document).ready(function(){
$("#select_country").change(function(){
   var countryId = $(this).val(); 
  $.ajax({
  	url: StateUrl,
  	data: {
          'country': countryId
        },
         success: function (states) {
       $("#select_state").html(states);
        }
  });
});
});
