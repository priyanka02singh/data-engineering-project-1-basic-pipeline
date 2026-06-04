from airflow import DAG 
from airflow.operators.python import PythonOperator 
from datetime import datetime 
import sys 

def check_environment():
    print("Airflow is working!") 
    print(f"Python version: {sys.version}") 

with DAG( 
    dag_id='test_setup', 
    start_date=datetime(2024, 1, 1), 
    schedule_interval=None, 
    catchup=False
) as dag:
    
    check_task = PythonOperator(
        task_id='check_environment_task', 
        python_callable=check_environment
    )
    check_task
