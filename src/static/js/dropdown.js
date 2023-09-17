document.addEventListener("DOMContentLoaded", function () {
    // Get all elements with the class "dynamic-dropdown"
    const dropdowns = document.querySelectorAll('.dynamic-dropdown');

    // Iterate over each dropdown
    dropdowns.forEach(dropdown => {
        // Get the page name from the data attribute
        const page = dropdown.getAttribute('data-page');

        // Fetch data from your Flask route with the page parameter
        fetch(`/get_dropdown_data/${page}`)
            .then(response => response.json())
            .then(data => {
                // Iterate over the data and create <option> elements
                data.forEach(optionText => {
                    const option = document.createElement('option');
                    option.value = optionText;
                    option.textContent = optionText;
                    dropdown.appendChild(option);
                });
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    });
});
