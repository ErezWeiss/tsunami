# tsunami
Dear everybody :)

## Quickstart:
clone the repo, run docker compose up, and see in localhost:5000 the alerts.

## The story
Disclaimer: You asked me to do the task till Wednesday, but I had only today for this task, due to other processes - hope you will like what I've done though.

1. I chose to implemnt the task with docker-compose, to demonstrate a micro production env. With more time I would implement it with k8s and Prometheus of course.
2. The docker compose will create the Tsunami, alertManager for scraping the logs, flask server to show the alerts, redis to save the state, and Jupiter notebook with no password - to catch a vulnerability.
3. Tsunami will test only localhost for this demo - due to my time, other hosts ips can easly be added in the Dockerfile of the tsunami. (python script that will iterate over text file of ips, for instance)  .
4. Tsunami runs in loops forever and update the logs file. alertManager microservice scrape the log and update the redis DB. Whenever one is refreshing the flask ui - it will ask the db for the status.
5. First result in this DB will appear after like 15 mins, at the time when the first scan will be ended.