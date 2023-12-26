from functools import cache
from io import TextIOWrapper
from itertools import batched


def map_parser(stream: TextIOWrapper):
    result_map = []
    while (line := stream.readline().strip()) != "":
        dest, source, length = map(int, line.split())
        result_map.append((source, dest, length))
    return result_map

def stream_parser(stream: TextIOWrapper):
    # Seeds
    chunk = stream.read(7)
    assert chunk == "seeds: "
    seeds = batched(map(int, stream.readline().split()), 2)
    stream.read(1)

    # seed-to-soil map
    assert stream.readline() == "seed-to-soil map:\n"
    seed_to_soil_map = map_parser(stream)

    # soil-to-fertilizer map
    assert stream.readline() == "soil-to-fertilizer map:\n"
    soil_to_fertilizer_map = map_parser(stream)

    # fertilizer-to-water map
    assert stream.readline() == "fertilizer-to-water map:\n"
    fertilizer_to_water_map = map_parser(stream)

    # water-to-light map
    assert stream.readline() == "water-to-light map:\n"
    water_to_light_map = map_parser(stream)

    # light-to-temperature map
    assert stream.readline() == "light-to-temperature map:\n"
    light_to_temperature_map = map_parser(stream)

    # temperature-to-humidity map
    assert stream.readline() == "temperature-to-humidity map:\n"
    temperature_to_humidity_map = map_parser(stream)

   # humidity-to-location map
    assert stream.readline() == "humidity-to-location map:\n"
    humidity_to_location_map = map_parser(stream)

    return seeds, (
        seed_to_soil_map,
        soil_to_fertilizer_map,
        fertilizer_to_water_map,
        water_to_light_map,
        light_to_temperature_map,
        temperature_to_humidity_map,
        humidity_to_location_map
    )

@cache
def process_map(map_index: int, data):
    for source, dest, length in maps[map_index]:
        if source <= data < source + length:
            return data - source + dest
    return data

with open('input.txt', encoding='ascii') as f:
    seeds, maps = stream_parser(f)

min_location = None
for start_seed, seed_length in seeds:
    for seed in range(start_seed, start_seed + seed_length):
        current_value = seed
        for i in range(len(maps)):
            current_value = process_map(i, current_value)
        if min_location is None:
            min_location = current_value
        min_location = min(min_location, current_value)

print(min_location)
