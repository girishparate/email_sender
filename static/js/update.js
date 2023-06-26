$( "#update_email_cred" ).on( "submit", function( event ) {
    loginForm = $( this ).serializeArray();
    event.preventDefault();
    var loginFormObject = {};
    $.each(loginForm,
        function(i, v) {
            loginFormObject[v.name] = v.value;
        });
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    $.ajax({
        type: 'put',
        headers: {'X-CSRFToken': csrftoken},
        url: '/update-email-credential',
        data: loginFormObject,
        success: function(response) {location.reload()}
    })
  } );