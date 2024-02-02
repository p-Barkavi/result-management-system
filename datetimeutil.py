from datetime import datetime

def getcurrenttime():
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    print("Time now: " + formatted_date)

    return formatted_date
