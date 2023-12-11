def process_data(file):
    with open(file) as f:
        for row in f:
            if row.startswith("Time:"):
                times = [int(_) for _ in row.split(":")[1].split()]
            elif row.startswith("Distance:"):
                distances = [int(_) for _ in row.split(":")[1].split()]
    return zip(times, distances)

def distance_formula(time, hold_time):
    return (time-hold_time)*hold_time

def derivative_distance_formula(time, hold_time):
    return (time-2*hold_time)

def optimum_hold_time(time):
    return time/2


def test_case_one():
    for time, distance in process_data("test_data.txt"):
        optimum_hold_time_ = int(optimum_hold_time(time))
        increment = 0
        ways_to_win = list()
        while distance_formula(time, optimum_hold_time_ + increment) > distance:
            ways_to_win.append(optimum_hold_time_ + increment)
            increment += 1
        increment = 0
        while distance_formula(time, optimum_hold_time_ - increment) > distance:
            ways_to_win.append(optimum_hold_time_ - increment)
            increment += 1
        ways_to_win = set(ways_to_win)
        print(time, distance, ways_to_win, len(ways_to_win))


test_case_one()
