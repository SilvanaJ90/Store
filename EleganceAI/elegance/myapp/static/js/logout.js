const logoutBtn = document.getElementById('logout-btn');

logoutBtn.addEventListener('click', async () => {
    const response = await fetch('http://127.0.0.1:8000/api/v1/logout', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include'
    });
    
    if (response.ok) {

        window.location.href = 'http://127.0.0.1:8000/';
    } else {
        const errorData = await response.json();
        console.error(errorData.error);
    }
});