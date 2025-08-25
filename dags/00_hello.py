from datetime import datetime
from airflow import DAG
from airflow.decorators import task

with DAG(
    dag_id="hello_world",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["test"],
) as dag:

    @task
    def say_hello():
        print("Hello from Airflow!")

    say_hello()
