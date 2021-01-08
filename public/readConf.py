import configparser
import os


class ReadConf():

    def readconf(self, section, value):
        config = configparser.ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/public/config.ini'
        file_path=os.getcwd()+'/public/config.ini'
        config.read(file_path,encoding="utf-8")
        item = config.get(section, value)
        return item
