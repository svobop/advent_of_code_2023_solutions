def process_data(file):
    seeds = None
    seed_to_soil = None
    soil_to_fertilizer = None
    fertilizer_to_water = None
    water_to_light = None
    light_to_temperature = None
    temperature_to_humidity = None
    humidity_to_location = None

    with open(file) as f:
        for row in f:
            if row.startswith("seeds:"):
                seeds = [int(_) for _ in row.split(":")[1].split()]
            elif row.startswith("seed-to-soil"):
                seed_to_soil = read_map(f)
            elif row.startswith("soil-to-fertilizer"):
                soil_to_fertilizer = read_map(f)
            elif row.startswith("fertilizer-to-water"):
                fertilizer_to_water = read_map(f)
            elif row.startswith("water-to-light"):
                water_to_light = read_map(f)
            elif row.startswith("light-to-temperature"):
                light_to_temperature = read_map(f)
            elif row.startswith("temperature-to-humidity"):
                temperature_to_humidity = read_map(f)
            elif row.startswith("humidity-to-location"):
                humidity_to_location = read_map(f)


    return seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location


def read_map(f):
    map = list()
    for row in f:
        if row.strip() == "":
            break
        numbers = [int(_) for _ in row.split()]
        map.append(numbers)
    return sorted(map, key=lambda x: x[0])

def apply_map(seed, map):
    map = sorted(map, key=lambda x: x[1])
    for row in map:
        if row[1] <= seed < row[1]+row[2]:
            return row[0] + (seed - row[1])
    return seed

def inverze_apply_map(seed, map):
    for row in map:
        if row[0] <= seed < row[0]+row[2]:
            return row[1] + (seed - row[0])
    return seed


def test_case_one():
    seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = process_data(
        "test_data.txt")
    print(seeds)
    print(seed_to_soil)
    print(soil_to_fertilizer)
    print(fertilizer_to_water)
    print(water_to_light)
    print(light_to_temperature)
    print(temperature_to_humidity)
    print(humidity_to_location)
    print("seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location")
    for seed in seeds:
        soil = apply_map(seed, seed_to_soil)
        fertilizer = apply_map(soil, soil_to_fertilizer)
        water = apply_map(fertilizer, fertilizer_to_water)
        light = apply_map(water, water_to_light)
        temperature = apply_map(light, light_to_temperature)
        humidity = apply_map(temperature, temperature_to_humidity)
        location = apply_map(humidity, humidity_to_location)

        print(seed, soil, fertilizer, water, light, temperature, humidity, location)


def task_one(input):
    apply_transformations(input)


def apply_transformations(input):
    seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = process_data(input)
    min_location = 1e100
    for seed in seeds:
        soil = apply_map(seed, seed_to_soil)
        fertilizer = apply_map(soil, soil_to_fertilizer)
        water = apply_map(fertilizer, fertilizer_to_water)
        light = apply_map(water, water_to_light)
        temperature = apply_map(light, light_to_temperature)
        humidity = apply_map(temperature, temperature_to_humidity)
        location = apply_map(humidity, humidity_to_location)
        if location < min_location:
            min_location = location
    print(min_location)


def task_one_inverse(input):
    apply_transformations_inverse(input)


def apply_transformations_inverse(input):
    seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = process_data(
        input)
    seed = 0
    location = -1
    while seed not in seeds:
        location += 1
        humidity = inverze_apply_map(location, humidity_to_location)
        temperature = inverze_apply_map(humidity, temperature_to_humidity)
        light = inverze_apply_map(temperature, light_to_temperature)
        water = inverze_apply_map(light, water_to_light)
        fertilizer = inverze_apply_map(water, fertilizer_to_water)
        soil = inverze_apply_map(fertilizer, soil_to_fertilizer)
        seed = inverze_apply_map(soil, seed_to_soil)
    print(location)


def task_two():
    seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = process_data(
        "input.txt")
    min_location = 1e100
    total_seed_ranges = len(seeds[::2])
    index = 0
    indexes = list()
    seed_intervals_starts = list()
    seed_intervals_lengths = list()
    for seed_range_start, seed_range_length in zip(seeds[::2], seeds[1::2]):
        seed_intervals_starts.append(seed_range_start)
        seed_intervals_lengths.append(seed_range_length)
        indexes.append(index)
        index += 1


    print(seed_intervals_starts)
    print(seed_intervals_lengths)
    print(indexes)
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.barh(indexes, width=seed_intervals_lengths, left=seed_intervals_starts, height=0.3)
    plt.show()

task_two()