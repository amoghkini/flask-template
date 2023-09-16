document.addEventListener("DOMContentLoaded", function () {
    const notificationIcon = document.getElementById('notificationIcon');
    const notificationBadge = document.querySelector('.notification-badge');

    // Function to update the notification badge
    function updateNotificationBadge() {
        // Make an AJAX request to get unread notifications
        fetch('/get_notifications')
            .then(response => response.json())
            .then(data => {
                const unreadNotifications = data.notifications;
                const count = unreadNotifications.length;

                // Update the badge and mark all notifications as read when the icon is clicked
                if (count > 0) {
                    notificationBadge.textContent = count;
                    // notificationBadge.style.display = 'block';
                } else {
                    notificationBadge.style.display = 'none';
                }

                notificationIcon.addEventListener('click', function () {
                    // Make an AJAX request to mark notifications as read
                    fetch('/mark_notifications_as_read')
                        .then(response => response.json())
                        .then(() => {
                            notificationBadge.style.display = 'none';
                            // You can display a dropdown/pop-up with unread notifications here
                        });
                });
            });
    }

    // Update the notification badge on page load
    updateNotificationBadge();
});