import os
import sys
from pathlib import Path

# Add this script to your Django project's root directory
# and run it with: python static_debug.py

# --- Configuration ---
APP_NAME = "weather_app"  # Change this to your app name
IMAGE_NAME = "devarno.png"  # The image filename
# -------------------

# Get the Django project settings
try:
    # Try to import Django settings
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'unrained.settings')  # Replace with your project name
    import django
    django.setup()
    from django.conf import settings
    settings_available = True
except Exception as e:
    print(f"Couldn't import Django settings: {e}")
    settings_available = False

# Current directory
current_dir = Path(os.path.abspath(os.path.dirname(__file__)))
print(f"Current directory: {current_dir}")

# Check if the image exists in various possible locations
possible_locations = [
    current_dir / APP_NAME / 'static' / APP_NAME / IMAGE_NAME,
    current_dir / 'static' / APP_NAME / IMAGE_NAME,
    current_dir / 'staticfiles' / APP_NAME / IMAGE_NAME
]

# If Django settings are available, add more potential locations
if settings_available:
    try:
        # Add STATIC_ROOT location
        static_root = Path(settings.STATIC_ROOT)
        possible_locations.append(static_root / APP_NAME / IMAGE_NAME)
        print(f"STATIC_ROOT: {static_root}")
        
        # Add STATIC_URL info
        print(f"STATIC_URL: {settings.STATIC_URL}")
        
        # Add STATICFILES_DIRS locations
        if hasattr(settings, 'STATICFILES_DIRS'):
            print(f"STATICFILES_DIRS: {settings.STATICFILES_DIRS}")
            for static_dir in settings.STATICFILES_DIRS:
                static_dir_path = Path(static_dir)
                possible_locations.append(static_dir_path / APP_NAME / IMAGE_NAME)
        else:
            print("STATICFILES_DIRS not defined in settings")
    except Exception as e:
        print(f"Error accessing Django settings: {e}")

# Check each location
print("\nChecking for image in possible locations:")
for loc in possible_locations:
    if loc.exists():
        print(f"✓ FOUND: {loc}")
    else:
        print(f"✗ NOT FOUND: {loc}")

# Check if collectstatic has been run
if settings_available:
    try:
        static_root = Path(settings.STATIC_ROOT)
        if static_root.exists():
            print(f"\nSTATIC_ROOT directory exists at {static_root}")
            # Count files to check if collectstatic was likely run
            file_count = sum(1 for _ in static_root.glob('**/*') if _.is_file())
            if file_count > 0:
                print(f"Found {file_count} files in STATIC_ROOT, collectstatic likely ran")
            else:
                print("STATIC_ROOT directory is empty, collectstatic may not have been run")
        else:
            print(f"\nSTATIC_ROOT directory does not exist at {static_root}")
            print("collectstatic has not been run or STATIC_ROOT is misconfigured")
    except Exception as e:
        print(f"Error checking STATIC_ROOT: {e}")

# Check server configuration (if possible)
print("\nReminder: For production deployments, ensure your web server is configured to serve:")
print(f"  - Files from {settings.STATIC_ROOT if settings_available else 'STATIC_ROOT'}")
print(f"  - At URL path {settings.STATIC_URL if settings_available else 'STATIC_URL'}")

print("\nRecommended fixes:")
print("1. Make sure the image file exists in the correct location:")
print(f"   - app_name/static/app_name/{IMAGE_NAME}")
print("2. For development, ensure DEBUG=True in settings.py")
print("3. For production, run 'python manage.py collectstatic'")
print("4. Check web server configuration for serving static files")