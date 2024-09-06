$(document).ready(function () {
  // Handle form submission
  $('#login-form').submit(function(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    const email = $('#email_i').val(); // Get the email value from the input field
    const password = $('#password_i').val(); // Get the password value from the input field

    // Authenticate the user by making a POST request to the API
    $.ajax({
      url: "http://127.0.0.1:8000/api/v1/users/login/",
      method: 'POST',
      dataType: 'json',
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify({ email: email, password: password }), // Send email and password as JSON
      success: function(response) {
        console.log('Login response:', response); // Log the login response

        // If authentication is successful, register the session
        $.ajax({
          url: "http://127.0.0.1:8000/api/v1/users/register-session/",
          method: 'POST',
          dataType: 'json',
          contentType: "application/json; charset=utf-8",
          data: JSON.stringify({ user_id: response.user_id, timestamp: new Date().toISOString() }),
          success: function() {
            console.log('Session registered successfully');
          },
          error: function(jqXHR, textStatus, errorThrown) {
            console.error('Error registering session:', errorThrown);
          }
        });

        // Redirect based on user role
        if (response.is_user) {
          window.location.href = "http://127.0.0.1:8000/";
        } else {
          window.location.href = "http://127.0.0.1:8000/qa_admin/";
        }
      },
      error: function(jqXHR, textStatus, errorThrown) {
        Swal.fire({
          title: 'Invalid credentials. Please try again.',
          icon: 'warning',
          confirmButtonText: 'OK'
        });
      }
    });
  });
});
