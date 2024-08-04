nic = str(200361613060)

day_of_year = int(nic[4:7])
year = int(nic[:4])

# Leap year check
is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
day_of_year -= 1

if day_of_year >= 500:
    day_of_year -= 500

if day_of_year <= 31:
    month = 'January'
    day = day_of_year
elif is_leap_year and day_of_year <= 60:
    month = 'February'
    day = day_of_year - 31
elif not is_leap_year and day_of_year <= 59:
    month = 'February'
    day = day_of_year - 31
elif day_of_year <= 90:
    month = 'March'
    day = day_of_year - 59
elif day_of_year <= 120:
    month = 'April'
    day = day_of_year - 90
elif day_of_year <= 151:
    month = 'May'
    day = day_of_year - 120
elif day_of_year <= 181:
    month = 'June'
    day = day_of_year - 151
elif day_of_year <= 212:
    month = 'July'
    day = day_of_year - 181
elif day_of_year <= 242:
    month = 'August'
    day = day_of_year - 212
elif day_of_year <= 273:
    month = 'September'
    day = day_of_year - 242
elif day_of_year <= 303:
    month = 'October'
    day = day_of_year - 273
elif day_of_year <= 334:
    month = 'November'
    day = day_of_year - 303
elif day_of_year <= 364:
    month = 'December'
    day = day_of_year - 334
else:
    # Handle cases where day_of_year exceeds expected ranges
    month = 'Unknown'
    day = day_of_year

print(year, month, day)
