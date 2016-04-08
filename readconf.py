# -*- coding: utf-8 -*-
import ConfigParser
from collectivework.settings import CONF_FILE

class DBconfig:
    dbhost = None
    dbport = None
    database = None
    dbuser = None
    dbpass = None

    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read(CONF_FILE)
        section = "DB"
        self.dbhost = config.get(section, "host")
        self.dbport = config.get(section, "port")
        self.database = config.get(section, "database")
        self.dbuser = config.get(section, "dbuser")
        self.dbpass = config.get(section, "pass")

    def getdbhost(self):
        return self.dbhost

    def getdbport(self):
        return self.dbport

    def getdatabase(self):
        return self.database

    def getdbuser(self):
        return self.dbuser

    def getdbpass(self):
        return self.dbpass

class DjangoSettings:
    secret_key = None

    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read(CONF_FILE)
        section = "DJANGO"
        self.secret_key = config.get(section, "secret_key")

    def getsecretkey(self):
        return self.secret_key


class EmailSettings:
    host = None
    port = None
    username = None
    password = None
    fromaddress = None

    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read(CONF_FILE)
        section = "EMAIL"
        self.host = config.get(section, "host")
        self.port = config.get(section, "port")
        self.username = config.get(section, "user")
        #self.password = config.get(section, "password")
        self.fromaddress = config.get(section, "fromaddress")


class TwitterConf:
    customerkey = None
    customersecret = None

    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read(CONF_FILE)
        section = "TWITTER"
        self.customerkey = config.get(section, "customerkey")
        self.customersecret = config.get(section, "customersecret")

    def getcustomerkey(self):
        return self.customerkey
    
    def getcustomersecret(self):
        return self.customersecret

