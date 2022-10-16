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

        self.posts_directory = config['input directory']
        self.target_directory = config['target directory'] + '/'
        self.post_template = self.env.get_template('post.html')
        self.index_template = self.env.get_template('base.html')
        return

    def _md_html(self, content):
        return {'html': self.md.convert(content), 'metadata': self.md.Meta}


    def _generate_page(self, directory, template, context):
        with open(directory, 'w') as new_page:
            md_data = self._md_html(context)
            metadata = md_data['metadata']
            content = md_data['html']
            new_page.write(self.env.get_template(template)
                .render(metadata=metadata, content=content))
        return


    def generate_post(self, post_filename):
        # TODO: Check if post exists and is the same
        source_file = self.posts_directory + '/' + post_filename
        page_directory = self.target_directory+post_filename[:-2]+'html'
        with open(source_file, 'r') as source_file:
            self._generate_page(page_directory,
                                self.post_template,
                                source_file.read())
        return


    def generate_index(self):
        self._generate_page('./index.html',  self.index_template, '')
        print('Index file generated.')
        return
    pass
