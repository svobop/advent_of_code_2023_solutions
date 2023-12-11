def process_data(file):
    with open(file) as f:
        for row in f:
            if row.startswith("Time:"):
                time = [int(_) for _ in row.split(":")[1].split()]
            elif row.startswith("Distance:"):
                distance = [int(_) for _ in row.split(":")[1].split()]
    return time, distance

def distance_formula(time, hold_time):
    return (time-hold_time)*hold_time

def derivative_distance_formula(time, hold_time):
    return (time-2*hold_time)

def optimum_hold_time(time):
    return time/2.

print(optimum_hold_time(7))
for hold_time in range(8):
    print(hold_time, distance_formula(7, hold_time), derivative_distance_formula(7, hold_time))