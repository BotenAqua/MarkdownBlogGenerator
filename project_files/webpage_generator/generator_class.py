from jinja2 import FileSystemLoader, Environment
from markdown import Markdown

class WebpageGenerator:

    def __init__(self, config):
        self.file_loader = FileSystemLoader('./project_files/templates')  #get path from init
        self.env = Environment(loader=self.file_loader)
        self.env.trim_blocks = True
        self.env.lstrip_blocks = True
        self.env.rstrip_blocks = True

        self.md = Markdown(extensions = ['meta'])

        self.target_directory = config['target directory'] + '/'
        self.post_template = self.env.get_template('post.html')
        self.index_template = self.env.get_template('base.html')
        return

    def _md_html(self, content):
        return {'html': md.convert(content), 'metadata': md.Meta}


    def _generate_page(self, directory, template, content = ''):
        print(directory)
        with open(directory, 'w') as new_page:

            new_page.write(self.env.get_template(template).render(content))
        return

    def generate_post(self, post_filename):
        # TODO: Check if post exists and is the same
        self._generate_page(self.target_directory+post_filename, self.post_template)
        return

    def generate_index(self):
        # TODO: Check if post exists and is the same
        self._generate_page('./index.html', self.index_template)
        return
    pass
