from glob import glob
import os.path as osp
'''
Script for generating the rows in an html table that link to the tabs in tabs/.

To run, set up template.html with whatever html you want, then put #TABLEROWS# 
in the spot where the rows should be inserted.

The tabs in tabs/ need to be named in the form <artist>-<songname>.

The output html is songbook.html.
'''

tab_files = sorted(glob('tabs_raw/*.txt'))

# Make table of links
table_str = ''
for tab_file in tab_files:
    artist, song_name = osp.basename(tab_file).split('-')
    song_name = song_name.split('.')[0]
    song_name = song_name.replace('_',' ')
    artist = artist.replace('_', ' ')

    row = f'''
    <tr>
    <td>{artist}</td>
    <td><a href="tabs_html/{osp.basename(tab_file).split(".")[0]}.html">{song_name}</a></td>
    </tr>'''

    table_str += row


with open('songbook_template.html','r') as f:
    html_str = f.read()

html_str = html_str.replace('#TABLEROWS#', table_str)

with open('songbook.html','w') as f:
    f.write(html_str)


# Make html pages
with open('song_template.html', 'r') as f:
    tab_template_str = f.read()

for tab_file in tab_files:
    artist, song_name = osp.basename(tab_file).split('-')
    song_name = song_name.split('.')[0]
    song_name = song_name.replace('_',' ')
    artist = artist.replace('_', ' ')

    with open(tab_file, 'r') as f:
        tab = f.read()

    tab = tab.replace('\n','<br>')

    tab_str = tab_template_str.replace('#TITLE#', f'{artist} - {song_name}')
    tab_str = tab_str.replace('#ARTIST_NAME#', artist)
    tab_str = tab_str.replace('#SONG_NAME#', song_name)
    tab_str = tab_str.replace('#TAB#', tab)

    with open(f'tabs_html/{osp.basename(tab_file).split(".")[0]}.html','w') as f:
        f.write(tab_str)
