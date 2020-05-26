function showSignup (){
  $('#thirddiv').hide();
  $('#secondiv').show();
}

function hideSignup (){
  $('#thirddiv').show();
  $('#secondiv').hide();
}

function validate (e) {
  e.preventDefault();
  var pass = $("#password").val();
  var confpass = $("#password2").val();

  if (pass !== confpass) {
    alert("Password don't match: Kindly re-enter the Confirm Password");
    return false;
  }
  
  $("#login-form").append("<div id='countdown'>Account successfully created, redirecting to Login page in <b id='redirect-count'>5</b></div>");
  var count = 5;
  var timer = setInterval(function () {
      count--;
      $('#redirect-count').html(count);
  }, 1000);

  setTimeout(function () {
      clearInterval(timer);
      hideSignup();
      $('#countdown').remove();
  }, 5000);
}

$(document).ready(function () {
  $('#signup-btn').on('click', showSignup);
  $('#signup-form').on('submit', validate);
});