$(document).on('click', '#toggle_icon', function() {

  $(this).toggleClass("active");
  
  var input = $("#id_password");
  
  input.attr('type') === 'password' ? input.attr('type','text') : input.attr('type','password')
  
});
