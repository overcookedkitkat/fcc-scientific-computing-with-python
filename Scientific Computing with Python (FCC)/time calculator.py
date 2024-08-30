days = {
    "": "",
    "Sunday": 1,
    "Monday": 2,
    "Tuesday": 3,
    "Wednesday": 4,
    "Thursday": 5,
    "Friday": 6,
    "Saturday": 7
}

def add_time(start, duration, day=""):
    #splitting hours, minutes, and am/pm
    arr = start.split()
    timeArr = arr[0].split(':')
    amPm = arr[1]
    hour = int(timeArr[0])
    minute = int(timeArr[1])
    
    addArr = duration.split(':')
    addHour = int(addArr[0])
    addMinute = int(addArr[1])
    
    #calculating new minute
    newMinute = minute + addMinute
    if newMinute >= 60:
        newMinute -= 60
        addHour += 1

    #calculating total hours and days
    totalHours = hour + addHour
    dayCount = totalHours // 24
    remainingHours = totalHours % 24
    
    #calculating new hour
    newHour = remainingHours % 12
    if newHour == 0:
        newHour = 12
    
    #determining am/pm
    periodCount = (hour + addHour) // 12
    isPm = amPm == "PM"
    newAmPm = "PM" if (periodCount + isPm) % 2 else "AM"
    
    #am/pm change at 12
    if remainingHours >= 12:
        dayCount += 1 if isPm else 0
    else:
        dayCount += 1 if isPm and (hour + addHour) >= 12 else 0
    
    #day calc
    if day:
        dayIndex = (days[day.capitalize()] + dayCount - 1) % 7 + 1
        newDay = None
        for k, v in days.items():
            if v == dayIndex:
                newDay = k
                break
    else:
        newDay = ""
    
    #days later message
    if dayCount == 0:
        daysLaterMessage = ""
    elif dayCount == 1:
        daysLaterMessage = " (next day)"
    else:
        daysLaterMessage = f" ({dayCount} days later)"
    
    if newDay:
        new_time = f"{newHour}:{newMinute:02d} {newAmPm}, {newDay}{daysLaterMessage}"
    else:
        new_time = f"{newHour}:{newMinute:02d} {newAmPm}{daysLaterMessage}"

    return new_time

# Test cases
print(repr(add_time('3:30 PM', '2:12'))) # should return '5:42 PM'
print(repr(add_time('11:55 AM', '3:12'))) # should return '3:07 PM'
print(repr(add_time('2:59 AM', '24:00'))) # should return '2:59 AM (next day)'
print(repr(add_time('11:59 PM', '24:05'))) # should return '12:04 AM (2 days later)'
print(repr(add_time('8:16 PM', '466:02'))) # should return '6:18 AM (20 days later)'
print(repr(add_time('3:30 PM', '2:12', 'Monday'))) # should return '5:42 PM, Monday'
print(repr(add_time('2:59 AM', '24:00', 'saturDay'))) # should return '2:59 AM, Sunday (next day)'
print(repr(add_time('11:59 PM', '24:05', 'Wednesday'))) # should return '12:04 AM, Friday (2 days later)'
print(repr(add_time('8:16 PM', '466:02', 'tuesday'))) # should return '6:18 AM, Monday (20 days later)'
