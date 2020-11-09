import time
def difference(morning_hour, evening_hour):
    variants = ""
    local_hour = time.localtime().tm_hour
    local_min = time.localtime().tm_min    
    if (local_hour < morning_hour):
        delta_hour  = morning_hour - (local_hour + 1)
        delta_min   = 60 - local_min 
        variants = "A"
    elif (local_hour >= morning_hour) and (local_hour < evening_hour):
        delta_hour = evening_hour - (local_hour + 1)
        delta_min   = 60 - local_min 
        variants = "B"
    else:
        B = local_hour + 1
        C = 24 - B
        delta_hour = morning_hour + C
        delta_min   = 60 - local_min 
        variants = "A"
    return ((delta_hour * 60 * 60) + delta_min * 60), variants
