def days_since_birthday(birthday):

    day, month, year = map(int, birthday.split('-'))
    CURRENT_YEAR = 2024
    full_years = CURRENT_YEAR - year - 1
    days = full_years * 365

    return days

# Example of my birthday

birthday = "24-04-2003"

print(days_since_birthday(birthday))


