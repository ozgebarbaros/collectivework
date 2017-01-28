import configparser

from collectivework.settings import CONF_FILE

class DjangoSettings:
    secret_key = None

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(CONF_FILE)
        section = "DJANGO"
        self.secret_key = config.get(section, "secret_key")

    def get_secret_key(self):
        return self.secret_key