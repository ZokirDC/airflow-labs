from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Функция для таска
def print_hello():
    print("Привет, Зокир! Этот DAG уникальный!")

# Создаём DAG
with DAG(
    dag_id='zokir12345_unique_dag',  # уникальный id
    start_date=datetime(2025, 8, 20),
    schedule_interval='@daily',
    catchup=False,
    default_args={
        'owner': 'dataadmin',
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
    },
) as dag:

    task_hello = PythonOperator(
        task_id='say_hello',
        python_callable=print_hello
    )

    task_hello
