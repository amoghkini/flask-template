document.addEventListener("DOMContentLoaded", function () {
    // Get the dark mode switch and store it in a variable
    const darkModeSwitch = document.getElementById('darkModeSwitch');
    const navbar = document.getElementById('navbar');

    // Function to set the theme based on the current dark mode setting
    function setTheme() {
        if (document.body.classList.contains('dark-mode')) {
            // Set dark mode theme
            navbar.classList.remove('navbar-light');
            navbar.classList.add('navbar-dark');
            darkModeSwitch.checked = true; // Dark mode, so switch is on
        } else {
            // Set light mode theme
            navbar.classList.remove('navbar-dark');
            navbar.classList.add('navbar-light');
            darkModeSwitch.checked = false; // Light mode, so switch is off
        }
    }

    // Function to toggle dark mode on or off
    function toggleDarkMode() {
        document.body.classList.toggle('dark-mode');
        setTheme();

        // Save user's preference to local storage
        localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
    }

    // Check if the user has previously selected dark mode
    const isDarkMode = localStorage.getItem('darkMode') === 'true';

    // Set initial dark mode based on user's previous selection
    if (isDarkMode) {
        toggleDarkMode();
    } else {
        setTheme(); // Set theme based on current dark mode setting
    }

    // Add event listener to the dark mode switch
    darkModeSwitch.addEventListener('change', toggleDarkMode);

    // Show/Hide Password functionality
    const togglePassword = document.querySelectorAll('.toggle-icon');
    togglePassword.forEach((icon) => {
        icon.addEventListener('click', function () {
            const passwordField = this.previousElementSibling;
            if (passwordField.type === 'password') {
                passwordField.type = 'text';
                this.classList.remove('fa-eye');
                this.classList.add('fa-eye-slash');
            } else {
                passwordField.type = 'password';
                this.classList.remove('fa-eye-slash');
                this.classList.add('fa-eye');
            }
        });
    }); 
});
