import os
import argparse
import subprocess
import webbrowser
#import constants
import sys


class Config:
    def __init__(self, name, **kwargs):
        """
        Creates a Config object
        
        optional keyword arguments:
            paths
            links
            browser
            browser_path
        """
        self.name = name
        self.paths = kwargs.get('paths')
        self.links = kwargs.get('links')
        self.browser = kwargs.get('browser')
        self.browser_path = kwargs.get('browser_path')

    @classmethod
    def from_file(cls, filename):
        with some_file_object as config_file:
            config_params = read_file_into_dict(config_file)
        return cls(name=filename_without_extension, **config_params)

    def open_file(self):
        try:
            self.file = open(os.path.join(constants.FOLDER_PATH, self.filename), "x")
        except FileExistsError as error:
            print(error)
            sys.exit()

    def write_paths(self):
        if self.paths:
            self.file.write("Paths: \n")
            for i in range(len(self.paths)):
                self.file.write(self.paths[i] + "\n")

    def write_links(self):
        if self.links:
            self.file.write("Links: \n")
            for i in range(len(self.links)):
                self.file.write(self.links[i] + "\n")

    def write_browser(self):
        if self.browser:
            self.file.write("Browser: \n")
            self.file.write(self.browser + "\n")

    def write_browser_path(self):
        if self.browser_path:
            self.file.write("Browser path: \n")
            self.file.write(self.browser_path + "\n")

    def close_file(self):
        self.file.close()

    def create_config(self):
        self.open_file()
        self.write_paths()
        self.write_browser()
        self.write_browser_path()
        self.write_links()
        self.close_file()

    def open_links(self, line):
        try:
            webbrowser.register(
                browser, None, webbrowser.BackgroundBrowser(browser_path)
            )
            webbrowser.get(browser).open_new_tab(line)
        except webbrowser.Error as error:
            print(error)

    def open_apps(self, line):
        try:
            subprocess.Popen(line)
        except subprocess.SubprocessError as error:
            print(error)

    def read_file(self):
        with open(os.path.join(constants.FOLDER_PATH, self.filename), "r") as file:
            for line in file.readlines():
                

    def execute(self):
        string_type = None
        self.read_file()

            line = line.strip()
            string_types = ["Paths:", "Links:", "Browser:", "Browser path:"]
            if not line:
                break
            if line in string_types:
                string_type = line
                continue
            if string_type == "Paths:":
                self.open_apps(line)
            elif string_type == "Browser:":
                self.browser = line
            elif string_type == "Browser path:":
                self.browser_path = line
            elif string_type == "Links:":
                self.open_links(line)

    def delete(self):
        try:
            file = os.path.join(constants.FOLDER_PATH, self.filename)
            os.remove(file)
        except FileNotFoundError as error:
            print(error)


def main():
    parser = argparse.ArgumentParser(description="Create, execute or delete a config")

    subparser = parser.add_subparsers(dest="command", required=True)

    parser_delete = subparser.add_parser("delete", help="Delete config")
    parser_delete.add_argument("filename", type=str, help="The file you want to delete")

    parser_execute = subparser.add_parser("execute", help="Execute config")
    parser_execute.add_argument(
        "filename", type=str, help="The file you want to execute"
    )

    parser_create = subparser.add_parser("create", help="Create config")
    parser_create.add_argument("-p", "--paths", type=str, nargs="*")
    parser_create.add_argument("-l", "--links", type=str, nargs="*")
    parser_create.add_argument("-b", "--browser", type=str)
    parser_create.add_argument("-bp", "--browserpath", type=str)
    required_args = parser_create.add_argument_group("required arguments")
    required_args.add_argument("-fn", "--filename", type=str, required=True)

    args = parser.parse_args()

    if args.command == "create":
        config = Config(
            args.filename, args.paths, args.links, args.browser, args.browserpath
        )
        if not os.path.exists(constants.FOLDER_PATH):
            os.makedirs(constants.FOLDER_PATH)
        config.create_config()
    elif args.command == "execute":
        config = Config(args.filename)
        config.execute()
    elif args.command == "delete":
        config = Config(args.filename)
        config.delete()


if __name__ == "__main__":
    main()
