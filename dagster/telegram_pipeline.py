from dagster import job, op, Out, In, String, ScheduleDefinition
import subprocess
import os

# Define ops
@op(out=Out(String))
def scrape_telegram_data():
    """Scrape Telegram data and return the raw data path."""
    raw_path = "C:/Users/Daniel.Temesgen/Desktop/KIAM/Shipping a Data Product From Raw Telegram Data to an Analytical API/data/raw/telegram_messages/2025-07-DD"
    script_path = "C:/Users/Daniel.Temesgen/Desktop/KIAM/Shipping a Data Product From Raw Telegram Data to an Analytical API/src/scraper.py"
    subprocess.run([
        "C:/Users/Daniel.Temesgen/Desktop/KIAM/Shipping a Data Product From Raw Telegram Data to an Analytical API/week7/Scripts/python.exe",
        script_path
    ], check=True)
    return raw_path

@op(ins={"raw_path": In(String)}, out=Out(String))
def load_raw_to_postgres(raw_path):
    """Load scraped data into PostgreSQL raw tables."""
    dbt_path = "C:/Users/Daniel.Temesgen/Desktop/KIAM/Shipping a Data Product From Raw Telegram Data to an Analytical API/dbt-demo/telegrahm_dbt"
    subprocess.run([
        "C:/Users/Daniel.Temesgen/Desktop/KIAM/Shipping a Data Product From Raw Telegram Data to an Analytical API/week7/Scripts/dbt.exe",
        "run", "--project-dir", dbt_path, "--select", "stg_messages"
    ], check=True)
    return dbt_path

@op(ins={"dbt_path": In(String)}, out=Out(String))
def run_dbt_transformations(dbt_path):
    """Run dbt transformations to create data marts."""
    subprocess.run([
        "C:/Users/Daniel.Temesgen/Desktop/KIAM/Shipping a Data Product From Raw Telegram Data to an Analytical API/week7/Scripts/dbt.exe",
        "run", "--project-dir", dbt_path
    ], check=True)
    return dbt_path

@op(ins={"dbt_path": In(String)})
def run_yolo_enrichment(dbt_path):
    """Run YOLO enrichment on images and store detections."""
    script_path = "C:/Users/Daniel.Temesgen/Desktop/KIAM/Shipping a Data Product From Raw Telegram Data to an Analytical API/src/process_images.py"
    subprocess.run([
        "C:/Users/Daniel.Temesgen/Desktop/KIAM/Shipping a Data Product From Raw Telegram Data to an Analytical API/week7/Scripts/python.exe",
        script_path
    ], check=True)
    subprocess.run([
        "C:/Users/Daniel.Temesgen/Desktop/KIAM/Shipping a Data Product From Raw Telegram Data to an Analytical API/week7/Scripts/dbt.exe",
        "run", "--project-dir", dbt_path, "--select", "fct_image_detections"
    ], check=True)

# Define the job
@job
def telegram_pipeline():
    raw_path = scrape_telegram_data()
    dbt_path = load_raw_to_postgres(raw_path)
    run_dbt_transformations(dbt_path)
    run_yolo_enrichment(dbt_path)

# Define a schedule
telegram_schedule = ScheduleDefinition(
    job=telegram_pipeline,
    cron_schedule="0 0 * * *",  # Runs daily at midnight UTC (3:00 AM EAT)
)