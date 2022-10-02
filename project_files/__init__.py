from os import listdir, mkdir
from os.path import isdir, isfile
import yaml

from . import webpage_generator

if not isfile('./config.yaml'):
    with open('config.yaml', 'w') as config_file:
        default_config = {
            'config version': 0.1,
            'input': {
                'posts directory': './posts'
                },
            'output': {
                'index file location': './',
                'index file name': 'index.html',
                'subpages location': './pages'
                }
        }
        yaml.dump(default_config, config_file)
    print('No config.yaml file found. New config file was generated. Please configure your blog and run the program again.')
    exit()

with open('config.yaml', 'r') as config_file:
    config = yaml.load(config_file, yaml.FullLoader)

# TODO: missing directories and files creation
# if not isdir(config['input']['posts directory']):
#     mkdir(config['input']['posts directory'])


# generate index file
with open('index.html', 'w') as index_file:
    index_file.write(webpage_generator.generate_page(content='Habababa!'))
print('Your blog was generated successfully!')
