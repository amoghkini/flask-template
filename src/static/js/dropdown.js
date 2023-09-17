document.addEventListener("DOMContentLoaded", function () {
    // Get a reference to the dropdown element
    const dropdown = document.getElementById('dropdown');

    // Check if the 'dropdown' element exists in the DOM
    if (dropdown) {
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
    }
});
