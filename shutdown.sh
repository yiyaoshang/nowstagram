ps -ef|grep gunicorn|awk '{print $2}'|xargs kill -9
