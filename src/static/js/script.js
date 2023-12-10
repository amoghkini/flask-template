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

        section1Button.addEventListener('click', function () {
            fetch(`/get_section_data?section=section1`)
                .then(response => response.json())
                .then(data => {
                    displayDataInTable(data, 'section1');
                })
                .catch(error => {
                    console.error('Error fetching Section 1 data:', error);
                });
        });

        section2Button.addEventListener('click', function () {
            fetch(`/get_section_data?section=section2`)
                .then(response => response.json())
                .then(data => {
                    displayDataInTable(data, 'section2');
                })
                .catch(error => {
                    console.error('Error fetching Section 2 data:', error);
                });
        });

        section3Button.addEventListener('click', function () {
            fetch(`/get_section_data?section=section3`)
                .then(response => response.json())
                .then(data => {
                    displayDataInTable(data, 'section3');
                })
                .catch(error => {
                    console.error('Error fetching Section 3 data:', error);
                });
        });

        // Function to display data in a table
        function displayDataInTable(data, sectionId) {
            const sectionDiv = document.getElementById(sectionId);
            const allSections = document.querySelectorAll('[id^="section"]'); // Select all sections

            // Hide all sections except the clicked section
            allSections.forEach(section => {
                if (section.id !== sectionId) {
                    section.style.display = 'none';
                }
            });

            const table = createTable(data);
            sectionDiv.innerHTML = ''; // Clear existing content of the clicked section
            sectionDiv.appendChild(table);

            // Display the clicked section after creating the table
            sectionDiv.style.display = 'block';

            // Display all buttons again
            const buttons = document.querySelectorAll('button[id^="section"]');
            buttons.forEach(button => {
                button.style.display = 'inline-block';
            });
        }




        // Function to create an HTML table from JSON data
        function createTable(data) {
            const table = document.createElement('table');
            table.classList.add('section-table');

            // Create table header
            const header = table.createTHead();
            const headerRow = header.insertRow();
            for (let key in data[0]) {
                const th = document.createElement('th');
                th.textContent = key;
                headerRow.appendChild(th);
            }

            // Create table body
            const body = table.createTBody();
            data.forEach(item => {
                const row = body.insertRow();
                for (let key in item) {
                    const cell = row.insertCell();
                    cell.textContent = item[key];
                }
            });

            return table;
        }


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
