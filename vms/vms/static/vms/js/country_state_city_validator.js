$(document).ready(
    function() {
        $("select#id_country").change(function() {
            if ($(this).val() == '0') {
                $("select#id_state").html("<option value='0'>-- Select State --</option>");
                $("select#id_state").attr('disabled', true);
                $("select#id_city").html("<option value='0'>-- Select city --</option>");
                $("select#id_city").attr('disabled', true);
            } else {
                var url = "/registration/getstate/" + $(this).val();
                var country = $(this).val();
                $.getJSON(url, function(states) {
                    var options = '<option value="0">-- Select State --</option>';
                    for (var i = 0; i < states.length; i++) {
                        options += '<option value="' + states[i].pk + '">' + states[i].fields['name'] + '</option>';
                    }
                    $("select#id_state").html(options);
                    $("select#id_state option:first").attr('selected', 'selected');
                    $("select#id_state").attr('disabled', false);
                    $("select#id_city option:first").attr('selected', 'selected');
                    $("select#id_city").attr('disabled', false);
                });
            }
        });

        $("select#id_state").change(function() {
            if ($(this).val() == '0') {
                $("select#id_city").html("<option value='0'>-- Select city --</option>");
                $("select#id_city").attr('disabled', true);
            } else {
                var url = "/registration/getcity/" + $(this).val();
                var state = $(this).val();
                $.getJSON(url, function(cities) {
                    var options = '<option value="0">-- Select City --</option>';
                    for (var i = 0; i < cities.length; i++) {
                        options += '<option value="' + cities[i].pk + '">' + cities[i].fields['name_ascii'] + '</option>';
                    }
                    $("select#id_city").html(options);
                    $("select#id_city option:first").attr('selected', 'selected');
                    $("select#id_city").attr('disabled', false);
                });
            }
        });

    });
