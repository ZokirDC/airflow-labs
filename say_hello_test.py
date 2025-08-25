from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def say_hello_test():
    print("Hello World from Airflow! Test DAG")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='say_hello_test',
    default_args=default_args,
    description='Тестовый DAG для автоматизации',
    schedule_interval='* * * * *',  # запуск каждую минуту
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=['test'],
) as dag:
    
    hello_task = PythonOperator(
        task_id='hello_task_test',
        python_callable=say_hello_test,
    )
