from datetime import datetime

class TimeUtils:
    
    DATE_FORMAT = "%Y-%m-%d"
    TIME_FORMAT = "%H:%M:%S"
    DATE_TIME_FORMAT = "%Y-%m-%d--%H-%M-%S"
    
    @staticmethod
    def get_time_of_day(hours, minutes, seconds, date_time_obj=None):
        if date_time_obj == None:
            date_time_obj = datetime.now()
        date_time_obj = date_time_obj.replace(hour=hours, minute=minutes, second=seconds, microsecond=0)
        return date_time_obj

    @staticmethod
    def get_time_of_today(hours, minutes, seconds):
        return TimeUtils.get_time_of_day(hours, minutes, seconds, datetime.now())

    @staticmethod
    def get_today_date_str(time=False):
        if time == True:
            return TimeUtils.convert_to_date_time_str(datetime.now())
        else:
            return TimeUtils.convert_to_date_str(datetime.now())

    @staticmethod
    def convert_to_date_str(datetime_obj):
        return datetime_obj.strftime(TimeUtils.DATE_FORMAT)
    
    @staticmethod
    def convert_to_date_time_str(datetime_obj):
        return datetime_obj.strftime(TimeUtils.DATE_TIME_FORMAT)