import time
import os


class Logger(object):

    def __init__(
            self,
            init_log_level,
            init_log_message,
            *init_log_args,
            init_log_show_default=True,
            init_log_show_level_default="0:1:2:3:4:5",
            init_log_write_default=True,
            init_log_write_level_default="0:1:2:3:4:5",
            init_log_path_folder_default=os.path.join("src", "logs"),

    ):
        self.log_level = init_log_level
        self.log_message = init_log_message
        self.log_args = init_log_args
        self.log_show = init_log_show_default
        self.log_show_level = init_log_show_level_default
        self.log_write = init_log_write_default
        self.log_write_level = init_log_write_level_default
        self.log_path_folder = init_log_path_folder_default
        self.log_path_file = os.path.join(self.log_path_folder,
                                          str(time.strftime("%d-%m-%Y", time.localtime())) + ".txt")

    def add_folder(self):
        if not os.path.isdir(self.log_path_folder):
            os.mkdir(self.log_path_folder)

    def add_file(self, text_log):
        try:
            with open(self.log_path_file, "a+") as file:
                file.write(text_log)
        except Exception as Error:
            print(Error)

    def add_log(self, type_log, text_log):
        if self.log_level == 0:
            generate_level_log = "\n ~ "
            generate_level_log_new_line = "\n ~ "
        elif self.log_level == 1:
            generate_level_log = "\n   - "
            generate_level_log_new_line = "\n   - "
        elif self.log_level == 2:
            generate_level_log = "\n   - - "
            generate_level_log_new_line = "\n   - - "
        elif self.log_level == 3:
            generate_level_log = "\n   - - - "
            generate_level_log_new_line = "\n   - - - "
        elif self.log_level == 4:
            generate_level_log = "\n   - - - - "
            generate_level_log_new_line = "\n   - - - - "
        elif self.log_level == 5:
            generate_level_log = "\n   - - - - - "
            generate_level_log_new_line = "\n   - - - - - "
        else:
            generate_level_log = "\n[No-level] "
            generate_level_log_new_line = "\n[No-level] - "

        result_log = str(
            generate_level_log +
            time.strftime("%X", time.localtime()) +
            " " +
            type_log +
            generate_level_log_new_line +
            text_log + "\n"
        )

        if self.log_show:
            for level in self.log_show_level.split(":"):
                if int(level) == int(self.log_level):
                    print(result_log)

        if self.log_write:
            for level in self.log_write_level.split(":"):
                if int(level) == int(self.log_level):
                    self.add_folder()
                    self.add_file(result_log)

    def warning(self):
        self.add_log("[WARNING]", self.log_message)

    def error(self):
        self.add_log("[ERROR]", self.log_message)

    def success(self):
        self.add_log("[SUCCESS]", self.log_message)

    def running(self):
        self.add_log("[RUN]", self.log_message)

    def info(self):
        self.add_log("[INFO]", self.log_message)

    def fatal(self):
        exit(self.add_log("[FATAL]", self.log_message))


if __name__ == "__main__":
    pass
