import datetime
from dateutil.relativedelta import relativedelta

"""py -m pip install python-dateutil ,install in cmd"""
# Current date and time
now = datetime.datetime.now()
print("Present Date & Time:", now.strftime("%d/%m/%Y %I:%M:%S %p"))

# Add days
print("After adding 10 days:", (now + datetime.timedelta(days=10)).strftime("%d/%m/%Y %I:%M:%S %p"))

# Add months
print("After adding 2 months:", (now + relativedelta(months=2)).strftime("%d/%m/%Y %I:%M:%S %p"))

# Add years
print("After adding 1 year:", (now + relativedelta(years=1)).strftime("%d/%m/%Y %I:%M:%S %p"))

# Add hours
print("After adding 5 hours:", (now + datetime.timedelta(hours=5)).strftime("%d/%m/%Y %I:%M:%S %p"))

# Add minutes
print("After adding 30 minutes:", (now + datetime.timedelta(minutes=30)).strftime("%d/%m/%Y %I:%M:%S %p"))

# Add seconds
print("After adding 45 seconds:", (now + datetime.timedelta(seconds=45)).strftime("%d/%m/%Y %I:%M:%S %p"))

# Subtract days
print("15 days ago:", (now - datetime.timedelta(days=15)).strftime("%d/%m/%Y %I:%M:%S %p"))

# Subtract months
print("2 months ago:", (now - relativedelta(months=2)).strftime("%d/%m/%Y %I:%M:%S %p"))

# Subtract years
print("1 year ago:", (now - relativedelta(years=1)).strftime("%d/%m/%Y %I:%M:%S %p"))

# Subtract hours
print("5 hours ago:", (now - datetime.timedelta(hours=5)).strftime("%d/%m/%Y %I:%M:%S %p"))

# Subtract minutes
print("30 minutes ago:", (now - datetime.timedelta(minutes=30)).strftime("%d/%m/%Y %I:%M:%S %p"))

# Subtract seconds
print("45 seconds ago:", (now - datetime.timedelta(seconds=45)).strftime("%d/%m/%Y %I:%M:%S %p"))
