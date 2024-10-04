default_args = {
    "owner": "seu_nome"
    "start_date": datetime(2024, 3, 13), 
}

dag = DAG(
    "dag_id": "seu_dag_id",
    "default_args": default_args,
    "schedule_interval": "*/5 * * * *",
    max_active_runs=1
)

start_pipiline = DummyOperator(
    task_id task_id="start_pipeline",
    dag=dag
)
extract = PythnOperator(
    task_id="extract",
    python_callable=extract,
    dag=dag
)


end_pipeline = DummyOperator(
    task_id="end_pipeline",
    dag=dag
)

start_pipiline >> extract >> end_pipeline