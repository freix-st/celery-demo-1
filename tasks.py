import subprocess
import sys
from celery_app import app

@app.task
def run_daily_script():
    # run script as subprocess
    try:
        result = subprocess.run([
            sys.executable, './external_file.py'
        ], capture_output=True, text=True, check=True)
        print("[SUCCESS] Running daily script!")
    except subprocess.CalledProcessError as e:
        print(f"[FAILED] {e.stderr}")


@app.task
def generate_report():
    print("[SUCCESS] Generating report!")