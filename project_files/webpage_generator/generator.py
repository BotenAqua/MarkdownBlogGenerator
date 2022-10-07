from os import listdir, mkdir
from os.path import isfile

from . import markdown_pages


def _create_directory(directory: str):
    mkdir(directory)
    return


def _generate_page():
    # TODO: all page generations here
    return


def generate_posts(config, post):
    post_directory = config['output']['subpages location'] + '/'  # TODO: check for / at the end
    post_file_name = post[-2:]+'.html'
    with open(post_directory+post_file_name, 'r') as web_post:
        web_post.write(post)
    return


def generate(config):
    # TODO:
    # generate all posts
    # generate index
    directory = config['input']['posts directory']+'/'
    for post in listdir(directory):
        dir = directory+post
        print(dir)
        if not isfile(dir) or dir[-3:] != '.md':
            continue
        with open(directory+post, 'r') as markdown_post:
            print(markdown_pages.demarkdownifier(markdown_post.read())['html'])
            print(markdown_pages.demarkdownifier(markdown_post.read())['metadata'])
    return
