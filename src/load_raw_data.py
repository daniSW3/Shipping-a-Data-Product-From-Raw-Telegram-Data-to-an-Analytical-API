import json
import logging
import os
from datetime import datetime
import psycopg2
from psycopg2.extras import Json

# Configure logging
logging.basicConfig(
    filename='raw_data_loader.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# PostgreSQL connection parameters
db_params = {
    'host': 'localhost',
    'port': 5432,
    'database': 'dbt',  # Updated to match current database
    'user': 'postgres',
    'password': 'admin3542'  # Replace with your PostgreSQL password
}

# Data lake base path
DATA_LAKE_PATH = 'C:/Users/Daniel.Temesgen/Desktop/KIAM/Shipping a Data Product From Raw Telegram Data to an Analytical API/data/raw/telegram_messages'

def create_raw_table(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE SCHEMA IF NOT EXISTS raw;
                CREATE TABLE IF NOT EXISTS raw.telegram_messages (
                    id SERIAL PRIMARY KEY,
                    channel_name VARCHAR(255),
                    date DATE,
                    message_data JSONB
                );
            """)
            conn.commit()
            logger.info("Created raw.telegram_messages table")
    except Exception as e:
        logger.error(f"Error creating raw table: {str(e)}")
        conn.rollback()
        raise

def load_json_files():
    conn = None
    try:
        conn = psycopg2.connect(**db_params)
        create_raw_table(conn)
        
        for root, _, files in os.walk(DATA_LAKE_PATH):
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    parts = root.split(os.sep)
                    if len(parts) >= 3 and parts[-2].startswith('2025-07-'):
                        channel_name = parts[-1]
                        date_str = parts[-2]
                        try:
                            date = datetime.strptime(date_str, '%Y-%m-%d').date()
                        except ValueError:
                            logger.warning(f"Invalid date format in path: {root}")
                            continue
                        
                        with open(file_path, 'r', encoding='utf-8') as f:
                            messages = json.load(f)
                        
                        with conn.cursor() as cur:
                            for message in messages:
                                cur.execute("""
                                    INSERT INTO raw.telegram_messages (channel_name, date, message_data)
                                    VALUES (%s, %s, %s)
                                """, (channel_name, date, Json(message)))
                            conn.commit()
                            logger.info(f"Loaded {len(messages)} messages from {file_path}")
                            
    except Exception as e:
        logger.error(f"Error loading data: {str(e)}")
        raise
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    load_json_files()
