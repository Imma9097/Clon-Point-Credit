import os

class Config:
    # Secret key for encrypting session data and other sensitive information
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'

    # Database configuration (MySQL)
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get('DATABASE_URL') or
        'mysql+pymysql://root:your_password@localhost/clon_point_credit'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Enable debug mode for development
    DEBUG = os.environ.get('FLASK_DEBUG', True)

    # JWT (JSON Web Token) configuration for authentication
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'your_jwt_secret_key'

    # CORS (Cross-Origin Resource Sharing) settings
    CORS_HEADERS = 'Content-Type'

# Optional: Different configurations for different environments (e.g., Development, Testing, Production)
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # Use production database URL

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use in-memory database for testing