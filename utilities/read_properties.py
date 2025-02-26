import configparser



#READ CONFIG FOLDER
config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_Config:
    @staticmethod
    def get_admin_page_url():
        return config.get("admin login info", "admin_page_url")

    @staticmethod
    def get_username():
        return config.get("admin login info", "username")

    @staticmethod
    def get_password():
        return config.get("admin login info", "password")

    @staticmethod
    def get_invalid_username():
        return config.get("admin login info", "invalid_username")