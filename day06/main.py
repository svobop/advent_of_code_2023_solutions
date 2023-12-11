from math import sqrt

def process_data(file):
    with open(file) as f:
        for row in f:
            if row.startswith("Time:"):
                times = [int(_) for _ in row.split(":")[1].split()]
            elif row.startswith("Distance:"):
                distances = [int(_) for _ in row.split(":")[1].split()]
    return zip(times, distances)

def process_data_(file):
    with open(file) as f:
        for row in f:
            if row.startswith("Time:"):
                times = [int(row.split(":")[1].replace(" ", ""))]
            elif row.startswith("Distance:"):
                distances = [int(row.split(":")[1].replace(" ", ""))]
    return zip(times, distances)

def distance_formula(time, hold_time):
    return (time-hold_time)*hold_time

def hold_time_formula(time, distance):
    return (time - sqrt(time**2-4*distance))/2, (time + sqrt(time**2-4*distance))/2

def derivative_distance_formula(time, hold_time):
    return (time-2*hold_time)

def optimum_hold_time(time):
    return time/2


def test_case_one(input):
    for time, distance in process_data(input):
        optimum_hold_time_ = int(optimum_hold_time(time))
        increment = 0
        ways_to_win = list()
        while distance_formula(time, optimum_hold_time_ + increment) > distance:
            ways_to_win.append(optimum_hold_time_ + increment)
            increment += 1
        increment = 1
        while distance_formula(time, optimum_hold_time_ - increment) > distance:
            ways_to_win.append(optimum_hold_time_ - increment)
            increment += 1
        print(time, distance, ways_to_win, len(ways_to_win))

def task_one(input):
    product = 1
    for time, distance in process_data(input):
        optimum_hold_time_ = int(optimum_hold_time(time))
        increment = 0
        ways_to_win = list()
        while distance_formula(time, optimum_hold_time_ + increment) > distance:
            ways_to_win.append(optimum_hold_time_ + increment)
            increment += 1
        increment = 1
        while distance_formula(time, optimum_hold_time_ - increment) > distance:
            ways_to_win.append(optimum_hold_time_ - increment)
            increment += 1
        product *= len(ways_to_win)
    return product

def task_two(input):
    product = 1
    for time, distance in process_data_(input):
        print(time, distance)
        optimum_hold_time_ = int(optimum_hold_time(time))
        increment = 0
        ways_to_win = list()
        while distance_formula(time, optimum_hold_time_ + increment) > distance:
            ways_to_win.append(optimum_hold_time_ + increment)
            increment += 1
        increment = 1
        while distance_formula(time, optimum_hold_time_ - increment) > distance:
            ways_to_win.append(optimum_hold_time_ - increment)
            increment += 1
        product *= len(ways_to_win)
    return product

def task_two_use_formula(input): # super fast but inexact because of rounding errors
    product = 1
    for time, distance in process_data_(input):
        print(time, distance)
        product *= abs(2*(hold_time_formula(time, distance)[0]-optimum_hold_time(time)))-1
    return product

print(task_two("input.txt"))
