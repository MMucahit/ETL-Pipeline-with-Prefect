# ETL-PipeLine with Prefect

<b> This project read csv file which is in local file system, transform it and write PostgreSql database </br></b>
<b> Follow below instructions to run project </br></b>

Database = PostgreSQL (on Docker) (http://localhost:8080) </br>
Prefect = Local (http://127.0.0.1:4200/) </br>

Start prefect ui: </br>
* prefect server start

Create Blocks (Storage, Process): </br>
* python blx.py

How to Learn blocks-slug to use create Deployments: </br>
* prefect blocks ls
  -sb {local-file-system/slug}
  -ib {process/slug}

Create Deployments with terminal: </br>
* prefect deployment build 
  -n titanic-dep 
  -sb local-file-system/titanic-storage-block 
  -ib process/titanic-process-infra 
  Transform.py:main --apply

How to start agent: </br>
* prefect agent start -q 'default'
