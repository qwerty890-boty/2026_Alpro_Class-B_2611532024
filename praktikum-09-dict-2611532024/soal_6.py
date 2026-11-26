schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

busiest_day, max_count = max(
    schedule.items(), key=lambda item: len(item[1])
)
print(f"Busiest day: {busiest_day} ({len(max_count)} courses)")

course_name = input().strip()
day_count = sum(1 for courses in schedule.values() if course_name in courses)
print(f"{course_name}: {day_count} days")