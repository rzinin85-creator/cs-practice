import sys
from stats import average_by_city, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
records, skipped = read_valid(lines)

print(len(records))
print(skipped)

best = warmest_city(records)
averages = average_by_city(records)
print(f"{averages[best]:.1f}")
