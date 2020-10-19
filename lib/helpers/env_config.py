import os
import yaml

class EnvConfig():
    def environment_config_for(key):
        # read production url.
        # get the full path for this file.
        full_file_path = os.path.realpath(__file__)
        # print(full_file_path)
        file_dirname = os.path.dirname(full_file_path)
        # print(file_dirname)
        parent_dirname = os.path.dirname(file_dirname)
        # print(parent_dirname)
        grand_parent_dirname = os.path.dirname(parent_dirname)
        # print(grand_parent_dirname)
        path_to_config_yml = os.path.join(grand_parent_dirname, 'config.yml')
        # print(path_to_config_yml)

        # The with function opens the file, in this case the yaml file.
        with open(path_to_config_yml) as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            url = data[os.environ.get('ENV')][key]

        return url

