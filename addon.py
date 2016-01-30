from xbmcswift2 import Plugin, xbmcgui
from resources.lib import topdocos

plugin = Plugin()


@plugin.route('/')
def main_menu():

    items = [
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('videos'),
        },
    ]
    
    return items


@plugin.route('/videos/')
def get_videos():
    
    items = []

    content = topdocos.get_section(SITE_URL, 'recently added')

    for i in content:
        items.append({
            'label': i['label'],
            'path': plugin.url_for('play_content', url=i['path']),
            'thumbnail': i['thumbnail'],
        })

    return items


    content = topdocos.get_section(SITE_URL, 'highest rated')

    for i in content:
        items.append({
            'label': i['label'],
        })

    return items


if __name__ == '__main__':
    plugin.run()
