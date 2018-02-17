<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script> 
 {% block setting_content %}
 {% block setting_content %}
<script>
$( document ).ready(function() {
var valeur=0;
var a1=12;
var a2=13;
var a3=12;
var a4=13;
var a5=12;
var a6=13;
var a7=12;
var a8=13;

$('#v1').on('input', function() {
    valeur+=a1;
    a1=0; 
     document.getElementById("myProgress").value = valeur;
    
});

    
$('#v2').change(function() {
    valeur+=a2;
    a2=0;
     document.getElementById("myProgress").value = valeur;
   
   
});


$('#v3').change(function() {
    valeur+=a3;
    a3=0;
     document.getElementById("myProgress").value = valeur;
   
   
});

$('#v4').change(function() {
    valeur+=a4;
    a4=0;
     document.getElementById("myProgress").value = valeur;
   
   
});

$('#v5').change(function() {
    valeur+=a5;
    a5=0;
     document.getElementById("myProgress").value = valeur;
   
   
});

$('#v6').change(function() {
    valeur+=a6;
    a6=0;
     document.getElementById("myProgress").value = valeur;
   
   
});


$('#v7').change(function() {
    valeur+=a7;
    a7=0;
     document.getElementById("myProgress").value = valeur;
   
   
});

$('#v8').change(function() {
    valeur+=a8;
    a8=0;
     document.getElementById("myProgress").value = valeur;
   
   
});
});
</script>  
