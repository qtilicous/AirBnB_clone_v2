#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder
"""

from fabric.api import local
from datetime import datetime
from os.path import isdir


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder"""
    try:
        if not isdir("versions"):
            local("mkdir -p versions")
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(current_time)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        print("An error occurred:", e)
        return None
