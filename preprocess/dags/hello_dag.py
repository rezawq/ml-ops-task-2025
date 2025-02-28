from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

# Define the DAG
dag = DAG(
    'hello_world_dag',  # DAG ID
    default_args=default_args,
    description='A simple Hello World DAG',
    schedule_interval=timedelta(minutes=1),
    catchup=False,  # Disable catchup to avoid backfilling
)

# Define a Python function to print "Hello World"
def print_hello():
    print("Hello World!")

# Create a task using the PythonOperator
hello_task = PythonOperator(
    task_id='hello_task',  # Task ID
    python_callable=print_hello,  # Function to execute
    dag=dag,  # Assign the DAG
)

# No need to reference `hello_task` at the end of the file