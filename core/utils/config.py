import configparser


# Params: abs file path, file section and its key
def get_config_value(conf_file, section, key):
    config = configparser.ConfigParser()
    config.read(conf_file)

    return config[section][key]
