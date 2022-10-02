from os import listdir
from os.path import isdir, isfile
import yaml

from . import webpage_generator

if not isfile('./config.yaml'):
    with open('config.yaml', 'w') as config_file:
        config = [
            {
                'posts': {
                    'posts_directory': './posts'
                    }
            }
        ]
        yaml.dump(config, config_file)
    print('No config.yaml file found. New config file was generated.')
    exit()

print(webpage_generator.generate_page(content='Habababa!'))
