// document.addEventListener("DOMContentLoaded", function () {
    

//     // Function to fetch dark mode status from the backend
//     function fetchDarkModeStatus() {
//         const userId = 'user1' //getUserId(); // Replace this with a function to get the user's ID
//         fetch(`/api/dark_mode?user_id=${userId}`)
//             .then(response => response.json())
//             .then(data => {
//                 if (data.status) {
//                     // Set the dark mode based on the retrieved status
//                     document.body.classList.toggle('dark-mode', data.status);
//                     setTheme();
//                     // Update the dark mode switch state on the profile page
//                     if (profileDarkModeSwitch) {
//                         profileDarkModeSwitch.checked = data.status;
//                     }
//                 }
//             })
//             .catch(error => console.error('Error fetching dark mode status:', error));
//     }

//     // Function to update dark mode status via API
//     function updateDarkModeStatus(status) {
//         const userId = 'user1' //getUserId(); // Replace this with a function to get the user's ID
//         fetch('/api/dark_mode', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({ user_id: userId, status }),
//         })
//             .then(response => response.json())
//             .then(data => {
//                 console.log(data.message);
//             })
//             .catch(error => console.error('Error updating dark mode status:', error));
//     }

//     // Fetch the dark mode status when the profile page loads
//     fetchDarkModeStatus();

//     // ... (the rest of your code)

//     // Update the dark mode status and API when the switch changes
//     if (profileDarkModeSwitch) {
//         profileDarkModeSwitch.addEventListener('change', function () {
//             const status = this.checked;
//             toggleProfileDarkMode();
//             updateDarkModeStatus(status);
//         });
//     }
// });



