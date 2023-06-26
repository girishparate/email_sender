$("#password").keyup(function(){
    var password = $("#password").val()
    var password_conf = $("#confirm_password").val()
    if (password==password_conf && password_conf.length > 0){
        $("#registration_submit").prop("disabled", false);
    }
  });

  $("#confirm_password").keyup(function(){
    var password = $("#password").val()
    var password_conf = $("#confirm_password").val()
    if (password==password_conf && password.length > 0){
        $("#registration_submit").prop("disabled", false);
    }
  });