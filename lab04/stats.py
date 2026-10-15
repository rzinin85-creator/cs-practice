def parse_record(line):
    parts = line.split(";")

    if len(parts) != 3:
        raise ValueError("Ожидалось 3 поля, получено " + str(len(parts)))

    city = parts[0]
    temp_str = parts[1]
    date = parts[2]

    if city.strip() == "":
        raise ValueError("Пустой город")
    if date.strip() == "":
        raise ValueError("Пустая дата")

    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError("Температура не число: " + temp_str)

    return {"city": city, "temp": temp, "date": date}

def read_valid(lines):
    records = []
    skipped = 0

    for line in lines:
        if line.strip() == "":
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            skipped = skipped + 1

    return records, skipped
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
