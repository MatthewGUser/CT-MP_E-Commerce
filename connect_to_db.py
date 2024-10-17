from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def connect_db(app):
    # Fetch database credentials from environment variables
    db_username = os.getenv('DB_USERNAME', 'default_user')
    db_password = os.getenv('DB_PASSWORD', 'default_password')
    db_host = os.getenv('DB_HOST', 'localhost')
    db_port = os.getenv('DB_PORT', '3306')
    db_name = os.getenv('DB_NAME', 'ecommerce_db')

    # Set up the database URI using the credentials
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.app = app
    db.init_app(app)
