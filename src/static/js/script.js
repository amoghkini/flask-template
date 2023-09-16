document.addEventListener("DOMContentLoaded", function () {
    // Function to set the theme based on the user's preference
    function setTheme() {
        const isDarkModeEnabled = document.body.classList.contains('dark-mode');
        if (isDarkModeEnabled) {
            document.documentElement.setAttribute('data-theme', 'dark');
        } else {
            document.documentElement.setAttribute('data-theme', 'light');
        }
    }

    // Function to save the dark mode status to the backend
    function saveDarkModeStatus(isDarkModeEnabled) {
        fetch('/api/set-dark-mode', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ darkMode: isDarkModeEnabled }),
        })
            .then(response => response.json())
            .then(data => {
                console.log('Dark mode status saved to the backend:', data);
            })
            .catch(error => {
                console.error('Error saving dark mode status:', error);
            });
    }

    // Function to check the dark mode status from the backend and update the button state
    function checkDarkModeStatus() {
        // Fetch the dark mode status from the backend
        fetch('/api/get-dark-mode')
            .then(response => response.json())
            .then(data => {
                const isDarkModeEnabled = data.darkMode;
                const profileDarkModeSwitch = document.getElementById('profileDarkModeSwitch');

                if (profileDarkModeSwitch) {
                    // Update the dark mode switch state on the profile page
                    profileDarkModeSwitch.checked = isDarkModeEnabled;
                    // Set the theme based on the current dark mode setting
                    if (isDarkModeEnabled) {
                        document.body.classList.add('dark-mode');
                    } else {
                        document.body.classList.remove('dark-mode');
                    }
                    setTheme();
                }
            })
            .catch(error => {
                console.error('Error checking dark mode status:', error);
            });
    }

    // Function to toggle dark mode on the profile page
    function toggleProfileDarkMode() {
        const isProfileDarkMode = document.body.classList.contains('dark-mode'); // Check if profile page is in dark mode
        document.body.classList.toggle('dark-mode'); // Toggle dark mode
        setTheme(); // Set theme based on the current dark mode setting

        // Save user's preference to local storage
        localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));

        // Save the dark mode status to the backend
        saveDarkModeStatus(document.body.classList.contains('dark-mode'));

        // Update the dark mode switch state on the profile page
        if (profileDarkModeSwitch) {
            profileDarkModeSwitch.checked = !isProfileDarkMode; // Toggle the switch
        }
    }

    // Get the dark mode switch for the profile page and store it in a variable
    const profileDarkModeSwitch = document.getElementById('profileDarkModeSwitch');

    // Add event listener to the dark mode switch on the profile page
    if (profileDarkModeSwitch) {
        profileDarkModeSwitch.addEventListener('change', toggleProfileDarkMode);
    }

    // Add event listener to the global dark mode switch
    const globalDarkModeSwitch = document.getElementById('globalDarkModeSwitch');
    if (globalDarkModeSwitch) {
        globalDarkModeSwitch.addEventListener('change', toggleGlobalDarkMode);
    }

    // Function to toggle global dark mode
    function toggleGlobalDarkMode() {
        const isGlobalDarkMode = document.body.classList.contains('dark-mode'); // Check if the whole site is in dark mode
        document.body.classList.toggle('dark-mode'); // Toggle dark mode
        setTheme(); // Set theme based on the current dark mode setting

        // Save user's preference to local storage
        localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));

        // Save the dark mode status to the backend
        saveDarkModeStatus(document.body.classList.contains('dark-mode'));

        // Update the dark mode switch state on the profile page
        if (profileDarkModeSwitch) {
            profileDarkModeSwitch.checked = !isGlobalDarkMode; // Toggle the switch
        }
    }

    // Function to set the initial theme based on user preference stored in local storage
    function setInitialTheme() {
        const isDarkModeEnabled = JSON.parse(localStorage.getItem('darkMode'));
        if (isDarkModeEnabled) {
            document.body.classList.add('dark-mode');
        } else {
            document.body.classList.remove('dark-mode');
        }
        setTheme();
    }

    // Call the function to set the initial theme
    setInitialTheme();

    console.log("Amogh is here")
    // Check if the current page is the profile page
    if (window.location.pathname === '/profile') {
        // Call the function to check and update the dark mode status only when on the profile page
        checkDarkModeStatus();
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

