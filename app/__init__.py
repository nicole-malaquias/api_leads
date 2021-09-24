from flask import Flask
from environs import Env
from app.configs import database, migrations, env_configs
from app import views 

env = Env()
env.read_env()

def create_app():
    app = Flask(__name__)
    env_configs.init_app(app)
    
    database.init_app(app)
    migrations.init_app(app)
    
    views.init_app(app)
    return app



