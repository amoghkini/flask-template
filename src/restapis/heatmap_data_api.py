from flask import jsonify, request
from flask.views import MethodView
from datetime import datetime, timedelta

class HeatmapDataAPI(MethodView):

    def get(self):
        # Simulated time series data (replace this with your database query)
        time_series_data = [{'date': '2023-01-01', 'value': 0}, {'date': '2023-01-02', 'value': 15}, {'date': '2023-01-03', 'value': 14}, {'date': '2023-01-04', 'value': 45}, {'date': '2023-01-05', 'value': 47}, {'date': '2023-01-06', 'value': 1}, {'date': '2023-01-07', 'value': 0}, {'date': '2023-01-08', 'value': 0}, {'date': '2023-01-09', 'value': 41}, {'date': '2023-01-10', 'value': 43}, {'date': '2023-01-11', 'value': 23}, {'date': '2023-01-12', 'value': 18}, {'date': '2023-01-13', 'value': 41}, {'date': '2023-01-14', 'value': 0}, {'date': '2023-01-15', 'value': 0}, {'date': '2023-01-16', 'value': 19}, {'date': '2023-01-17', 'value': 42}, {'date': '2023-01-18', 'value': 21}, {'date': '2023-01-19', 'value': 28}, {'date': '2023-01-20', 'value': 24}, {'date': '2023-01-21', 'value': 0}, {'date': '2023-01-22', 'value': 0}, {'date': '2023-01-23', 'value': 47}, {'date': '2023-01-24', 'value': 43}, {'date': '2023-01-25', 'value': 25}, {'date': '2023-01-26', 'value': 39}, {'date': '2023-01-27', 'value': 37}, {'date': '2023-01-28', 'value': 0}, {'date': '2023-01-29', 'value': 0}, {'date': '2023-01-30', 'value': 18}, {'date': '2023-01-31', 'value': 2}, {'date': '2023-02-01', 'value': 34}, {'date': '2023-02-02', 'value': 9}, {'date': '2023-02-03', 'value': 36}, {'date': '2023-02-04', 'value': 0}, {'date': '2023-02-05', 'value': 0}, {'date': '2023-02-06', 'value': 21}, {'date': '2023-02-07', 'value': 33}, {'date': '2023-02-08', 'value': 20}, {'date': '2023-02-09', 'value': 46}, {'date': '2023-02-10', 'value': 32}, {'date': '2023-02-11', 'value': 0}, {'date': '2023-02-12', 'value': 0}, {'date': '2023-02-13', 'value': 19}, {'date': '2023-02-14', 'value': 47}, {'date': '2023-02-15', 'value': 47}, {'date': '2023-02-16', 'value': 50}, {'date': '2023-02-17', 'value': 9}, {'date': '2023-02-18', 'value': 0}, {'date': '2023-02-19', 'value': 0}, {'date': '2023-02-20', 'value': 1}, {'date': '2023-02-21', 'value': 29}, {'date': '2023-02-22', 'value': 19}, {'date': '2023-02-23', 'value': 17}, {'date': '2023-02-24', 'value': 27}, {'date': '2023-02-25', 'value': 0}, {'date': '2023-02-26', 'value': 0}, {'date': '2023-02-27', 'value': 33}, {'date': '2023-02-28', 'value': 27}, {'date': '2023-03-01', 'value': 10}, {'date': '2023-03-02', 'value': 30}, {'date': '2023-03-03', 'value': 8}, {'date': '2023-03-04', 'value': 0}, {'date': '2023-03-05', 'value': 0}, {'date': '2023-03-06', 'value': 13}, {'date': '2023-03-07', 'value': 49}, {'date': '2023-03-08', 'value': 25}, {'date': '2023-03-09', 'value': 32}, {'date': '2023-03-10', 'value': 36}, {'date': '2023-03-11', 'value': 0}, {'date': '2023-03-12', 'value': 0}, {'date': '2023-03-13', 'value': 23}, {'date': '2023-03-14', 'value': 25}, {'date': '2023-03-15', 'value': 46}, {'date': '2023-03-16', 'value': 5}, {'date': '2023-03-17', 'value': 12}, {'date': '2023-03-18', 'value': 0}, {'date': '2023-03-19', 'value': 0}, {'date': '2023-03-20', 'value': 12}, {'date': '2023-03-21', 'value': 24}, {'date': '2023-03-22', 'value': 9}, {'date': '2023-03-23', 'value': 42}, {'date': '2023-03-24', 'value': 41}, {'date': '2023-03-25', 'value': 0}, {'date': '2023-03-26', 'value': 0}, {'date': '2023-03-27', 'value': 35}, {'date': '2023-03-28', 'value': 4}, {'date': '2023-03-29', 'value': 46}, {'date': '2023-03-30', 'value': 12}, {'date': '2023-03-31', 'value': 35}, {'date': '2023-04-01', 'value': 0}, {'date': '2023-04-02', 'value': 0}, {'date': '2023-04-03', 'value': 16}, {'date': '2023-04-04', 'value': 32}, {'date': '2023-04-05', 'value': 23}, {'date': '2023-04-06', 'value': 5}, {'date': '2023-04-07', 'value': 46}, {'date': '2023-04-08', 'value': 0}, {'date': '2023-04-09', 'value': 0}, {'date': '2023-04-10', 'value': 21}, {'date': '2023-04-11', 'value': 45}, {'date': '2023-04-12', 'value': 32}, {'date': '2023-04-13', 'value': 4}, {'date': '2023-04-14', 'value': 9}, {'date': '2023-04-15', 'value': 0}, {'date': '2023-04-16', 'value': 0}, {'date': '2023-04-17', 'value': 30}, {'date': '2023-04-18', 'value': 21}, {'date': '2023-04-19', 'value': 23}, {'date': '2023-04-20', 'value': 42}, {'date': '2023-04-21', 'value': 37}, {'date': '2023-04-22', 'value': 0}, {'date': '2023-04-23', 'value': 0}, {'date': '2023-04-24', 'value': 45}, {'date': '2023-04-25', 'value': 16}, {'date': '2023-04-26', 'value': 45}, {'date': '2023-04-27', 'value': 29}, {'date': '2023-04-28', 'value': 14}, {'date': '2023-04-29', 'value': 0}, {'date': '2023-04-30', 'value': 0}, {'date': '2023-05-01', 'value': 25}, {'date': '2023-05-02', 'value': 8}, {'date': '2023-05-03', 'value': 22}, {'date': '2023-05-04', 'value': 9}, {'date': '2023-05-05', 'value': 4}, {'date': '2023-05-06', 'value': 0}, {'date': '2023-05-07', 'value': 0}, {'date': '2023-05-08', 'value': 9}, {'date': '2023-05-09', 'value': 18}, {'date': '2023-05-10', 'value': 37}, {'date': '2023-05-11', 'value': 44}, {'date': '2023-05-12', 'value': 20}, {'date': '2023-05-13', 'value': 0}, {'date': '2023-05-14', 'value': 0}, {'date': '2023-05-15', 'value': 26}, {'date': '2023-05-16', 'value': 10}, {'date': '2023-05-17', 'value': 13}, {'date': '2023-05-18', 'value': 0}, {'date': '2023-05-19', 'value': 10}, {'date': '2023-05-20', 'value': 0}, {'date': '2023-05-21', 'value': 0}, {'date': '2023-05-22', 'value': 6}, {'date': '2023-05-23', 'value': 28}, {'date': '2023-05-24', 'value': 31}, {'date': '2023-05-25', 'value': 24}, {'date': '2023-05-26', 'value': 1}, {'date': '2023-05-27', 'value': 0}, {'date': '2023-05-28', 'value': 0}, {'date': '2023-05-29', 'value': 8}, {'date': '2023-05-30', 'value': 43}, {'date': '2023-05-31', 'value': 31}, {'date': '2023-06-01', 'value': 25}, {'date': '2023-06-02', 'value': 22}, {'date': '2023-06-03', 'value': 0}, {'date': '2023-06-04', 'value': 0}, {'date': '2023-06-05', 'value': 19}, {'date': '2023-06-06', 'value': 4}, {'date': '2023-06-07', 'value': 14}, {'date': '2023-06-08', 'value': 33}, {'date': '2023-06-09', 'value': 29}, {'date': '2023-06-10', 'value': 0}, {'date': '2023-06-11', 'value': 0}, {'date': '2023-06-12', 'value': 21}, {'date': '2023-06-13', 'value': 4}, {'date': '2023-06-14', 'value': 17}, {'date': '2023-06-15', 'value': 35}, {'date': '2023-06-16', 'value': 42}, {'date': '2023-06-17', 'value': 0}, {'date': '2023-06-18', 'value': 0}, {'date': '2023-06-19', 'value': 38}, {'date': '2023-06-20', 'value': 39}, {'date': '2023-06-21', 'value': 41}, {'date': '2023-06-22', 'value': 11}, {'date': '2023-06-23', 'value': 33}, {'date': '2023-06-24', 'value': 0}, {'date': '2023-06-25', 'value': 0}, {'date': '2023-06-26', 'value': 11}, {'date': '2023-06-27', 'value': 47}, {'date': '2023-06-28', 'value': 1}, {'date': '2023-06-29', 'value': 2}, {'date': '2023-06-30', 'value': 7}, {'date': '2023-07-01', 'value': 0}, {'date': '2023-07-02', 'value': 0}, {'date': '2023-07-03', 'value': 26}, {'date': '2023-07-04', 'value': 21}, {'date': '2023-07-05', 'value': 0}, {'date': '2023-07-06', 'value': 35}, {'date': '2023-07-07', 'value': 26}, {'date': '2023-07-08', 'value': 0}, {'date': '2023-07-09', 'value': 0}, {'date': '2023-07-10', 'value': 46}, {'date': '2023-07-11', 'value': 10}, {'date': '2023-07-12', 'value': 8}, {'date': '2023-07-13', 'value': 9}, {'date': '2023-07-14', 'value': 48}, {'date': '2023-07-15', 'value': 0}, {'date': '2023-07-16', 'value': 0}, {'date': '2023-07-17', 'value': 14}, {'date': '2023-07-18', 'value': 11}, {'date': '2023-07-19', 'value': 14}, {'date': '2023-07-20', 'value': 44}, {'date': '2023-07-21', 'value': 35}, {'date': '2023-07-22', 'value': 0}, {'date': '2023-07-23', 'value': 0}, {'date': '2023-07-24', 'value': 40}, {'date': '2023-07-25', 'value': 49}, {'date': '2023-07-26', 'value': 23}, {'date': '2023-07-27', 'value': 24}, {'date': '2023-07-28', 'value': 34}, {'date': '2023-07-29', 'value': 0}, {'date': '2023-07-30', 'value': 0}, {'date': '2023-07-31', 'value': 11}, {'date': '2023-08-01', 'value': 28}, {'date': '2023-08-02', 'value': 18}, {'date': '2023-08-03', 'value': 21}, {'date': '2023-08-04', 'value': 1}, {'date': '2023-08-05', 'value': 0}, {'date': '2023-08-06', 'value': 0}, {'date': '2023-08-07', 'value': 30}, {'date': '2023-08-08', 'value': 7}, {'date': '2023-08-09', 'value': 30}, {'date': '2023-08-10', 'value': 28}, {'date': '2023-08-11', 'value': 38}, {'date': '2023-08-12', 'value': 0}, {'date': '2023-08-13', 'value': 0}, {'date': '2023-08-14', 'value': 35}, {'date': '2023-08-15', 'value': 41}, {'date': '2023-08-16', 'value': 31}, {'date': '2023-08-17', 'value': 49}, {'date': '2023-08-18', 'value': 5}, {'date': '2023-08-19', 'value': 0}, {'date': '2023-08-20', 'value': 0}, {'date': '2023-08-21', 'value': 19}, {'date': '2023-08-22', 'value': 3}, {'date': '2023-08-23', 'value': 38}, {'date': '2023-08-24', 'value': 25}, {'date': '2023-08-25', 'value': 37}, {'date': '2023-08-26', 'value': 0}, {'date': '2023-08-27', 'value': 0}, {'date': '2023-08-28', 'value': 37}, {'date': '2023-08-29', 'value': 29}, {'date': '2023-08-30', 'value': 50}, {'date': '2023-08-31', 'value': 40}, {'date': '2023-09-01', 'value': 15}, {'date': '2023-09-02', 'value': 0}, {'date': '2023-09-03', 'value': 0}, {'date': '2023-09-04', 'value': 15}, {'date': '2023-09-05', 'value': 10}, {'date': '2023-09-06', 'value': 34}, {'date': '2023-09-07', 'value': 32}, {'date': '2023-09-08', 'value': 9}, {'date': '2023-09-09', 'value': 0}, {'date': '2023-09-10', 'value': 0}, {'date': '2023-09-11', 'value': 45}, {'date': '2023-09-12', 'value': 43}, {'date': '2023-09-13', 'value': 10}, {'date': '2023-09-14', 'value': 18}, {'date': '2023-09-15', 'value': 8}, {'date': '2023-09-16', 'value': 0}, {'date': '2023-09-17', 'value': 0}, {'date': '2023-09-18', 'value': 20}, {'date': '2023-09-19', 'value': 10}, {'date': '2023-09-20', 'value': 8}, {'date': '2023-09-21', 'value': 45}, {'date': '2023-09-22', 'value': 37}, {'date': '2023-09-23', 'value': 0}, {'date': '2023-09-24', 'value': 0}, {'date': '2023-09-25', 'value': 27}, {'date': '2023-09-26', 'value': 29}, {'date': '2023-09-27', 'value': 14}, {'date': '2023-09-28', 'value': 33}, {'date': '2023-09-29', 'value': 31}, {'date': '2023-09-30', 'value': 0}, {'date': '2023-10-01', 'value': 0}, {'date': '2023-10-02', 'value': 21}, {'date': '2023-10-03', 'value': 44}, {'date': '2023-10-04', 'value': 18}, {'date': '2023-10-05', 'value': 22}, {'date': '2023-10-06', 'value': 7}, {'date': '2023-10-07', 'value': 0}, {'date': '2023-10-08', 'value': 0}, {'date': '2023-10-09', 'value': 20}, {'date': '2023-10-10', 'value': 27}, {'date': '2023-10-11', 'value': 23}, {'date': '2023-10-12', 'value': 31}, {'date': '2023-10-13', 'value': 6}, {'date': '2023-10-14', 'value': 0}, {'date': '2023-10-15', 'value': 0}, {'date': '2023-10-16', 'value': 21}, {'date': '2023-10-17', 'value': 4}, {'date': '2023-10-18', 'value': 37}, {'date': '2023-10-19', 'value': 10}, {'date': '2023-10-20', 'value': 10}, {'date': '2023-10-21', 'value': 0}, {'date': '2023-10-22', 'value': 0}, {'date': '2023-10-23', 'value': 12}, {'date': '2023-10-24', 'value': 36}, {'date': '2023-10-25', 'value': 20}, {'date': '2023-10-26', 'value': 22}, {'date': '2023-10-27', 'value': 26}, {'date': '2023-10-28', 'value': 0}, {'date': '2023-10-29', 'value': 0}, {'date': '2023-10-30', 'value': 33}, {'date': '2023-10-31', 'value': 46}, {'date': '2023-11-01', 'value': 3}, {'date': '2023-11-02', 'value': 13}, {'date': '2023-11-03', 'value': 35}, {'date': '2023-11-04', 'value': 0}, {'date': '2023-11-05', 'value': 0}, {'date': '2023-11-06', 'value': 45}, {'date': '2023-11-07', 'value': 8}, {'date': '2023-11-08', 'value': 4}, {'date': '2023-11-09', 'value': 22}, {'date': '2023-11-10', 'value': 43}, {'date': '2023-11-11', 'value': 0}, {'date': '2023-11-12', 'value': 0}, {'date': '2023-11-13', 'value': 49}, {'date': '2023-11-14', 'value': 1}, {'date': '2023-11-15', 'value': 47}, {'date': '2023-11-16', 'value': 0}, {'date': '2023-11-17', 'value': 8}, {'date': '2023-11-18', 'value': 0}, {'date': '2023-11-19', 'value': 0}, {'date': '2023-11-20', 'value': 37}, {'date': '2023-11-21', 'value': 20}, {'date': '2023-11-22', 'value': 1}, {'date': '2023-11-23', 'value': 21}, {'date': '2023-11-24', 'value': 2}, {'date': '2023-11-25', 'value': 0}, {'date': '2023-11-26', 'value': 0}, {'date': '2023-11-27', 'value': 29}, {'date': '2023-11-28', 'value': 33}, {'date': '2023-11-29', 'value': 38}, {'date': '2023-11-30', 'value': 45}, {'date': '2023-12-01', 'value': 47}, {'date': '2023-12-02', 'value': 0}, {'date': '2023-12-03', 'value': 0}, {'date': '2023-12-04', 'value': 49}, {'date': '2023-12-05', 'value': 2}, {'date': '2023-12-06', 'value': 16}, {'date': '2023-12-07', 'value': 37}, {'date': '2023-12-08', 'value': 26}, {'date': '2023-12-09', 'value': 0}, {'date': '2023-12-10', 'value': 0}, {'date': '2023-12-11', 'value': 12}, {'date': '2023-12-12', 'value': 13}, {'date': '2023-12-13', 'value': 2}, {'date': '2023-12-14', 'value': 7}, {'date': '2023-12-15', 'value': 3}, {'date': '2023-12-16', 'value': 0}, {'date': '2023-12-17', 'value': 0}, {'date': '2023-12-18', 'value': 27}, {'date': '2023-12-19', 'value': 44}, {'date': '2023-12-20', 'value': 50}, {'date': '2023-12-21', 'value': 33}, {'date': '2023-12-22', 'value': 5}, {'date': '2023-12-23', 'value': 0}, {'date': '2023-12-24', 'value': 0}, {'date': '2023-12-25', 'value': 35}, {'date': '2023-12-26', 'value': 31}, {'date': '2023-12-27', 'value': 39}, {'date': '2023-12-28', 'value': -4}, {'date': '2023-12-29', 'value': 9}, {'date': '2023-12-30', 'value': 0}, {'date': '2023-12-31', 'value': 0}]

        start_date = request.args.get('startDate')
        end_date = request.args.get('endDate')

        # Convert start_date and end_date to datetime objects for comparison
        start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
        end_datetime = datetime.strptime(end_date, '%Y-%m-%d')

        # Calculate the difference in days
        date_difference = (end_datetime - start_datetime).days
        import time;time.sleep(2)
        if date_difference > 400:
            return jsonify({'error': 'The difference between start and end dates cannot be more than 400 days.'})
        time_series_data = complete_weeks_in_data(time_series_data)
        return jsonify({'heatmap_data': time_series_data})


def complete_weeks_in_data(time_series_data):
    # Extracting dates from the data and converting them to datetime objects
    dates = [datetime.strptime(item['date'], '%Y-%m-%d') for item in time_series_data]

    # Finding the minimum and maximum dates from the list
    min_date = min(dates)
    max_date = max(dates)

    # Getting the day of the week for the minimum date (0 for Sunday, 1 for Monday, etc.)
    day_of_min_date = min_date.weekday()

    # Calculating the start date of the week based on the minimum date
    days_before_start = (day_of_min_date + 1) % 7  # Adjusting to start from Sunday (0)
    start_date_of_week = min_date - timedelta(days=days_before_start)

    # Creating data with value as 0 for all dates between start_date_of_week and min_date
    missing_data_start = [{'date': (start_date_of_week + timedelta(days=i)).strftime('%Y-%m-%d'), 'value': 0}
                          for i in range((min_date - start_date_of_week).days)]

    # Adding missing_data_start to the start of time_series_data list
    time_series_data = missing_data_start + time_series_data

    # Getting the day of the week for the maximum date (0 for Sunday, 1 for Monday, etc.)
    day_of_max_date = max_date.weekday()

    # Calculating the end date of the week based on the maximum date
    days_after_end = 6 - ((day_of_max_date + 1) % 7)  # Adjusting to end at Saturday (6)
    last_date_of_week = max_date + timedelta(days=days_after_end)

    # Creating data with value as 0 for all dates between max_date and last_date_of_week
    missing_data_end = [{'date': (max_date + timedelta(days=i + 1)).strftime('%Y-%m-%d'), 'value': 0}
                        for i in range((last_date_of_week - max_date).days)]

    # Adding missing_data_end to the end of time_series_data list
    time_series_data += missing_data_end

    return time_series_data
