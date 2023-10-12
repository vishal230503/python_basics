import calendar

def print_calendar(year):
    print(calendar.calendar(year))

def print_month_calendar(year, month):
    print(calendar.monthcalendar(year, month))

def print_month(year, month):
    print(calendar.month(year, month))

def print_year_calendar(year):
    print(calendar.yearcalendar(year))

def print_weekday_names():
    print(calendar.day_name)

def print_weekday_numbers():
    print(calendar.day_abbr)

def print_weekday_number(year, month, day):
    print(calendar.weekday(year, month, day))

def print_isocalendar_date(year, month, day):
    print(calendar.ISOCalendar(year).toordinal(year, month, day))

def print_isocalendar_dates(year):
    for month in range(1, 13):
        for day in range(1, calendar.monthrange(year, month)[1] + 1):
            print(calendar.ISOCalendar(year).toordinal(year, month, day))

def print_month_name(month):
    print(calendar.month_name[month])

def print_month_abbreviation(month):
    print(calendar.month_abbr[month])

def print_days_in_month(year, month):
    print(calendar.monthrange(year, month)[1])

def print_days_in_year(year):
    print(calendar.isleap(year))

def print_all_month_names():
    print(calendar.month_name)

def print_all_month_abbreviations():
    print(calendar.month_abbr)

def print_all_weekday_names():
    print(calendar.day_name)

def print_all_weekday_abbreviations():
    print(calendar.day_abbr)

def print_all_calendar_constants():
    print("Month names: ", calendar.month_name)
    print("Month abbreviations: ", calendar.month_abbr)
    print("Weekday names: ", calendar.weekday)