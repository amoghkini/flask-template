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

    // Check if the current page is the profile page
    if (window.location.pathname === '/profile' || window.location.pathname === '/') {
        // Call the function to check and update the dark mode status when on the profile page or the root URL
        checkDarkModeStatus();
    }


});

