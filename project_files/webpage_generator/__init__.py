from jinja2 import Template

def generate_page(content):
    page = Template('This is a test! The content you provided is: {{ page_content }}')
    return page.render(page_content=content)
