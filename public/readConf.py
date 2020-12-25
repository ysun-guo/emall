import configparser
import os


class ReadConf():

    def readconf(self, section, value):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.getcwd()) + '/public/config.ini'
        config.read(file_path)
        item = config.get(section, value)
        return item


if __name__ == '__main__':
    test = ReadConf()
    t = test.readconf('URL', "homeURL")  # 传入sections的值
    print(t)
