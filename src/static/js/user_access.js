function fetchUserRoleAndShowMenus() {
    // Check local storage for user role
    const userRole = localStorage.getItem('userRole');
    console.log(userRole)
    if (userRole) {
        // Use the role from local storage for UI changes
        showHideMenus(userRole);
    } else {
        // Fetch user role from the backend
        fetch('/api/user/role')
            .then(response => response.json())
            .then(data => {
                const { role } = data;
                if (role) {
                    localStorage.setItem('userRole', role); // Store the role in local storage
                    showHideMenus(role);
                }
            })
            .catch(error => {
                console.error('Error fetching user role:', error);
            });
    }
}

// Function to show/hide menus based on user role
function showHideMenus(role) {
    if (role === 'admin') {
        $('#adminMenu').show();
        $('#nav1').show();
        $('#nav2').show();
        // ... Show/hide other elements as needed
    } else if (role === 'user1') {
        $('#adminMenu').hide();
        $('#nav1').hide();
        $('#nav2').hide();
        // ... Show/hide other elements as needed
    }
    // Add conditions for other roles
}

// Update user role (example function)
function updateUserRole(role) {
    fetch('/api/user/role', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ role }),
    })
        .then(response => response.json())
        .then(data => {
            if (data.message === 'User role updated successfully') {
                localStorage.setItem('userRole', role); // Update role in local storage
                showHideMenus(role); // Update UI based on the new role
            }
        })
        .catch(error => {
            console.error('Error updating user role:', error);
        });
}

// Example usage of updateUserRole function:
// updateUserRole('admin'); // Use this to change the role

// Call this function when the page loads
document.addEventListener('DOMContentLoaded', function () {
    fetchUserRoleAndShowMenus();
});
