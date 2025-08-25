from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="my_dag",
    start_date=datetime(2025, 8, 20),
    schedule_interval="@daily",
    catchup=False
) as dag:

    task1 = BashOperator(
        task_id="print_date",
        bash_command="date"
    )
