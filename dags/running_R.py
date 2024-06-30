from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

# Define a Dag
dag = DAG(
    'R_world',
    description='A simple Dag tutorial',
    schedule_interval=None,
    start_date = datetime(2023,3,22)
)

#Define the Bash Operator task

run_R = BashOperator(
    task_id = "Run_R",
    bash_command='Rscript --no-save  /opt/airflow/dags/scripts/sample.r',
    dag=dag
)

run_R