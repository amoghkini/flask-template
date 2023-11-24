document.addEventListener("DOMContentLoaded", function () {
    
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


// Function to clear local storage upon logout
function clearLocalStorageOnLogout() {
    console.log("About to remove data from localStorage")
    // Clear the 'userRole' key from local storage
    localStorage.removeItem('userRole');
}

// Function to handle logout and redirection
function handleLogoutAndRedirect() {
    // Perform logout actions (e.g., API call)
    fetch('/logout')
        .then(response => response.json())
        .then(data => {
            if (data.message === 'Logged out successfully' && data.redirect_url) {
                clearLocalStorageOnLogout(); // Clear local storage upon successful logout
                window.location.href = data.redirect_url; // Redirect to the specified URL
            }
        })
        .catch(error => {
            console.error('Error logging out:', error);
        });
}

// Example usage: Call this function when the logout action is triggered
document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('logoutButton').addEventListener('click', function () {
        handleLogoutAndRedirect(); // Trigger logout and redirection
    });
});
