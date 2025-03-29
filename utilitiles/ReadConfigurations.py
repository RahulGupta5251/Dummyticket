from configparser import ConfigParser


def readconfigurations(category ,key):
    config = ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category ,key)