Welcome to tutorial to run R in airflow docker
Apache airflow is an open source platform that allows us to create, schedule and monitor workflows through programming.

Most of the scripts that we see as a sample to learn airflow is basically in python. In this git repository we will see how can we run r-scripts in airflow in docker. This tutorial is to setup docker in windows and run airflow within docker

STEP 1: Install Docker 
https://docs.docker.com/desktop/install/windows-install/
SETP 2: Install apache-airflow in docker
https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
STEP 3: Install R
1) open console and copy <b> docker exec -u root -it <container_id> /bin/bash </b>
NOTE: In airflow we will install R in airflow worker because worker is responsible to run or execute our dags. So far container id I used my airflow worker container_id which you can easily find using <b> Docker ps </b>
2) I follwed https://gcore.com/learning/how-to-install-r-on-ubuntu/
3) Now you are ready to run rscripts in airflow




