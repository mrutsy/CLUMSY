import configparser
import os


class Parser(object):

    def __init__(self):
        self.paths = None
        self.parser = None
        self.parser = None

    def init(self, *path):
        self.parser = configparser.ConfigParser()
        self.paths = os.path.join(*path)
        self.parser.read(self.paths)
        return self

    def get(self, section, option, split=None):
        result = "Bye bye..."
        try:
            if split:
                result = self.parser.get(section, option).split(":")
            else:
                result = self.parser.get(section, option)
        except Exception as Error:
            print(self.paths)
            print(Error)
        finally:
            return result

    def get_sections(self):
        result = self.parser.sections()
        return result

    def set(self, section, option, text):
        result = "Bye bye..."
        try:
            result = self.parser.set(section, option, text)

            with open(self.paths, "w") as config_file:
                self.parser.write(config_file)
        except Exception as Error:
            print(self.paths)
            print(Error)
        finally:
            return result

    # @staticmethod
    # def create_config(path):
    #     """
    #     Create a config file
    #     """
    #     config = configparser.ConfigParser()
    #     config.add_section("Settings")
    #     config.set("Settings", "font", "Courier")
    #     config.set("Settings", "font_size", "10")
    #     config.set("Settings", "font_style", "Normal")
    #     config.set("Settings", "font_info",
    #                "You are using %(font)s at %(font_size)s pt")
    #
    #     with open(path, "w") as config_file:
    #         config.write(config_file)
    #
    # def get(self, path):
    #     """
    #     Returns the config object
    #     """
    #     if not os.path.exists(path):
    #         self.create_config(path)
    #
    #     config = configparser.ConfigParser()
    #     config.read(path)
    #     return config
    #
    # def get(self, path, section, setting):
    #     """
    #     Print out a setting
    #     """
    #     config = self.get_config(path)
    #     value = config.get(section, setting)
    #     msg = "{section} {setting} is {value}".format(
    #         section=section, setting=setting, value=value
    #     )
    #
    #     print(msg)
    #     return value
    #
    # def set(self, path, section, setting, value):
    #     """
    #     Update a setting
    #     """
    #     config = self.get_config(path)
    #     config.set(section, setting, value)
    #     with open(path, "w") as config_file:
    #         config.write(config_file)
    #
    # def delete(self, path, section, setting):
    #     """
    #     Delete a setting
    #     """
    #     config = self.get_config(path)
    #     config.remove_option(section, setting)
    #     with open(path, "w") as config_file:
    #         config.write(config_file)

