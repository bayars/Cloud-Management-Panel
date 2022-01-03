#!/usr/bin/python3.9

from datetime import datetime
from zoneinfo import ZoneInfo

dt = datetime.now(ZoneInfo(America/New_York))
print(dt)
