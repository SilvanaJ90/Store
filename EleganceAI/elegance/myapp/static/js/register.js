$(document).ready(function () {
  $("#registerForm").submit(function (event) {
    event.preventDefault();
    
    // Get the form values
    let password = $('#password').val();
    let confirmPassword = $('#confirm_password').val();

    // Validate that the passwords match
    if (password !== confirmPassword) {
      Swal.fire("Las contraseñas no coinciden", "", "error");
      return;
    }

    // Prepare the form data
    let formData = {
      first_name: $('#first_name').val(),
      last_name: $('#last_name').val(),
      email: $('#email').val(),
      password: password
    };

    $.ajax({
      url: "http://127.0.0.1:8000/api/v1/users/register/",
      type: "POST",
      data: JSON.stringify(formData),
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      success: function(response) {
        if (response) {
          Swal.fire({
            title: "Registro exitoso",
            text: "",
            icon: "success",
            confirmButtonText: "Continuar",
            confirmButtonColor: "#3085d6",
            position: 'center',
            allowOutsideClick: false
          }).then((result) => {
            if (result.isConfirmed) {
              window.location.href = "http://127.0.0.1:8000/signin/";
            }
          });
        } else {
          Swal.fire("Error en el registro", "", "error");
        }
      },
      error: function(xhr, status, error) {
        Swal.fire("Error en el registro", "Por favor, inténtelo de nuevo más tarde.", "error");
      }
    });
  });
});
