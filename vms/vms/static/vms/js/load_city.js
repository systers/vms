$(document).ready(function() {
    $("#select_state").change(function() {
	
/* Disables the city input field until the state input is filled up */
	function hideCity(){
		var country = $("#select_country");
    		var state = $("#select_state");
		var city = $("#select_city"); 
		if(state.prop('disabled') === false && state.val() !== null && state.val() !== "0") {
			city.prop("disabled", false);
		}
		else {
			city.prop("disabled", true);
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
		var state = $("#select_state");
		var city = $("#select_city");
		if(state.val() !== "0" && state.val()!==null && state.prop('disabled') === false) {
                	city.html(cities);
		}
		else { 
			city.empty();
		}
            }
        });
    });
});
