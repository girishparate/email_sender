$("#password").keyup(function(){
    var password = $("#password").val()
    var password_conf = $("#confirm_password").val()
    if (password==password_conf){
        $("#registration_submit").prop("disabled", false);
    }
  });

  $("#confirm_password").keyup(function(){
    var password = $("#password").val()
    var password_conf = $("#confirm_password").val()
    if (password==password_conf){
        $("#registration_submit").prop("disabled", false);
    }
  });