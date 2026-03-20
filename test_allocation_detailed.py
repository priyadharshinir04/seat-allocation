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

print(f"Groups: {len(groups)}\n")

# Find valid pairs
valid_pairs = []
for g1, g2 in combinations(groups.keys(), 2):
    dept1, year1 = g1
    dept2, year2 = g2
    if dept1 != dept2 and year1 != year2:
        valid_pairs.append((g1, g2))

print(f"Valid pairs: {len(valid_pairs)}\n")

# SIMULATE ALLOCATION
seats_per_classroom = 25
allocation = []
room_no = 1

# Step 1: Allocate main valid pairs
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

print(f"After main pairs: {len(allocation)} students allocated, {room_no-1} rooms used")

# Step 2: Re-group remaining
remaining_groups = {}
for group_key, group_list in groups.items():
    if group_list:
        remaining_groups[group_key] = group_list

print(f"Remaining groups: {len(remaining_groups)}")
for key, lst in remaining_groups.items():
    if lst:
        print(f"  {key}: {len(lst)} students")

# Step 3: Create remaining valid pairs
remaining_pairs = []
for g1, g2 in combinations(remaining_groups.keys(), 2):
    dept1, year1 = g1
    dept2, year2 = g2
    
    if dept1 != dept2 and year1 != year2 and remaining_groups[g1] and remaining_groups[g2]:
        remaining_pairs.append((g1, g2))

print(f"\nRemaining valid pairs: {len(remaining_pairs)}")

# Step 4: Allocate remaining pairs
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

print(f"After remaining pairs: {len(allocation)} students allocated, {room_no-1} rooms used")

# Step 5: Handle final remaining
final_remaining = []
for group_list in remaining_groups.values():
    final_remaining.extend(group_list)

if final_remaining:
    print(f"\nFinal remaining students to allocate: {len(final_remaining)}")
    for key, lst in remaining_groups.items():
        if lst:
            print(f"  {key}: {len(lst)} students")
    
    i = 0
    while i < len(final_remaining):
        room_students = final_remaining[i:i+seats_per_classroom]
        depts_in_room = set(s['department'] for s in room_students)
        allocation.extend([(room_no, s['department'], s['year']) for s in room_students])
        print(f"  Room {room_no}: {len(room_students)} students, Depts: {depts_in_room}")
        room_no += 1
        i += seats_per_classroom

print(f"\n✓ FINAL ALLOCATION:")
print(f"   Total students: {len(allocation)}")
print(f"   Total rooms: {room_no - 1}")
print(f"   Total classrooms: {20}")
