import pandas as pd
from itertools import combinations

# Load dataset
df = pd.read_excel('uploads/students_320_updated_depts.xlsx')
print(f"Total students: {len(df)}\n")

# Group by Department + Year
groups = {}
for (dept, year), group in df.groupby(['Department', 'Year']):
    group_list = []
    for _, row in group.iterrows():
        group_list.append({
            'register_number': row['Register Number'], 
            'department': dept,
            'year': year
        })
    groups[(dept, year)] = group_list

seats_per_classroom = 25
allocation = []
room_no = 1

# Step 1: Main valid pairs (dept ≠ dept AND year ≠ year)
valid_pairs = []
for g1, g2 in combinations(groups.keys(), 2):
    dept1, year1 = g1
    dept2, year2 = g2
    if dept1 != dept2 and year1 != year2:
        valid_pairs.append((g1, g2))

for (g1, g2) in valid_pairs:
    if not groups[g1] or not groups[g2]:
        continue
    room_students = []
    while len(room_students) < seats_per_classroom and (groups[g1] or groups[g2]):
        if groups[g1] and len(room_students) < seats_per_classroom:
            student = groups[g1].pop()
            room_students.append(student)
        if groups[g2] and len(room_students) < seats_per_classroom:
            student = groups[g2].pop()
            room_students.append(student)
    if room_students:
        allocation.extend([(room_no, s['department'], s['year']) for s in room_students])
        room_no += 1

print(f"After main pairs (strict: dept ≠ dept, year ≠ year):")
print(f"  Students: {len(allocation)}, Rooms: {room_no-1}\n")

# Step 2: Remaining valid pairs (still dept ≠ dept AND year ≠ year)
remaining_groups = {}
for group_key, group_list in groups.items():
    if group_list:
        remaining_groups[group_key] = group_list

remaining_pairs = []
for g1, g2 in combinations(remaining_groups.keys(), 2):
    dept1, year1 = g1
    dept2, year2 = g2
    if dept1 != dept2 and year1 != year2 and remaining_groups[g1] and remaining_groups[g2]:
        remaining_pairs.append((g1, g2))

for (g1, g2) in remaining_pairs:
    if not remaining_groups[g1] or not remaining_groups[g2]:
        continue
    room_students = []
    while len(room_students) < seats_per_classroom and (remaining_groups[g1] or remaining_groups[g2]):
        if remaining_groups[g1] and len(room_students) < seats_per_classroom:
            student = remaining_groups[g1].pop()
            room_students.append(student)
        if remaining_groups[g2] and len(room_students) < seats_per_classroom:
            student = remaining_groups[g2].pop()
            room_students.append(student)
    if room_students:
        allocation.extend([(room_no, s['department'], s['year']) for s in room_students])
        room_no += 1

print(f"After remaining strict pairs:")
print(f"  Students: {len(allocation)}, Rooms: {room_no-1}\n")

# Step 3: Year-based pairs (year ≠ year, allow same dept)
final_remaining_groups = {}
for group_key, group_list in remaining_groups.items():
    if group_list:
        final_remaining_groups[group_key] = group_list

print(f"Remaining groups for year-based pairing:")
for key, lst in final_remaining_groups.items():
    if lst:
        print(f"  {key}: {len(lst)} students")

year_based_pairs = []
for g1, g2 in combinations(final_remaining_groups.keys(), 2):
    dept1, year1 = g1
    dept2, year2 = g2
    if year1 != year2 and final_remaining_groups[g1] and final_remaining_groups[g2]:
        year_based_pairs.append((g1, g2))

print(f"Year-based pairs found: {len(year_based_pairs)}\n")

for (g1, g2) in year_based_pairs:
    if not final_remaining_groups[g1] or not final_remaining_groups[g2]:
        continue
    room_students = []
    while len(room_students) < seats_per_classroom and (final_remaining_groups[g1] or final_remaining_groups[g2]):
        if final_remaining_groups[g1] and len(room_students) < seats_per_classroom:
            student = final_remaining_groups[g1].pop()
            room_students.append(student)
        if final_remaining_groups[g2] and len(room_students) < seats_per_classroom:
            student = final_remaining_groups[g2].pop()
            room_students.append(student)
    if room_students:
        depts = set(s[1] for s in [(room_no, s['department'], s['year']) for s in room_students])
        years = set(s[2] for s in [(room_no, s['department'], s['year']) for s in room_students])
        print(f"Room {room_no}: {len(room_students)} students, Depts: {depts}, Years: {years}")
        allocation.extend([(room_no, s['department'], s['year']) for s in room_students])
        room_no += 1

print(f"\nAfter year-based pairs:")
print(f"  Students: {len(allocation)}, Rooms: {room_no-1}\n")

# Step 4: Any final remaining
absolute_remaining = []
for group_list in final_remaining_groups.values():
    absolute_remaining.extend(group_list)

if absolute_remaining:
    print(f"Absolute final remaining: {len(absolute_remaining)} students")
    i = 0
    while i < len(absolute_remaining):
        room_students = absolute_remaining[i:i+seats_per_classroom]
        allocation.extend([(room_no, s['department'], s['year']) for s in room_students])
        room_no += 1
        i += seats_per_classroom

print(f"\n✓ FINAL:")
print(f"   Total students: {len(allocation)}")
print(f"   Expected: {len(df)}")
print(f"   Match: {len(allocation) == len(df)}")
print(f"   Total rooms: {room_no - 1}")
