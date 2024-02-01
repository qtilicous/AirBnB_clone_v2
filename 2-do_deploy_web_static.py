#!/usr/bin/env python3
"""
Fabric script that distributes an archive to your web servers,
using the function do_deploy
"""

from fabric.api import *
import os

env.hosts = ['54.197.21.189', '52.72.26.58']
env.user = 'root'
env.key_filename = '/root/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not os.path.exists(archive_path):
        return False

    filename = os.path.basename(archive_path)
    file_no_ext = os.path.splitext(filename)[0]

    try:
        put(archive_path, '/tmp/')

        run('mkdir -p /data/web_static/releases/{}/'.format(file_no_ext))
        run(
                'tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
                .format(filename, file_no_ext)
                )

        run('rm /tmp/{}'.format(filename))

        run('rm -rf /data/web_static/current')

        run(
                'ln -s /data/web_static/releases/{}/ /data/web_static/current'
                .format(file_no_ext)
                )

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"An error occurred during deployment: {e}")
        return False
