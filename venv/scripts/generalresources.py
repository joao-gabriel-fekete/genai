from datetime import datetime


def format_date_with_suffix(date):
    day = date.day
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]

    return date.strftime(f"%B {day}{suffix} %Y")

# Get the current date
now = datetime.now()

# Format the date
dateTimeString = format_date_with_suffix(now)

#dateTimeString = datetime.now().strftime("%A, %d/%m/%Y %H:%M")
