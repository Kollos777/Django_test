from django.db import connections

def mydatabase():
    conn = connections['default'].cursor()
    return conn
