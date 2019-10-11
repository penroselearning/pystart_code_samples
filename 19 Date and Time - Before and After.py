from datetime import datetime
from datetime import timedelta

today = datetime.now()

one_week_after_today = today + timedelta(days=7)
one_week_before_today = today - timedelta(days=7)

one_year_from_today = today + timedelta(days=365)
one_year_before_today = today - timedelta(days=365)

print(f'One Week After Today: {one_week_after_today}')
print(f'One Week Before Today: {one_week_before_today}')
print(f'One Year from Today: {one_year_from_today}')
print(f'One Year Before Today: {one_year_before_today}')
