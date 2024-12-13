from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator

from datetime import datetime, timedelta
import sys
import os

# Define default_args
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'update_google_sheet_with_sat_data',
    default_args=default_args,
    description='Run app.py every 15 minutes',
    schedule_interval='*/15 * * * *',
    start_date=datetime(2023, 12, 12),
    catchup=False,
)

# Define the Python function wrapper
def run_app():
    project_dir = os.path.join(os.path.dirname(__file__), 'project')
    sys.path.insert(0, project_dir)
    os.chdir(project_dir)
    from app import main  # Assuming your main function is called 'main'
    main()

# Add a PythonOperator
run_app_task = PythonOperator(
    task_id='run_app',
    python_callable=run_app,
    dag=dag,
)

start_task = DummyOperator(
    task_id='start',
    dag=dag,
)

end_task = DummyOperator(
    task_id='end',
    dag=dag,
)

start_task >> run_app_task >> end_task