from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator


default_args = {
    'owner': 'marcin',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    dag_id='0_second_dag',
    default_args=default_args,
    start_date=datetime(2021, 12, 19),
    schedule_interval="@once",
) as dag:
    task1 = PostgresOperator(
        task_id='create_postgres_table',
        postgres_conn_id='postgres_localhost',
        sql="""
            create table if not exists dag_runs (
                dt date,
                dag_id character varying,
                primary key (dt, dag_id)
            )
        """
    )


    task1