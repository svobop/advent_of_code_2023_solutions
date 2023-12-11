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
    return sorted(map, key=lambda x: x[1])

def apply_map(seed, map):
    for row in map:
        if seed == 81:
            pass
        if row[1] <= seed < row[1]+row[2]:
            return row[0] + (seed - row[1])
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


seeds, seed_to_soil, soil_to_fertilizer, fertilizer_to_water, water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location = process_data(
    "input.txt")

min_location = 1e100
for seed in seeds:
    soil = apply_map(seed, seed_to_soil)
    fertilizer = apply_map(soil, soil_to_fertilizer)
    water = apply_map(fertilizer, fertilizer_to_water)
    light = apply_map(water, water_to_light)
    temperature = apply_map(light, light_to_temperature)
    humidity = apply_map(temperature, temperature_to_humidity)
    location = apply_map(humidity, humidity_to_location)
    print(location)
    if location < min_location:
        min_location = location

print(min_location)