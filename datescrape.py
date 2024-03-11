from datetime import datetime, timedelta

def generate_date_list(start_date, end_date):
    # Convert start_date and end_date strings to datetime objects
    start_date_obj = datetime.strptime(start_date, "%m-%Y")
    end_date_obj = datetime.strptime(end_date, "%m-%Y")

    # Initialize an empty list to store the generated dates
    date_list = []

    # Iterate through the range of dates and generate the list
    current_date = start_date_obj
    while current_date <= end_date_obj:
        # Append the current date to the list in the format "MM-YYYY"
        date_list.append(current_date.strftime("%m-%Y"))

        # Move to the next month
        current_date = current_date + timedelta(days=32)
        current_date = current_date.replace(day=1)

    return date_list

# Test the function with example input
#   start_date = '01-2012'
#   end_date = '04-2012'
#   dates = generate_date_list(start_date, end_date)
#   print("dates =", dates)