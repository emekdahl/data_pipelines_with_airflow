# Data Pipelines #

### How Airflow Works ###

#### What makes up Airflow? ####

- scheduler: for orchestrating execution of jobs on a trigger or schedule
    - starts DAGs based on time or external triggers
    - analyzes the tasks that make up the DAG and selects the tasks that have no dependencies and runs them first
    - then, tasks are placed in the queue
- Work queue which holds the state of running DAGS and Tasks
    - as work arrives in the queue, the workers pick up the tasks and run them
    - as tasks are completed, the worker passes that info to the scheduler and the scheduler updates
    - once all tasks have been completed, the run is considered complete
- Worker Processes that execute the operations defined in each DAG
    - workers work with other dbs like spark, redshift, and so on
- Database which saves creds, connections, history, and configuration
    - strictly a meta-data db
- Web interface which provides a control dashboard for users and maintainers

** caveat : airflow only has the processing power of one machine, so you don't do the heavy processing of data on these servers.
Rather, you use it to schedule and kick off the workers


### Operators and Tasks ###

#### Building a Data Pipeline in Airflow ####

- Airflow comes with many operators out of the box that can perform common operations 

    - PythonOperator
    - PostgresOperator
    - RedshiftToS3Operator
    - S3ToRedshiftOperator
    - BashOperator
    - SimpleHttpOperator
    - Sensor
    
#### Task Dependencies ####

##### Airflow Dags #####

- nodes = tasks
- edges = ordering and dependencies between tasks

Option 1:
- task dependencies can be described programmatically in Airflow using >> and <<

Option 2:
- Task dependencies can also be set with "set_downstream" and "set_upstream"


#### Airflow Hooks

Connections can be accessed in code via hooks

- Hooks provide a resuable interface to external systems and databases
- You don't have to worry about how and where to store these connection strings and secrets in your code

Hooks:
- HttpHook
- PostgresHook (works with RedShift)
- MySqlHook
- SlackHook
- PrestoHook


#### Templating

Airflow leverages templating to allow users to "fill in the blank" with important runtime variables for tasks
