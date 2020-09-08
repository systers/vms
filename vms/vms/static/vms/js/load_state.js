$(document).ready(function() {
    $("#select_country").change(function() {
/* Disables the city and state input field until the country input is filled up */
	function hideState(){
 		var country =document.getElementById("select_country").value;
    		var state =document.getElementById("select_state").value;
		if(country==="0") {
			document.getElementById("select_state").disabled='disabled';
			document.getElementById("select_city").disabled='disabled';
		}  
		if (country!=="0"){
			document.getElementById("select_state").disabled=false;	
		}
		if(state.disabled===false && state.value!==null && state.value!=="0") {
			document.getElementById("select_city").disabled=false;
		}
		else {
			document.getElementById("select_city").disabled=true;
			document.getElementById("select_city").value="";
		}
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
		var state=$("#select_state"); 
		if(state.val()!=="0" && state.val()!==null && state.prop('disabled')===false)
              $("#select_city").html(cities);
		else  
              $("#select_city").empty();
        $("#select_state").empty(); 
                      
			 },
			
                    });
                } else if (statecheck === true) {
                    $.ajax({
                        url: StateUrl,
                        data: {
                            "country": countryId
                        },
                        success: function(states) {
                            $("#select_state").html(states);
                            $("#select_city").empty();
				 
                        }
                    });
                }
            }
        }); 
    });

});










