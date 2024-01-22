import configparser
from model.RandomConfig import RandomConfig


class Config:
    def __init__(self, random, default_filename, random_config):
        self.random = random.lower() == 'true'
        self.default_filename = default_filename == 'true'
        self.random_config = random_config


def parse_config():
    config = configparser.RawConfigParser()
    config.read('ConfigFile.properties')
    return Config(
        config.get('Mode', 'random'),
        config.get('Mode', 'default_filename'),
        RandomConfig(config.get('Random', 'min'), config.get('Random', 'max'), config.get('Random', 'count'), config.get('Random', 'scale'))
    )
