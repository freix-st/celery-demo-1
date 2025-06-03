from celery_app import app

@app.task
def run_daily_script():
    print("[SUCCESS] Running daily script!")

@app.task
def generate_report():
    print("[SUCCESS] Generating report!")