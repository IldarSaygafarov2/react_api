import multiprocessing

bind = '127.0.0.1:5000'  # с каким локальным хостом связывается gunicorn
workers = multiprocessing.cpu_count() + 1
user = 'root'
timeout = 120