function togglePasswordVisibility() {
    const passwordInput = document.getElementById('password');
    const toggleText = document.querySelector('.toggle-password');
    
    // Switch between hidden characters and standard text string
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        toggleText.textContent = 'Hide';
    } else {
        passwordInput.type = 'password';
        toggleText.textContent = 'Show';
    }
}