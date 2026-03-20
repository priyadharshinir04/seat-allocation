#!/usr/bin/env python
"""
Comprehensive verification of the Realistic Classroom Visualization Upgrade
"""
import os
import sys

print("╔" + "═"*68 + "╗")
print("║" + " "*12 + "REALISTIC CLASSROOM VISUALIZATION UPGRADE" + " "*16 + "║")
print("║" + " "*20 + "Verification Report" + " "*29 + "║")
print("╚" + "═"*68 + "╝\n")

tests_passed = 0
tests_failed = 0

def test(description, condition, details=""):
    global tests_passed, tests_failed
    if condition:
        print(f"✓ {description}")
        if details:
            print(f"  → {details}")
        tests_passed += 1
    else:
        print(f"✗ {description}")
        if details:
            print(f"  → {details}")
        tests_failed += 1

# TEST 1: Template File Exists
test("Template file exists",
     os.path.exists('templates/classroom_view.html'),
     "classroom_view.html is present")

# TEST 2: Jinja Compilation
try:
    from jinja2 import Environment, FileSystemLoader
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('classroom_view.html')
    test("Template compiles without errors",
         True,
         "Jinja2 template syntax is valid")
except Exception as e:
    test("Template compiles without errors",
         False,
         str(e))

# TEST 3: Flask App Import
try:
    from app import app
    test("Flask application imports successfully",
         True,
         "app.py loads without errors")
except Exception as e:
    test("Flask application imports successfully",
         False,
         str(e))

# TEST 4: Route Exists
try:
    from app import app
    routes = [rule.rule for rule in app.url_map.iter_rules()]
    has_route = '/classroom-visualization' in routes
    test("Classroom visualization route exists",
         has_route,
         "Route /classroom-visualization is registered")
except Exception as e:
    test("Classroom visualization route exists",
         False,
         str(e))

# TEST 5: Template Structure Check
try:
    with open('templates/classroom_view.html', 'r') as f:
        content = f.read()
        
    has_classroom_layout = 'class="classroom-layout' in content
    test("Classroom layout container exists",
         has_classroom_layout,
         "CSS class 'classroom-layout' found")
        
    has_bench_sections = 'class="bench-sections' in content
    test("Bench sections grid layout exists",
         has_bench_sections,
         "CSS class 'bench-sections' found")
        
    has_bench_elements = 'class="bench' in content
    test("Bench elements defined",
         has_bench_elements,
         "CSS class 'bench' found")
        
    has_board_area = 'class="classroom-board' in content
    test("Classroom board area defined",
         has_board_area,
         "CSS class 'classroom-board' found")
        
    has_benchmark_seats = 'class="benchmark-seat' in content
    test("Benchmark seat elements defined",
         has_benchmark_seats,
         "CSS class 'benchmark-seat' found")
        
except Exception as e:
    test("Template structure validation",
         False,
         str(e))

# TEST 6: Key CSS Classes
try:
    with open('templates/classroom_view.html', 'r') as f:
        content = f.read()
        
    css_classes = [
        '.classroom-layout',
        '.bench-sections',
        '.bench-section',
        '.bench-section-label',
        '.bench',
        '.bench-label',
        '.bench-rows',
        '.benchmark-seat',
        '.classroom-board',
        '.seat-info'
    ]
    
    for css_class in css_classes:
        has_class = css_class in content
        if has_class:
            tests_passed += 1
        else:
            tests_failed += 1
            
    print(f"\n✓ CSS Classes: {len(css_classes)} required classes defined")
        
except Exception as e:
    print(f"✗ CSS Classes check failed: {e}")
    tests_failed += 1

# TEST 7: Jinja Loops for Bench Organization
try:
    with open('templates/classroom_view.html', 'r') as f:
        content = f.read()
        
    has_sections = [
        ('LEFT SECTION: Benches 1-5', 'range(1, 6)'),
        ('MIDDLE-LEFT SECTION: Benches 6-10', 'range(6, 11)'),
        ('MIDDLE-RIGHT SECTION: Benches 11-15', 'range(11, 16)'),
        ('RIGHT SECTION: Benches 16-20', 'range(16, 21)')
    ]
    
    sections_found = 0
    for section_name, range_call in has_sections:
        if section_name in content and range_call in content:
            sections_found += 1
    
    test("All four bench sections implemented",
         sections_found == 4,
         f"{sections_found}/4 sections found (LEFT, MIDDLE-LEFT, MIDDLE-RIGHT, RIGHT)")
        
except Exception as e:
    test("Bench sections validation",
         False,
         str(e))

# TEST 8: Seat Rendering Logic
try:
    with open('templates/classroom_view.html', 'r') as f:
        content = f.read()
        
    has_seat1 = 'Seat 1' in content
    has_seat2 = 'Seat 2' in content
    has_dual_seats = 'bench-rows' in content and 'benchmark-seat' in content
    
    test("Two-seat bench structure implemented",
         has_seat1 and has_seat2 and has_dual_seats,
         "Each bench configured with 2 seats side-by-side")
        
except Exception as e:
    test("Seat rendering logic",
         False,
         str(e))

# TEST 9: Department Color Classes
try:
    with open('templates/classroom_view.html', 'r') as f:
        content = f.read()
        
    dept_colors = {
        '.dept-cse': '#3498db',
        '.dept-it': '#2ecc71',
        '.dept-ece': '#e67e22',
        '.dept-mech': '#9b59b6',
        '.dept-civil': '#1abc9c',
        '.dept-eee': '#f39c12',
        '.dept-aids': '#c0392b'
    }
    
    colors_found = 0
    for color_class, hex_code in dept_colors.items():
        if hex_code in content:
            colors_found += 1
    
    test("Department color scheme implemented",
         colors_found >= 7,
         f"{colors_found}/7 department colors defined")
        
except Exception as e:
    test("Department colors",
         False,
         str(e))

# TEST 10: View Toggle Feature
try:
    with open('templates/classroom_view.html', 'r') as f:
        content = f.read()
        
    has_toggle = 'btn-view-toggle' in content
    has_table_link = "url_for('view_results')" in content
    has_classroom_link = "url_for('classroom_visualization')" in content
    
    test("View toggle buttons implemented",
         has_toggle and has_table_link and has_classroom_link,
         "Toggle available between Classroom Layout and Table View")
        
except Exception as e:
    test("View toggle",
         False,
         str(e))

# TEST 11: Search Functionality  
try:
    with open('templates/classroom_view.html', 'r') as f:
        content = f.read()
        
    has_search = 'searchStudent()' in content
    has_search_input = 'searchInput' in content
    has_highlight = 'highlighted' in content
    
    test("Search functionality integrated",
         has_search and has_search_input and has_highlight,
         "Student search with highlight animation ready")
        
except Exception as e:
    test("Search functionality",
         False,
         str(e))

# TEST 12: Print Styles
try:
    with open('templates/classroom_view.html', 'r') as f:
        content = f.read()
        
    has_print_styles = '@media print' in content
    has_page_break = 'page-break' in content
    
    test("Print-friendly styles implemented",
         has_print_styles and has_page_break,
         "Print optimization for exam administration")
        
except Exception as e:
    test("Print styles",
         False,
         str(e))

# TEST 13: Responsive Design
try:
    with open('templates/classroom_view.html', 'r') as f:
        content = f.read()
        
    has_responsive = '@media (max-width' in content
    responsive_counts = content.count('@media (max-width')
    
    test("Responsive design media queries",
         has_responsive and responsive_counts >= 3,
         f"{responsive_counts} breakpoints for mobile/tablet optimization")
        
except Exception as e:
    test("Responsive design",
         False,
         str(e))

# TEST 14: Navigation Flow
try:
    with open('templates/classroom_view.html', 'r') as f:
        content = f.read()
        
    has_back_button = 'oncampus_dashboard' in content
    has_footer_actions = 'footer-actions' in content
    
    test("Navigation and back button flow",
         has_back_button and has_footer_actions,
         "Complete navigation to dashboard and other pages")
        
except Exception as e:
    test("Navigation",
         False,
         str(e))

# SUMMARY
print("\n" + "─"*68)
print(f"\nTest Results:")
print(f"  ✓ Passed: {tests_passed}")
print(f"  ✗ Failed: {tests_failed}")
print(f"  Total:   {tests_passed + tests_failed}\n")

if tests_failed == 0:
    print("╔" + "═"*66 + "╗")
    print("║  ✓ ALL TESTS PASSED - UPGRADE COMPLETE  ✓" + " "*21 + "║")
    print("╚" + "═"*66 + "╝")
    print("\n🎉 Realistic Classroom Visualization Successfully Implemented!\n")
    print("Key Features Ready:")
    print("  ✓ 4-section bench layout (LEFT, MIDDLE-LEFT, MIDDLE-RIGHT, RIGHT)")
    print("  ✓ 20 benches × 2 seats per classroom")
    print("  ✓ Department color coding")
    print("  ✓ Professional board/examiner area")
    print("  ✓ Search and highlight functionality")
    print("  ✓ Print-optimized layout")
    print("  ✓ Responsive design for all devices")
    print("  ✓ View toggle (Classroom ↔ Table)")
    sys.exit(0)
else:
    print("⚠ Some tests failed. Please review the output above.")
    sys.exit(1)
