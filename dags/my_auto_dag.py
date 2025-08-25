from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_task():
    print("Hello from my_auto_dag!")

with DAG(
    dag_id="my_auto_dag",
    start_date=datetime(2025, 8, 20),
    schedule_interval="@daily",
    catchup=False
) as dag:
    task1 = PythonOperator(
        task_id="print_hello",
        python_callable=hello_task
    )
