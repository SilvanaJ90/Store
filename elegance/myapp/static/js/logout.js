const logoutBtn = document.getElementById('logout-btn');

logoutBtn.addEventListener('click', async () => {
    const response = await fetch('http://127.0.0.1:8000/api/v1/logout', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include'  // Incluye cookies en la solicitud
    });
    
    if (response.ok) {
        // Redirecciona al usuario a la página de inicio de sesión
        window.location.href = 'http://127.0.0.1:8000/';
    } else {
        // Maneja el error de cierre de sesión
        const errorData = await response.json();
        console.error(errorData.error);
    }
});