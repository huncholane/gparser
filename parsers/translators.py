"""
Translator functions for the basics.
"""
import re
import datetime as dt


def split_hour_minute(str):
    """Extracts hours and minutes into separate strings"""
    if ':' in str and len(str) < 5 or len(str) < 4:
        raise ValueError(
            f'Hours and minutes must have at least 4 characters without : and 5 with :.')
    str = ''.join(re.findall(r'\d+', str))
    return str[:-2], str[-2:]


def hour_minute_to_delta(cls, str):
    """Converts hour and minute string into a time delta"""
    hours, minutes = split_hour_minute(str)
    return dt.timedelta(hours=int(hours), minutes=int(minutes))


def hour_minute_to_int(cls, str):
    """Converts hours and minutes to a total number of minutes"""
    hours, minutes = split_hour_minute(str)
    return int(minutes)+int(hours)*60


def phone(cls, str):
    """Converts numbers to a phone number with country code readiness"""
    nums = ''.join(re.findall(r'\d+', str))
    if len(nums) < 4:
        raise TypeError(f'Impossible phone number {str}.')
    if nums[:3] == '011':
        return '+'+nums[3:]
    else:
        return '+1'+nums
