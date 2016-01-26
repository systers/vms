<script>
$( document ).ready(function() {

$(window).scroll(function () {
  var s = $(window).scrollTop();
  var d = $(document).height();
  var c = $(window).height();
   var scrollPercent = (s / (d-c)) * 100;
        var position = scrollPercent;
   $("#progressbar").attr('value', position);
   $("#progressbar").css({'background': 'Orange'});
});
});
</script>  
