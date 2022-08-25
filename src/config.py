from decouple import config

class Config:
    SECRET_KEY= 'pass'

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development' : DevelopmentConfig
}

