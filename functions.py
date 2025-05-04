hours_in_day = 24

def convert_to_hours(num_days):
    return(f"Number of hours in {num_days} days is {num_days * hours_in_day}")

hours = convert_to_hours(100)
print(hours)