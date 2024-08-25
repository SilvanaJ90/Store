$(document).ready(function() {
  $('#login-form').submit(function(event) {
    event.preventDefault(); // Prevent default form behavior

    const email = $('#email_i').val();
    const password = $('#password_i').val();

    // Check if the user exists by making a GET request to the API
    $.ajax({
      url: "http://127.0.0.1:5001/api/v1/users",
      method: 'GET',
      dataType: 'json',
      success: function(response) {
        let userExists = false;
        let userId = null;
        for (let i = 0; i < response.length; i++) {
          if (response[i].email === email) {
            userExists = true;
            userId = response[i].id;
            break;
          }
        }

        if (userExists) {
          // Authenticate the user by making a POST request to the API
          $.ajax({
            url: "http://127.0.0.1:5001/api/v1/users/login",
            method: 'POST',
            dataType: 'json',
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify({ email: email, password: password }),
            success: function(response) {
              // Check user role and redirect
              if (response.is_user === true) {
                window.location.href = "/glab_books/allbooks";
              } else if (response.is_user === false) {
                window.location.href = "/glab_books/admin";
              } else {
                swal({
                  title: 'Rol desconocido',
                  icon: 'warning',
                  confirmButtonText: 'OK'
                });
              }
            },
            error: function(jqXHR, textStatus, errorThrown) {
              swal({
                title: 'Credenciales inválidas. Inténtelo de nuevo.',
                icon: 'warning',
                confirmButtonText: 'OK'
              });
            }
          });
        } else {
          swal({
            title: 'El usuario no existe. Por favor regístrese.',
            icon: 'warning',
            confirmButtonText: 'OK'
          });
        }
      },
      error: function(jqXHR, textStatus, errorThrown) {
        swal({
          title: 'Ocurrió un error al buscar el usuario.',
          icon: 'error',
          confirmButtonText: 'OK'
        });
      }
    });
  });
});
