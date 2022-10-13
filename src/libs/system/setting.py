import src.libs.system as system
import os.path


class Setting(object):

    def __init__(
            self,
            init_setting_path_default=os.path.join("src", "configs", "setting.ini")
    ):
        self.setting_file_path = init_setting_path_default
        self.setting_object = system.Parser(self.setting_file_path)

        self.setting_section = None
        self.setting_option = None

    def language_current(self):
        self.setting_section = "language"
        self.setting_option = "current"
        return self

    def language_default(self):
        self.setting_section = "language"
        self.setting_option = "default"
        return self

    def get(self):
        result = self.setting_object.get(self.setting_section, self.setting_option)
        return result

    def set(self, value):
        result = self.setting_object.s
        # try:
        #     with open(self.setting_file_path, "a+") as file:
        #         file.write(text_log)
        # except Exception as Error:
        #     print(Error)
