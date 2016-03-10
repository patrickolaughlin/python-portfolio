# meetings.py
"""meetings.py
Timezone converter for entered time
uses timezones in OTHER_TIMEZONE."""


from datetime import datetime

import pytz

OTHER_TIMEZONES = [
    pytz.timezone('US/Eastern'),
    pytz.timezone('Pacific/Auckland'),
    pytz.timezone('Asia/Calcutta'),
    pytz.timezone('UTC'),
    pytz.timezone('Europe/Paris'),
    pytz.timezone('Africa/Khartoum')
]
fmt = '%Y-%m-%d %H:%M:%S %Z%z'

while True:
    date_input = input("When is your meeting? Please use MM/DD/YYYY HH:MM format. ")
    try:
        local_date = datetime.strptime(date_input, '%m/%d/%Y %H:%M')
    except ValueError:
        print("{} doesn't seem to be a valid date and time.".format(date_input))
    else:
        # this else is here for when try doesn't blow up
        local_date = pytz.timezone('US/Central').localize(local_date)
        # have this match your local timezone
        utc_date = local_date.astimezone(pytz.utc)

        print("Your meeting time in other timezones: ")
        output = []
        for timezone in OTHER_TIMEZONES:
            output.append(utc_date.astimezone(timezone))
        for appointment in output:
            print(appointment.strftime(fmt))
        break
    
