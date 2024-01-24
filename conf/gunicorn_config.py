command = '/home/viktor/Documents/projects/healthaid/backend/env/bin/gunicorn'
pythonpath = '/home/viktor/Documents/projects/healthaid/backend/eduhack'
bind = '127.0.0.1:8004'
workers = 3

# run gunicorn -c conf/gunicorn_config.py eduhack.wsgi
# And the press ctrl z to run server at the backgrund
# run "pkill gunicorn" to kill server