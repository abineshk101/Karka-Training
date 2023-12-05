from datetime import datetime
import pytz
UTC=pytz.utc
print(datetime.now(UTC))
india=pytz.timezone('Asia/Kolkata')
print(datetime.now(india))