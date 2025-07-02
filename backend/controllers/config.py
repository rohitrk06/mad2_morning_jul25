class Config:
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    SECURITY_PASSWORD_SALT = 'your_password_salt_here'
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'