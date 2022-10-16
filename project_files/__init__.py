from os.path import isfile, isdir
from os import mkdir
import yaml

from . import webpage_generator

if not isfile('./config.yaml'):
    with open('config.yaml', 'w') as config_file:
        default_config = {
            'config version': 0.1,
            'target directory': './pages',
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
    print('No config.yaml file found. New config file was generated. '
          'Please configure your blog and run the program again.')
    exit()

with open('config.yaml', 'r') as config_file:
    config = yaml.load(config_file, yaml.FullLoader)

# TODO: missing directories and files creation
# if not isdir(config['input']['posts directory']):
#     mkdir(config['input']['posts directory'])
if not isdir(config['target directory']):
    mkdir(config['target directory'])

webGen = webpage_generator.WebpageGenerator(config)

# generate index file
webGen.generate_index()

# generate blog posts
webGen.generate_post('test.html')

print('Your blog was generated successfully!')
