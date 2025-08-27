from datetime import date
def calculate_days_between_dates(start_date_tuple, end_date_tuple):
    start_date = date(start_date_tuple[0], start_date_tuple[1], start_date_tuple[2])
    end_date = date(end_date_tuple[0], end_date_tuple[1], end_date_tuple[2])

    time_difference = end_date - start_date

    return time_difference.days

date1 = (2014, 7, 2)
date2 = (2014, 7, 11)

number_of_days = calculate_days_between_dates(date1, date2)

print(f"{number_of_days} days")
