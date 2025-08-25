# ./dags/test_dag.py

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Функция для PythonOperator
def hello_world(**kwargs):
    print("Hello, Airflow!")

# Объявление DAG
with DAG(
    dag_id="test_dag",
    start_date=datetime(2025, 8, 20),
    schedule_interval="@daily",  # ежедневный запуск
    catchup=False,               # пропуск старых дат
    tags=["test"]
) as dag:

    task_hello = PythonOperator(
        task_id="hello_task",
        python_callable=hello_world
    )

    task_hello  # единственная задача

