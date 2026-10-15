import sys
from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
records = read_valid(lines)

# Всего строк непустых — минус те, что прошли. Разница = пропущенные.
nonempty = 0
for line in lines:
    if line.strip() != "":
        nonempty = nonempty + 1

skipped = nonempty - len(records)

print(len(records))
print(skipped)

if len(records) > 0:
    best = warmest_city(records)
    averages = average_by_city(records)
    print(f"{averages[best]:.1f}")
else:
    print("0.0")
