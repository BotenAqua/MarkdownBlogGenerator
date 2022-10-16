from os.path import isfile, isdir
from os import mkdir, listdir
import yaml

from . import webpage_generator

if not isfile('./config.yaml'):
    with open('config.yaml', 'w') as config_file:
        with open('project_files/default_config.yaml', 'r') as default_config:
            config_file.write(default_config.read())
    print('No config.yaml file found. New config file was generated. '
          'Please configure your blog and run the program again.')
    exit()

with open('config.yaml', 'r') as config_file:
    config = yaml.load(config_file, yaml.FullLoader)

if not isdir(config['target directory']):
    mkdir(config['target directory'])
    print('Generated target directory.')

webGen = webpage_generator.WebpageGenerator(config)

# generate index file
webGen.generate_index()

# generate blog posts
# TODO: check subdirs for md files
for el in listdir(config['input directory']):
    if isfile(config['input directory']+'/'+el) and el[-3:] == '.md':
        webGen.generate_post(el)
        print('Generatated post from ' + el)

print('Your blog was generated successfully!')
