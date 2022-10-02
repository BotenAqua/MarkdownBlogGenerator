from jinja2 import FileSystemLoader, Environment

file_loader = FileSystemLoader('./project_files/templates') # TODO: path changing

env = Environment(loader=file_loader)
env.trim_blocks = True
env.lstrip_blocks = True
env.rstrip_blocks = True

from pathlib import Path
mypath = Path().absolute()
print('Absolute path : {}'.format(mypath))

template = env.get_template('base.html')


def generate_page(content='', title='Default title', language='en'):
    return template.render(content=content)
