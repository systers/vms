$(document).ready(function() {
    $("#select_state").change(function() {
/* Disables the city input field until the state input is filled up */
	function hideCity(){
		var state =document.getElementById("select_state");
		if(state.disabled===false && state.value!==null && state.value!=="0") {
			document.getElementById("select_city").disabled=false;
		}
		else {
			document.getElementById("select_city").disabled=true;
		}
	}
    hideCity(); 

/** Fetches cities belonging to selected state and country */
        var countryId = $("#select_country").val();
        var stateId = $(this).val();
        $.ajax({
            url: CityUrl,
            data: {
                "country": countryId,
                "state": stateId
            },
            success: function(cities) {
		var state=$("#select_state"); 
		if(state.val()!=="0" && state.val()!==null && state.prop('disabled')===false)
                	$("#select_city").html(cities);
		else  
			$("#select_city").empty();
            }
        });


    });

});

