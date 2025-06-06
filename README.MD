# Celery demo

Shows basic use of celery for scheduling scripts that are meant to run regularly

Good celery tutorials:

[Medium.com - Hands-on Learn Python Celery In 30 Minutes](https://lip17.medium.com/hands-on-learn-python-celery-in-30-minutes-9544aabb70b1)

[Medium.com - Mastering Celery: A Guide to Background Tasks, Workers, and Parallel Processing in Python](https://khairi-brahmi.medium.com/mastering-celery-a-guide-to-background-tasks-workers-and-parallel-processing-in-python-eea575928c52)

## Beat and worker
When running scheduled tasks, Celery has two components - Beat and Worker.

For **BEAT**, think beat as in having a steady rhythm. Beat will distribute tasks based on the schedule given.

The **WORKER** is the one that handles the tasks that Beat will throw. If there are not enough workers available, then 
you will have to wait for one to finish a task to be available. The max tasks that are being processed by worker is 
set using the ```--concurrency``` switch or simply ```-c```

---
If you want to run a task periodically using the scheduling functionality (similar to a cronjob), then you need to 
run both. Hence the need for ```celery_start.sh```

<br />
If only one is running, it won't work (either no tasks being delegated, 
or no tasks being processed). 
You 
can of course also delegate manually through script though with the ```.delay``` functionality.