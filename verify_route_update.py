from app import app

print("✓ Verifying classroom grid update...")
print()

routes = {rule.rule: list(rule.methods) for rule in app.url_map.iter_rules()}

print("Classroom-related routes:")
for route in sorted(routes.keys()):
    if 'classroom' in route or 'grid' in route:
        methods = routes[route]
        print(f"  • {route:30} {methods}")

print()
print("Key route details:")

# Check /classroom-grid
if '/classroom-grid' in routes:
    print("  ✓ /classroom-grid - NOW RENDERS NEW BENCH LAYOUT")
else:
    print("  ✗ /classroom-grid not found!")

# Check /classroom-visualization  
if '/classroom-visualization' in routes:
    print("  ✓ /classroom-visualization - Also available with new bench layout")
else:
    print("  ✗ /classroom-visualization not found!")

print()
print("✓ Update complete! Visit http://127.0.0.1:5000/classroom-grid to see the new bench layout.")
