# Lesson One - Data Pipelines #

## What is a Data Pipeline? ##

### Real World Examples of the Output of a Data Pipeline ###

- automated marketing emails

- real-time pricing for ride-share apps

- shopping online and then later saw ads for items which you had been considering but hadn't yet purchased

### Definition - What is a data pipeline ###

- a series of steps in which data is processed

- ETL steps are often found but each step is not strictly required

## Data Validation ##

### Definition ### 

- the process of ensuring that data is present, correct & meaningful

- data quality checks can be performed manually, but it is strongly preferred that it is automated and becomes a part of pipeline definitions

### Data Validation in Action ###

- assert that the same number of rows was maintained

- validate that values that should be greater than 0 are greater than 0, as in the bikesharing app example

- ensuring that the output matches the needs of the customer

### Why is this important? ###

- data pipelines provide a set of logical guidelines and a common set of terminology

- the conceptual framework of data pipelines will help you better organize and execute everyday data engineering tasks

## DAGs and Data Pipelines ## 

### Directed Acyclic Graphs (DAGs) ###

- data pipelines are well expressed as Directed Acyclic Graphs

- The conceptual framework of data pipelines will help to better organize and execute everyday data engineering tasks

### What is a graph? ###

- Graphs describe entities and the relationships between them

### Examples ###

- Social networks
    - model users as nodes and their relationships as edges

- Airlines
    - Airports are nodes
    - Edges are flights to other locations

### What is a DAG? ###

- DAGs consist of vertices, or nodes, & directed edges that connect to those nodes

- DAGs have a direction and DO NOT CONTAIN CYCLES

- a series of discrete steps

    - often described as extraction, tranformation, and load


## Bikeshare DAG ##

### Example ###

#### Initial Pipeline ####

- S3 -> Redshift

- Redshift Analysis

- Deliver Data

Then, you suspect you may want to incorporate another data source to get traffic info to place bikeshare hubs in optimal locations. So you add another edge to the graph.

## Apache Airflow ##

### Definition ###

- open source tool and platform to programattically author, schedule, and monitor workflows

### About ### 

- created by airBnB

- goals: 
    - DAG-based
    - schedule-able
    - data-pipeline tool
    - capable of running in mission-critical environments

### Why it is popular ###

- Airflow DAGs are written in python

- simple to maintain and can run data analysis itself or trigger external tools

- visual representation of the DAG

##