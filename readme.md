# speed reading repository
This repository is intended to create environment for speed reading and contemplating everything written without leaving
leaving anything.
In this first we will create compression and then ask few question related to given comprehension to test whether you have
understood it correctly.


# gunicorn setup
envs:
    APP_DB=mysql+pymysql://root:root@127.0.0.1:3306/speed;FLASK_DEBUG=1;SQLALCHEMY_ECHO=1;SQLALCHEMY_POOL_SIZE=10;SQLALCHEMY_MAX_OVERFLOW=10;SQLALCHEMY_POOL_PRE_PING=1
    
params:
    -c config/gunicorn_config.py -b 127.0.0.1:9000 --log-level DEBUG main:app_instance
    
# Database 
 Creating database name speed