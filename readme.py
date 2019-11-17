import os
import glob

def replace_file(oldname, newname):
    os.remove(newname)
    os.rename(oldname, newname)
    return

guides = [each.split('/')[1] for each in glob.glob('guides/*.md')]

with open('READ.md', 'a') as fh:
    fh.write('# Stuff and the rest\n\n')

    fh.write('## Links\n\n')
    fh.write(f'1. <https://github.com/chidimo/Bookmarks>\n')
    fh.write(f'1. <https://github.com/chidimo/reference>\n')
    fh.write(f'1. <https://github.com/chidimo/ALC-4.0-Mobile-Web-Specialist-Roadmap>\n\n')

    fh.write('## Algorithms\n\n')

    fh.write('## Analysis\n\n')

    fh.write('## Git-tools\n\n')

    fh.write('## Guides\n\n')
    for name in [file.split('.md')[0] for file in sorted(guides)]:
        link = f'1. [{name}](guides/{name}.md)\n'
        fh.write(link)

    fh.write('## Hackerrank\n\n')

    fh.write('## JavaScript\n\n')

    fh.write('## Mathematics\n\n')

    fh.write('## Project Euler\n\n')

    fh.write('## Python\n\n')


replace_file('READ.md', 'README.md')
