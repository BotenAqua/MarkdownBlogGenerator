from markdown import Markdown

md = Markdown(extensions = ['meta'])

def demarkdownifier(content):
    html = md.convert(content)
    metadata =md.Meta
    return {'html':html, 'metadata':metadata}
