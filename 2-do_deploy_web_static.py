#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from fabric.api import env, put, run
from os.path import exists
env.hosts = ['54.197.21.189', '52.72.26.58']


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp')

        # Uncompress the archive to the folder
        # /data/web_static/releases/<archive filename without extension>
        file_name = archive_path.split('/')[-1]
        file_name_without_extension = file_name.split('.')[0]
        run('mkdir -p /data/web_static/releases/{}/'
            .format(file_name_without_extension))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(file_name, file_name_without_extension))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(file_name))

        # Move the uncompressed files to the proper location
        run('mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'
            .format(file_name_without_extension,
                    file_name_without_extension))

        # Delete the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s /data/web_static/releases/{}/ '
            '/data/web_static/current'
            .format(file_name_without_extension))

        print("New version deployed!")
        return True

    except Exception as e:
        print(e)
        return False
