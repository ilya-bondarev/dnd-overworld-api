class Config:
    db_type = 'postgresql'
    username = 'username'
    password = 'password'
    host = 'localhost'
    database_name = 'database_name'

    SQLALCHEMY_DATABASE_URI = f'{db_type}://{username}:{password}@{host}/{database_name}'