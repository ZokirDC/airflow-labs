
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def hello_world():
    print("Hello, Airflow!")

with DAG(
    'my_first_dag',
    description='My first DAG',
    schedule_interval='@daily',
    start_date=datetime(2025, 8, 20),
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id='hello_task',
        python_callable=hello_world
    )
