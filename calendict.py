import calendar

def last_day_of_month(year, month):
    return calendar.monthrange(year, month)[1]

def generate_last_day_dictionary(start_year, end_year):
    last_day_dict = {}
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            key = f"{month:02d}-{year}"
            value = last_day_of_month(year, month)
            last_day_dict[key] = value
    return last_day_dict