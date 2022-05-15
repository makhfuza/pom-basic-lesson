import configparser

config = configparser.RawConfigParser()
config.read(r'.\configs\config.ini')

class ReadConfig:
    @staticmethod
    def get_app_url():
        return config.get('common info', 'url')

    @staticmethod
    def valid_username():
        return config.get('common info', 'valid_username')

    @staticmethod
    def valid_password():
        return config.get('common info', 'valid_password')