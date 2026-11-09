def replace_value(values, index, new_value):
    values[index] = new_value
    return None

def find_first(values, target):
    for n in range(len(values)):
        if values[n] == target:
            return n
    return -1

def summarize(values):
    minimum = min(values)
    maximum = max(values)
    total = sum(values)
    stats_record = (minimum, maximum, total)
    return stats_record

days = int(input("Enter the number of days: "))

original = []
for i in range(days):
    hours = int(input("Enter sleep time in hours: "))
    original.append(hours)

updated = original[:]

index_to_fix = int(input("Enter the index to correct: "))
new_time = int(input("Enter the new sleep time: "))
replace_value(updated, index_to_fix, new_time)

target = int(input("Enter the sleep time to search for: "))

found_index = find_first(updated, target)
target_count = updated.count(target)

stats_record = summarize(updated)
minimum, maximum, total = stats_record

sorted_list = sorted(updated)

print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_list}")
print(f"Minimum sleep time: {minimum} hours")
print(f"Maximum sleep time: {maximum} hours")
print(f"Total sleep time: {total} hours")

if found_index == -1:
    print("Target not found")
else:
    print(f"First matching index: {found_index}")

print(f"Matching values: {target_count}")
