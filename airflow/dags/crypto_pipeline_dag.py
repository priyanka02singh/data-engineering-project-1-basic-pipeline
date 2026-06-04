from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    dag_id='crypto_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    extract = BashOperator(
        task_id='extract_task',
        bash_command=""" 
        curl -s 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd' > /tmp/crypto.json 
        echo "Data extracted successfully"  
        """
    )

    transform = BashOperator(
        task_id='transform_task',
        bash_command="""
        cat /tmp/crypto.json | python -m json.tool > /tmp/crypto_clean.json
        echo "Data transformed successfully"
        """
    )
    
    load = BashOperator(
        task_id='load_task',
        bash_command="""
        echo "Loading data into Postgres..."
        echo "SELECT * FROM crypto_data;" > /tmp/load_log.txt
        echo "Load step completed"
        """
    )

    extract >> transform >> load
