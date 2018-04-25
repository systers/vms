$(document).ready(function(){
    $("#event-select").on("change", function() { 
        var eventName = $("#event-select").val();
        var value = "";
        $.ajax({
            url: "get_job_list/",
            data: {
              "event_name" : eventName
            },
            dataType: "json",
            success (data) {
                $("#job-select")
                    .empty()
                    .append("<option value=''>-- Select Job --</option>");
                for(var i=0; i< data.length; i++){
                    value = data[i].fields.name;
                    $("#job-select")
                        .append($("<option></option>")
                        .attr("value",value)
                        .text(value));
                }
            }
        });
    });
});