#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to your web servers"""

from fabric.api import local, env, put, run
from os.path import exists
from datetime import datetime

env.hosts = ['54.197.21.189', '52.72.26.58']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """Packs the version of the project"""
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        file_name = "versions/web_static_{}.tgz".format(current_time)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print("An error occurred while packing:", e)
        return None


def do_deploy(archive_path):
    """Deploys the archive to the web servers"""
    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        archive_name = archive_path.split("/")[1].split(".")[0]
        run("mkdir -p /data/web_static/releases/{}/".format(archive_name))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(archive_name, archive_name))
        run("rm /tmp/{}.tgz".format(archive_name))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/"
            .format(archive_name, archive_name))
        run("rm -rf /data/web_static/releases/{}/web_static"
            .format(archive_name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ "
            "/data/web_static/current"
            .format(archive_name))
        return True
    except Exception as e:
        print("An error occurred while deploying:", e)
        return False


def deploy():
    """Deploys the archive to your web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
