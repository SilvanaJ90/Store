$(document).ready(function () {
  $("form").submit(function (event) {
    event.preventDefault();
    
    let formData = {
      first_name: $('#first_name').val(),
      last_name: $('#last_name').val(),
      email: $('#email').val(),
      password: $('#password').val()
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
            title: "Se guardó el registro correctamente",
            text: "",
            icon: "success",
            confirmButtonText: "Continuar",
            confirmButtonColor: "#3085d6",
            cancelButtonText: "Cancelar",
            position: 'center',
            allowOutsideClick: false
          }).then((result) => {
            if (result.isConfirmed) {
              window.location.href = "http://127.0.0.1:8000/";
            }
          });
        } else {
          Swal.fire("Datos incorrectos", "", "error");
        }
      }
    });
  });
});
