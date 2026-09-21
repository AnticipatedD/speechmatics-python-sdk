import sys
from pathlib import Path

# Automatically inject the src directory into the Python path for all test runs
root_dir = Path(__file__).resolve().parent
src_dir = root_dir / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))
