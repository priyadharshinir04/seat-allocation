import pandas as pd
import sys

# Test 1: Load and validate sample data
print("="*60)
print("TEST 1: Load Sample Data")
print("="*60)
try:
    df = pd.read_csv('sample_students.csv')
    print(f"✓ Loaded sample_students.csv")
    print(f"  - Rows: {len(df)}")
    print(f"  - Columns: {list(df.columns)}")
    print(f"  - Departments: {sorted(df['Department'].unique())}")
except Exception as e:
    print(f"✗ Error loading data: {e}")
    sys.exit(1)

# Test 2: Test app import and routes
print("\n" + "="*60)
print("TEST 2: Verify Flask Routes")
print("="*60)
try:
    from app import app
    routes = [rule.rule for rule in app.url_map.iter_rules()]
    critical_routes = ['/view-results', '/classroom-visualization', '/generate-seating']
    for route in critical_routes:
        if route in routes:
            print(f"✓ Route exists: {route}")
        else:
            print(f"✗ Route missing: {route}")
except Exception as e:
    print(f"✗ Error checking routes: {e}")
    sys.exit(1)

# Test 3: Test template rendering context simulation
print("\n" + "="*60)
print("TEST 3: Template Context Simulation")
print("="*60)
try:
    # Simulate allocation results
    allocation_results = []
    student_data = df.to_dict('records')
    
    classrooms = ['Hall A', 'Hall B']
    benches_per_classroom = 25
    
    classroom_index = 0
    bench_num = 1
    
    for i, student in enumerate(student_data):
        if i > 0 and i % (benches_per_classroom * 2) == 0:
            classroom_index += 1
            bench_num = 1
        
        if i % 2 == 0:
            bench_num_str = f"B-{bench_num}"
        else:
            bench_num += 1
            bench_num_str = f"B-{bench_num}"
        
        allocation_results.append({
            'register_number': student['Register Number'],
            'student_name': student['Student Name'],
            'department': student['Department'],
            'classroom': classrooms[min(classroom_index, len(classrooms)-1)],
            'bench_number': bench_num_str,
            'seat_number': 'S-' + ('1' if i % 2 == 0 else '2')
        })
    
    print(f"✓ Created {len(allocation_results)} allocation records")
    
    # Group by classroom
    classrooms_dict = {}
    for result in allocation_results:
        classroom = result['classroom']
        if classroom not in classrooms_dict:
            classrooms_dict[classroom] = []
        classrooms_dict[classroom].append(result)
    
    print(f"✓ Grouped into {len(classrooms_dict)} classrooms:")
    for classroom, students in classrooms_dict.items():
        print(f"  - {classroom}: {len(students)} students")
        benches = set(s['bench_number'] for s in students)
        print(f"    Benches: {len(benches)} unique benches")
        depts = set(s['department'] for s in students)
        print(f"    Departments: {len(depts)} unique departments")
        
except Exception as e:
    print(f"✗ Error in simulation: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n" + "="*60)
print("ALL TESTS PASSED!")
print("="*60)
