const darkModeSwitch = document.getElementById('darkModeSwitch');
const navbar = document.getElementById('navbar');

// Function to toggle dark mode
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    navbar.classList.toggle('navbar-dark', document.body.classList.contains('dark-mode'));
    navbar.classList.toggle('navbar-light', !document.body.classList.contains('dark-mode'));

    // Save the user's preference to local storage
    if (document.body.classList.contains('dark-mode')) {
        localStorage.setItem('darkMode', 'enabled');
    } else {
        localStorage.setItem('darkMode', 'disabled');
    }
}

// Check the user's preference from local storage, if available
if (localStorage.getItem('darkMode') === 'enabled') {
    toggleDarkMode();
}

darkModeSwitch.addEventListener('click', toggleDarkMode);
