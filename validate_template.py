from jinja2 import Environment, FileSystemLoader
import sys

env = Environment(loader=FileSystemLoader('templates'))
try:
    template = env.get_template('classroom_view.html')
    print('✓ classroom_view.html compiles without Jinja errors')
    print('✓ Template is ready to use')
except Exception as e:
    print(f'✗ Template error: {e}')
    import traceback
    traceback.print_exc()
    sys.exit(1)
