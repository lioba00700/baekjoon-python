# 2026.03.08
from datetime import datetime

# strfdate 사용
print(datetime.now().strftime('%Y-%m-%d'))

# f-string 사용
now = datetime.now()
print(f"{now:%Y-%m-%d}")