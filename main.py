import os
import sys
import pytest
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))
sys.path.append(root_path)

if __name__ == "__main__":
    print("Starting Teeeeest")
    pytest.main(['.', '-s',])
