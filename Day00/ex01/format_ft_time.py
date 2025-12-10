import datetime
import time


seconds = time.time()
date = datetime.datetime.now()


format_time = f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation"

# Days
# %d : Day of month (e.g., 21)
# %A : Full weekday name (e.g., Friday)

# Months
# %m : Month as a number (e.g., 10)
# %b : Month as abbreviated name (e.g., Oct)
# %B : Month as full name (e.g., October)

# Years
# %y : Short year (e.g., 22)
# %Y : Full year (e.g., 2022)
format_date = date.strftime("%b %d %Y")


print(format_time)
print(format_date)