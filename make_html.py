from glob import glob
import os.path as osp
'''
Script for generating the rows in an html table that link to the tabs in tabs/.

To run, set up template.html with whatever html you want, then put #TABLEROWS# 
in the spot where the rows should be inserted.

The tabs in tabs/ need to be named in the form <artist>-<songname>.

The output html is songbook.html.
'''

tab_files = sorted(glob('tabs/*.txt'))

table_str = ''

for tab_file in tab_files:
    artist, song = osp.basename(tab_file).split('-')
    song = song.split('.')[0]
    artist = artist.replace('_',' ')
    song = song.replace('_',' ')

    row = f'''
    <tr>
    <td>{artist}</td>
    <td><a href="{tab_file}">{song}</a></td>
    </tr>'''

    table_str += row


with open('songbook_template.html','r') as f:
    html_str = f.read()

html_str = html_str.replace('#TABLEROWS#', table_str)

with open('songbook.html','w') as f:
    f.write(html_str)
