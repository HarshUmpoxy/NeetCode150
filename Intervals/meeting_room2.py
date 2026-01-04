# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i),
# find the minimum number of days required to schedule all meetings without any conflicts.

# Note: (0,8),(8,10) is not considered a conflict at 8.

# Line Sweep Algorithm
# 1. Create a list of events (start, end)
# 2. Sort events by time
# 3. Iterate through events
# 4. If event is start, increment count
# 5. If event is end, decrement count
# 6. Return max count

def minMeetingDays(intervals):
    events = []
    
    # Step 1: Create Events
    # We use +1 for start and -1 for end.
    for start, end in intervals:
        events.append((start, 1))
        events.append((end, -1))
    
    # Step 2: Sort Events
    # Python sorts tuples element by element.
    # 1. It sorts by 'time' (first element).
    # 2. If times are equal, it sorts by 'type' (second element).
    # Since -1 (End) is smaller than 1 (Start), Python AUTOMATICALLY
    # puts the End event before the Start event for the same time.
    # This perfectly handles the (8,8) edge case!
    events.sort()
    
    max_days = 0
    current_days = 0
    
    # Step 3: Sweep
    for time, type_ in events:
        current_days += type_
        max_days = max(max_days, current_days)
        
    return max_days