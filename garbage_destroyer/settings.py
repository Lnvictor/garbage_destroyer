from configparser import ConfigParser
import os


config = ConfigParser()
config.read(os.path.abspath(os.curdir) + '/garbage_destroyer/config.ini')
