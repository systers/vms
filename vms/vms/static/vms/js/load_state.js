$(document).ready(function() {
    $("#select_country").change(function() {
console.log("hi")
/* Disables the city and state input field until the country input is filled up */
	function hideState(){
		var country = $("#select_country");
    		var state = $("#select_state");
		var city = $("#select_city");

		if(country.val() === "0") {
			state.prop("disabled", true); console.log("country 0");
			city.prop("disabled", true);
		}  
		if (country.val() !== "0"){ console.log("country 0");
			state.prop("disabled", false);
		}  console.log(state.val())
		if(state.prop('disabled') === false && state.val() !== null && state.val() !== "0") {
			city.prop("disabled", false);
		}
		else {
			city.prop("disabled", true);
			city.val("");
		}
 console.log(state.val())
	}
	hideState(); 

/** Fetches states belonging to selected  country */
        var countryId = $(this).val();
        $.ajax({
            url: CheckState,
            data: {
                "country": countryId
            },
            success: function(statecheck) {
                if (statecheck === false) {
                    $.ajax({
                        url: CityUrl,
                        data: {
                            "country": countryId,
                            "state": 0
                        },
                        success: function(cities) {
    				var state = $("#select_state");
				var city = $("#select_city");
				if(state.val() !== "0" && state.val() !== null &&state.prop('disabled') === false) {
               				city.html(cities);
				}
				else {  
					city.empty();
				}
                         	state.empty(); 
			 },
                    });
                } else if (statecheck === true) {
                    $.ajax({
                        url: StateUrl,
                        data: {
                            "country": countryId
                        },
                        success: function(states) {
    				var state = $("#select_state");
				var city = $("#select_city");
				state.html(states);
                           	city.empty();	 
                        }
                    });
                }
            }
        }); 
    });
});
