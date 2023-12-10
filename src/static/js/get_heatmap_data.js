document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById('heatmapForm');
    form.addEventListener('submit', function (event) {
        event.preventDefault();

        // Show the loading icon
        const loadingIcon = document.getElementById('loadingIcon');
        loadingIcon.style.display = 'block';

        // Clear existing heatmap before adding a new one
        const existingHeatmap = document.querySelector('.heatmap-container');
        if (existingHeatmap) {
            existingHeatmap.innerHTML = ''; // Clear the heatmap container
        }
        
        const formData = new FormData(form);
        const searchParams = new URLSearchParams(formData).toString();

        fetch(`/api/heatmap_data?${searchParams}`) // Fetch data from Flask endpoint
            .then(response => {
                if (!response.ok) {
                    throw new Error('The request failed');
                }
                return response.json();
            })
            .then(data => {
                loadingIcon.style.display = 'none';
                if (data.hasOwnProperty('error')) {
                    throw new Error(data.error);
                }

                const values = data.heatmap_data.map(datevalue => datevalue.value);
                const minvalue = Math.min(...values);
                const maxvalue = Math.max(...values);

                const weeksData = groupDataByWeek(data.heatmap_data);
                const maxRows = Math.max(...weeksData.map(weekData => weekData.length));

                const dayLabels = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
                const dayLabelsContainer = document.createElement('div');
                dayLabelsContainer.classList.add('day-labels');

                dayLabels.forEach(label => {
                    const dayLabel = document.createElement('div');
                    dayLabel.classList.add('day-label');
                    dayLabel.textContent = label;
                    dayLabelsContainer.appendChild(dayLabel);
                });

                document.querySelector('.heatmap-container').appendChild(dayLabelsContainer);


                weeksData.forEach(weekData => {
                    const weekColumn = document.createElement('div');
                    weekColumn.classList.add('heatmap-column');

                    for (let i = 0; i < maxRows; i++) {
                        const cell = document.createElement('div');
                        cell.classList.add('heatmap-cell');
                        if (i < weekData.length) {
                            cell.style.backgroundColor = getColorForvalue(weekData[i].value, minvalue, maxvalue);
                            cell.addEventListener('mouseenter', () => displayValueAndDate(cell, weekData[i].value, weekData[i].date));
                        }
                        cell.addEventListener('mouseleave', () => hideValueAndDate());
                        weekColumn.appendChild(cell);
                    }

                    document.querySelector('.heatmap-container').appendChild(weekColumn);
                });
            })
            .catch(error => {
                loadingIcon.style.display = 'none';
                alert(error.message); // Alert with the error message
                console.error('Error:', error);
            });

        function getColorForvalue(value, minvalue, maxvalue) {
            const colors = ['#ebedf0', '#c6e48b', '#7bc96f', '#239a3b', '#196127'];
            const range = maxvalue - minvalue;
            const step = Math.ceil(range / colors.length);
            const thresholds = Array.from({ length: colors.length - 1 }, (_, i) => minvalue + step * (i + 1));

            if (value === 0) return colors[0]; // Lowest value
            for (let i = 0; i < thresholds.length; i++) {
                if (value <= thresholds[i]) {
                    return colors[i + 1];
                }
            }
            return colors[colors.length - 1]; // Highest value
        }

        function displayValueAndDate(cell, value, date) {
            const tooltip = document.createElement('div');
            tooltip.classList.add('heatmap-tooltip');
            tooltip.textContent = `Date: ${date}, Value: ${value}`;

            // Calculate mouse position relative to the viewport
            const rect = cell.getBoundingClientRect();
            const mouseX = event.clientX - rect.left;
            const mouseY = event.clientY - rect.top;

            // Set tooltip position relative to the mouse position
            tooltip.style.left = mouseX + 'px';
            tooltip.style.top = mouseY + 'px';

            cell.appendChild(tooltip);
        }

        function hideValueAndDate() {
            const tooltips = document.querySelectorAll('.heatmap-tooltip');
            tooltips.forEach(tooltip => tooltip.remove());
        }

        function groupDataByWeek(data) {
            const weeksData = [];
            let currentWeek = [];
            data.forEach(datevalue => {
                const dayOfWeek = new Date(datevalue.date).getDay();
                if (dayOfWeek === 0 && currentWeek.length > 0) {
                    while (currentWeek.length < 7) {
                        currentWeek.push({ date: '', value: 0 });
                    }
                    weeksData.push(currentWeek);
                    currentWeek = [];
                }
                currentWeek.push(datevalue);
            });
            if (currentWeek.length > 0) {
                while (currentWeek.length < 7) {
                    currentWeek.push({ date: '', value: 0 });
                }
                weeksData.push(currentWeek);
            }
            return weeksData;
        }
    });

});