document.addEventListener("DOMContentLoaded", function () {
    // Get the dark mode switch for the navbar and store it in a variable
    const darkModeSwitch = document.getElementById('darkModeSwitch');
    const navbar = document.getElementById('navbar');

    // Function to set the theme based on the current dark mode setting
    function setTheme() {
        if (document.body.classList.contains('dark-mode')) {
            // Set dark mode theme for the navbar
            navbar.classList.remove('navbar-light');
            navbar.classList.add('navbar-dark');
            darkModeSwitch.checked = true; // Dark mode, so switch is on
        } else {
            // Set light mode theme for the navbar
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

    // Add event listener to the dark mode switch on the navbar
    darkModeSwitch.addEventListener('change', toggleDarkMode);

    // Get the dark mode switch for the profile page and store it in a variable
    const profileDarkModeSwitch = document.getElementById('profileDarkModeSwitch');

    // Function to toggle dark mode on the profile page
    function toggleProfileDarkMode() {
        document.body.classList.toggle('dark-mode');
        setTheme();

        // Save user's preference to local storage
        localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
    }

    // Add event listener to the dark mode switch on the profile page
    if (profileDarkModeSwitch) {
        profileDarkModeSwitch.addEventListener('change', toggleProfileDarkMode);
    }

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

    // Function to clear error messages
    function clearErrorMessages(form) {
        const errorMessages = form.querySelectorAll('.error-message');
        errorMessages.forEach(message => {
            message.textContent = "";
        });
    }

    // Add event listener to the "Reset" button
    const resetButton = document.getElementById('resetButton');
    if (resetButton) {
        resetButton.addEventListener('click', function () {
            // Reset the form by accessing it through the parent form element
            const form = this.closest('form');
            if (form) {
                form.reset();
            }
        });
    }
    
    // Function to check if password and confirm password match
    function validatePassword() {
        const password = document.getElementById('password').value;
        const confirmPassword = document.getElementById('confirmPassword').value;
        const confirmPasswordError = document.getElementById('confirmPasswordError');

        if (password !== confirmPassword) {
            confirmPasswordError.textContent = "Password and confirm password should be same";
            return false;
        } else {
            confirmPasswordError.textContent = ""; // Clear the error message
            return true;
        }
    }

    const section1Button = document.getElementById('section1Button');
    const section2Button = document.getElementById('section2Button');
    const section3Button = document.getElementById('section3Button');

    const section1 = document.getElementById('section1');
    const section2 = document.getElementById('section2');
    const section3 = document.getElementById('section3');

    section1Button.addEventListener('click', function () {
        section1.style.display = 'block';
        section2.style.display = 'none';
        section3.style.display = 'none';
    });

    section2Button.addEventListener('click', function () {
        section1.style.display = 'none';
        section2.style.display = 'block';
        section3.style.display = 'none';
    });

    section3Button.addEventListener('click', function () {
        section1.style.display = 'none';
        section2.style.display = 'none';
        section3.style.display = 'block';
    });

    // Add event listeners and API request logic for each form here
    const section1Form = document.getElementById('section1Form');
    section1Form.addEventListener('submit', function (event) {
        event.preventDefault();
        // Perform API request for Section 1
        // ...
    });

    const section2Form = document.getElementById('section2Form');
    section2Form.addEventListener('submit', function (event) {
        event.preventDefault();
        // Perform API request for Section 2
        // ...
    });

    const section3Form = document.getElementById('section3Form');
    section3Form.addEventListener('submit', function (event) {
        event.preventDefault();
        // Perform API request for Section 3
        // ...
    });


    // Add event listener to the form submit button to clear error messages and validate passwords before submission
    const forms = document.querySelectorAll('.custom-form');
    forms.forEach(form => {
        form.addEventListener('submit', function (event) {
            // Clear existing error messages
            clearErrorMessages(form);

            // Validate passwords
            const isPasswordValid = validatePassword();
            if (!isPasswordValid) {
                event.preventDefault(); // Prevent form submission if passwords don't match
            }
        });
    });

});
