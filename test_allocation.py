import pandas as pd
from itertools import combinations

# Load dataset
df = pd.read_excel('uploads/students_320_updated_depts.xlsx')
print(f"Total students to allocate: {len(df)}")

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
    print(f"  Group ({dept}, Y{year}): {len(group_list)} students")

print(f"\nTotal groups created: {len(groups)}")

# Find valid pairs
valid_pairs = []
for g1, g2 in combinations(groups.keys(), 2):
    dept1, year1 = g1
    dept2, year2 = g2
    if dept1 != dept2 and year1 != year2:
        valid_pairs.append((g1, g2))

print(f"Valid pairs found: {len(valid_pairs)}")

# Simulate allocation
allocation = []
for (g1, g2) in valid_pairs:
    # Pop from original groups (this removes them)
    while groups[g1] and groups[g2]:
        if groups[g1]:
            s = groups[g1].pop()
            allocation.append(s)
        if groups[g2]:
            s = groups[g2].pop()
            allocation.append(s)

# Remaining students
for group_key, group_list in groups.items():
    allocation.extend(group_list)

print(f"\n✓ FINAL: Allocated {len(allocation)} students")
print(f"Expected: {len(df)} students")
print(f"Match: {len(allocation) == len(df)}")
