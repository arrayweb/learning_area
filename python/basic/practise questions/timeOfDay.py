# Write a function which receives 4 digits and returns the latest time of day that can be built with those digits.

# The time should be in HH:MM format.

# Examples:

# digits: 1, 9, 8, 3 => result: "19:38"
# digits: 9, 1, 2, 5 => result: "21:59" ("19:25" is also a valid time, but 21:59 is later)

# Notes

#     Result should be a valid 24-hour time, between 00:00 and 23:59.
#     Only inputs which have valid answers are tested.

 
def latest_clock(a, b, c, d):
    # combine the digits into a sorted list
    sorted_digits = sorted([a, b, c, d], reverse=True)

    # build the hours part of the time by taking the first two digits
    hour_str = ''.join([str(d) for d in sorted_digits[:2]])
    hour = int(hour_str) if len(hour_str) == 2 else f"0{hour_str[0]}"

    # build the minutes part of the time by taking the last two digits
    min_str = ''.join([str(d) for d in sorted_digits[-2:]])
    minute = int(min_str) if len(min_str) == 2 else f"0{min_str[0]}"

    return f"{hour}:{minute}"