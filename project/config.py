# coding=utf-8
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Config:
    """Default configuration for all environments"""

    DEBUG = False
    TESTING = False
    APP_NAME = "Template"
    APPLICATION_ROOT = "/template"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "gjr39dkjn344_!67#"


class TestConfig(Config):
    """Configuration to run tests"""

    DEBUG = True
    TESTING = True
    DATABASE = os.path.join(BASE_DIR, "db_test.sqlite3")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, "db_test.sqlite3")


class DevConfig(Config):
    """Configuration to run in local environments"""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, "db.sqlite3")


class PreConfig(Config):
    """Configuration to run with docker and kubernetes in Preproduction"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, "db.sqlite3")


class ProdConfig(Config):
    """Configuration to run with docker and kubernetes in Production"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, "prod.db")


CONFIG = {
    "test": TestConfig,
    "dev": DevConfig,
    "pre": PreConfig,
    "prod": ProdConfig,
    "default": DevConfig
}
