$(document).ready(function() {
  $('#login-form').submit(function(event) {
    event.preventDefault(); // Prevent default form behavior

    const email = $('#email_i').val();
    const password = $('#password_i').val();

    // Check if the user exists by making a GET request to the API
    $.ajax({
      url: "http://127.0.0.1:8000/api/v1/users",
      method: 'GET',
      dataType: 'json',
      headers: {
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN' // Reemplaza con el token real si es necesario
      },
      success: function(response) {
        let userExists = false;
        let userId = null;
        let isStaff = false;
        
        for (let i = 0; i < response.length; i++) {
          if (response[i].email === email) {
            userExists = true;
            userId = response[i].id;
            isStaff = response[i].is_staff; // Obtiene el valor de is_staff
            break;
          }
        }

        if (userExists) {
          // Authenticate the user by making a POST request to the API
          $.ajax({
            url: "http://127.0.0.1:8000/api/v1/users/login",
            method: 'POST',
            dataType: 'json',
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify({ email: email, password: password }),
            success: function(response) {
              if (response.is_user === true) {
                if (isStaff) {
                  window.location.href = "http://127.0.0.1:8000/admin-categories/";
                } else {
                  window.location.href = "http://127.0.0.1:8000/";
                }
              } else {
                Swal.fire({
                  title: 'Rol desconocido',
                  icon: 'warning',
                  confirmButtonText: 'OK'
                });
              }
            },
            error: function(jqXHR, textStatus, errorThrown) {
              Swal.fire({
                title: 'Credenciales inválidas. Inténtelo de nuevo.',
                icon: 'warning',
                confirmButtonText: 'OK'
              });
            }
          });
        } else {
          Swal.fire({
            title: 'El usuario no existe. Por favor regístrese.',
            icon: 'warning',
            confirmButtonText: 'OK'
          });
        }
      },
      error: function(jqXHR, textStatus, errorThrown) {
        Swal.fire({
          title: 'Ocurrió un error al buscar el usuario.',
          icon: 'error',
          confirmButtonText: 'OK'
        });
      }
    });
  });
});
