from jinja2 import FileSystemLoader, Environment
from . import markdown_pages
from . import generator

file_loader = FileSystemLoader('./project_files/templates') # TODO: path changing

env = Environment(loader=file_loader)
env.trim_blocks = True
env.lstrip_blocks = True
env.rstrip_blocks = True

template = env.get_template('base.html')


def generate_page(content='', title='Default title', language='en'):
    return template.render(content=content)

print(env.get_template('post.html').render(content='TEST'))
