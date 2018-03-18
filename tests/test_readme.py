import os
import re


def test_readme_links():
    project_path = os.path.dirname(os.path.dirname(__file__))
    readme_path = os.path.join(project_path, 'README.rst')
    link_re = re.compile('<(.*)>')

    for line in open(readme_path):
        match = link_re.search(line)
        if match:
            link = match.group(1)
            if link.startswith('examples/'):
                assert os.path.exists(os.path.join(project_path, link))
