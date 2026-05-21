# main.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cli import ConsoleApplication

if __name__ == "__main__":
    app = ConsoleApplication()
    app.run()
