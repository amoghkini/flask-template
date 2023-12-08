document.addEventListener("DOMContentLoaded", function () {
    fetch('/api/heatmap_data') // Fetch data from Flask endpoint
        .then(response => response.json())
        .then(data => {
            const counts = data.date_counts.map(dateCount => dateCount.count);
            const minCount = Math.min(...counts);
            const maxCount = Math.max(...counts);

            const weeksData = groupDataByWeek(data.date_counts);
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
                        cell.style.backgroundColor = getColorForCount(weekData[i].count, minCount, maxCount);
                        cell.addEventListener('mouseenter', () => displayValueAndDate(cell, weekData[i].count, weekData[i].date));
                    }
                    cell.addEventListener('mouseleave', () => hideValueAndDate());
                    weekColumn.appendChild(cell);
                }

                document.querySelector('.heatmap-container').appendChild(weekColumn);
            });


        })
        .catch(error => console.error('Error:', error));

    function getColorForCount(count, minCount, maxCount) {
        const colors = ['#ebedf0', '#c6e48b', '#7bc96f', '#239a3b', '#196127'];
        const range = maxCount - minCount;
        const step = Math.ceil(range / colors.length);
        const thresholds = Array.from({ length: colors.length - 1 }, (_, i) => minCount + step * (i + 1));

        if (count === 0) return colors[0]; // Lowest count
        for (let i = 0; i < thresholds.length; i++) {
            if (count <= thresholds[i]) {
                return colors[i + 1];
            }
        }
        return colors[colors.length - 1]; // Highest count
    }

    function displayValueAndDate(cell, count, date) {
        const tooltip = document.createElement('div');
        tooltip.classList.add('heatmap-tooltip');
        tooltip.textContent = `Date: ${date}, Count: ${count}`;
        cell.appendChild(tooltip);
    }

    function hideValueAndDate() {
        const tooltips = document.querySelectorAll('.heatmap-tooltip');
        tooltips.forEach(tooltip => tooltip.remove());
    }

    function groupDataByWeek(data) {
        const weeksData = [];
        let currentWeek = [];
        data.forEach(dateCount => {
            const dayOfWeek = new Date(dateCount.date).getDay();
            if (dayOfWeek === 0 && currentWeek.length > 0) {
                while (currentWeek.length < 7) {
                    currentWeek.push({ date: '', count: 0 });
                }
                weeksData.push(currentWeek);
                currentWeek = [];
            }
            currentWeek.push(dateCount);
        });
        if (currentWeek.length > 0) {
            while (currentWeek.length < 7) {
                currentWeek.push({ date: '', count: 0 });
            }
            weeksData.push(currentWeek);
        }
        return weeksData;
    }
});