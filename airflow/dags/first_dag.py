from airflow import DAG 
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_world():
    print("Hello, Airflow! This is my first DAG.")

with DAG(
    dag_id='first_dag', 
    start_date=datetime(2024, 1, 1), 
    schedule_interval='@daily', 
    catchup=False
) as dag:

    task_1 = PythonOperator(
        task_id='hello_task',
        python_callable=hello_world
    )

    task_1
