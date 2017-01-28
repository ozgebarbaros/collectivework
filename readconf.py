# -*- coding: utf-8 -*-
import configparser

from collectivework.settings import CONF_FILE


class DBConfig:
    db_host = None
    db_port = None
    db_name = None
    db_user = None
    db_pass = None

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(CONF_FILE)
        try:
            section = "DB"
            self.db_host = config.get(section, "host")
            self.db_port = config.get(section, "port")
            self.db_name = config.get(section, "name")
            self.db_user = config.get(section, "user")
            self.db_pass = config.get(section, "pass")
        except:
            pass

    def get_db_host(self):
        return self.db_host

    def get_db_port(self):
        return self.db_port

    def get_db_name(self):
        return self.db_name

    def get_db_user(self):
        return self.db_user

    def get_db_pass(self):
        return self.db_pass


class DjangoSettings:
    secret_key = None

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(CONF_FILE)
        try:
            section = "DJANGO"
            self.secret_key = config.get(section, "secret_key")
        except:
            pass

    def get_secret_key(self):
        return self.secret_key


class EmailSettings:
    host = None
    port = None
    username = None
    password = None
    from_address = None

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(CONF_FILE)
        try:
            section = "EMAIL"
            self.host = config.get(section, "host")
            self.port = config.get(section, "port")
            self.username = config.get(section, "user")
            self.password = config.get(section, "password")
            self.from_address = config.get(section, "from_address")
        except:
            pass

class TwitterConf:
    consumer_key = None
    consumer_secret = None

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(CONF_FILE)
        try:
            section = "TWITTER"
            self.consumer_key = config.get(section, "consumer_key")
            self.consumer_secret = config.get(section, "consumer_secret")
        except:
            pass

    def get_consumer_key(self):
        return self.consumer_key

    def get_consumer_secret(self):
        return self.consumer_secret
