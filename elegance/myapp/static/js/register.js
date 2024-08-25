$(document).ready(function () {
  $("form").submit(function (event) {
    event.preventDefault();
    let formData = {
      first_name : $('#first_name').val(),
      last_name: $('#last_name').val(),
      email: $('#email').val(),
      password: $('#password').val()
    };

    $.ajax({
      url: "http://127.0.0.1:5001/api/v1/users/register",
      type: "POST",
      data: JSON.stringify(formData),
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      success: function(response) {
        if (response) {
          swal({
            title: "Se guardó el registro correctamente",
            text: "",
            icon: "success",
            buttons: {
              confirm: {
                text: "Continuar",
                value: true,
                visible: true,
                className: "bg-primary",
                closeModal: false
              }
            },
            dangerMode: true,
            position: 'center',
          })
          .then((value) => {
            if (value) {
              window.location.href ="/glab_books/";
            }
          });
        } else {
          swal("Datos  incorrectos", "", "error");
        }
      }
    })
  });
});