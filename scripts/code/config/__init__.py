import yaml

def read_config():
    paths = [
        "../config/g_config.yaml",
        "code/config/l_config.yaml",
    ]

    config = {}
    for path in paths:
        with open(path, "r") as file:
            temp_config = yaml.safe_load(file)
            config.update(temp_config)

    return config