nic = str(200418601010)

monthAndDate = int(nic[4:7])
year = int(nic[:4])
# print(year)

# Leap year check
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Initialize day and month
day_of_year = monthAndDate

if day_of_year <= 31:
    month = 'January'
    day = day_of_year
elif day_of_year <= 60:
    month = 'February'
    day = day_of_year - 31
    if is_leap_year:
        if day_of_year == 60:
            month = 'February'
            day = 29
else:
    if not is_leap_year:
        day_of_year -= 1  # Adjust for non-leap years
    if day_of_year <= 90:
        month = 'March'
        day = day_of_year - 60
    elif day_of_year <= 120:
        month = 'April'
        day = day_of_year - 91
    elif day_of_year <= 151:
        month = 'May'
        day = day_of_year - 121
    elif day_of_year <= 181:
        month = 'June'
        day = day_of_year - 152
    elif day_of_year <= 212:
        month = 'July'
        day = day_of_year - 182
    elif day_of_year <= 243:
        month = 'August'
        day = day_of_year - 213
    elif day_of_year <= 273:
        month = 'September'
        day = day_of_year - 244
    elif day_of_year <= 304:
        month = 'October'
        day = day_of_year - 274
    elif day_of_year <= 334:
        month = 'November'
        day = day_of_year - 305
    elif day_of_year <= 365:
        month = 'December'
        day = day_of_year - 335

print(f"Year: {year}, Month: {month}, Day: {day}")
