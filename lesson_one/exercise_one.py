import datetime
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def greet():
    logging.info("hello world!")


dag = DAG(
        'lesson1.exercise1',
        start_date=datetime.datetime.now())

greet_task = PythonOperator(
   task_id="greet_task",
   python_callable=greet,
   dag=dag
)
