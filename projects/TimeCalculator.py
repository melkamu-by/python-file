def add_time(start, duration, starting_day=False):
    
    start_parts = start.split()
    time_parts = start_parts[0].split(':')
    period = start_parts[1]
    
    start_hour = int(time_parts[0])
    start_min = int(time_parts[1])
    
    
    dur_parts = duration.split(':')
    dur_hour = int(dur_parts[0])
    dur_min = int(dur_parts[1])
    
    if start_hour == 12:
        start_hour = 0
    if period == "PM":
        start_hour += 12
        
    total_min = start_min + dur_min
    extra_hour = total_min // 60
    final_min = total_min % 60
    
    total_hour = start_hour + dur_hour + extra_hour
    final_hour = total_hour % 24
    days_later = total_hour // 24
    
    display_period = "AM"
    if final_hour >= 12:
        display_period = "PM"
        if final_hour > 12:
            final_hour -= 12
    elif final_hour == 0:
        final_hour = 12
        
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    new_time = f"{final_hour}:{final_min:02d} {display_period}"
    
    if starting_day:
        current_day_index = days_of_week.index(starting_day.capitalize())
        new_day_index = (current_day_index + days_later) % 7
        new_time += f", {days_of_week[new_day_index]}"

    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time
print(add_time("3:00 PM", "3:10"))
print(add_time("12:00 PM", "2:00"))
print(add_time("11:30 PM", "2:32", "Monday"))
print(add_time("6:30 PM", "205:45", "Tuesday"))

   

    