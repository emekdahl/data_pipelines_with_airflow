import datetime
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def hello_world():
    logging.info("Hello World")

dag = DAG(
        "lesson1.exercise2",
        start_date=datetime.datetime.now() - datetime.timedelta(days=60),
        schedule_interval="@monthly")

task = PythonOperator(
        task_id="hello_world_task",
        python_callable=hello_world,
        dag=dag)
