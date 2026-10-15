def parse_record(line):
    city, temp, date = line.split(";")
    return {"city": city, "temp": float(temp), "date": date}


def read_valid(lines):
    records = []
    for line in lines:
        records.append(parse_record(line))
    return records, 0


def average_by_city(records):
    total = {}
    count = {}
    for record in records:
        city = record["city"]
        total[city] = total.get(city, 0.0) + record["temp"]
        count[city] = count.get(city, 0) + 1
    averages = {}
    for city in total:
        averages[city] = round(total[city] / count[city], 1)
    return averages


def warmest_city(records):
    averages = average_by_city(records)
    best = None
    for city in averages:
        if best is None or averages[city] > averages[best]:
            best = city
    return best
